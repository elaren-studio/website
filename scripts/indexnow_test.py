import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).with_name("indexnow.py")
SPEC = importlib.util.spec_from_file_location("indexnow", SCRIPT)
indexnow = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(indexnow)


class IndexNowValidationTests(unittest.TestCase):
    def test_accepts_production_url(self):
        self.assertEqual(indexnow.validate_url("https://elarenstudio.com/contact/"), "https://elarenstudio.com/contact/")

    def test_rejects_foreign_host_query_fragment_userinfo_and_port(self):
        for value in (
            "https://example.com/contact/",
            "https://elarenstudio.com/contact/?x=1",
            "https://elarenstudio.com/contact/#top",
            "https://user:pass@elarenstudio.com/contact/",
            "https://elarenstudio.com:443/contact/",
        ):
            with self.subTest(value=value), self.assertRaises(ValueError):
                indexnow.validate_url(value)

    def test_rejects_duplicate_and_over_limit_urls(self):
        with self.assertRaises(ValueError):
            indexnow.validate_urls(["https://elarenstudio.com/", "https://elarenstudio.com/"])
        with self.assertRaises(ValueError):
            indexnow.validate_urls(["https://elarenstudio.com/"] * (indexnow.MAX_URLS + 1))

    def test_dry_run_does_not_open_network(self):
        with patch.object(indexnow, "get_exact", side_effect=AssertionError("network")):
            self.assertEqual(indexnow.main(["--url", "https://elarenstudio.com/contact/"]), 0)

    def test_submit_checks_key_and_urls_before_post(self):
        with patch.object(indexnow, "get_exact", return_value=(200, b"d4491462488144a79e557134c68c5c16")) as get, patch.object(indexnow.urllib.request, "urlopen") as post:
            post.return_value.__enter__.return_value.status = 202
            self.assertEqual(indexnow.submit(["https://elarenstudio.com/contact/"], "d4491462488144a79e557134c68c5c16", "d4491462488144a79e557134c68c5c16.txt"), 202)
            self.assertEqual(get.call_count, 2)
            post.assert_called_once()


if __name__ == "__main__":
    unittest.main()
