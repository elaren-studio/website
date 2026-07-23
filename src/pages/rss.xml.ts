import rss from "@astrojs/rss";
import type { APIContext } from "astro";
import { getAllResources, getResourceUrl } from "../lib/resources";

export async function GET(context: APIContext) {
	const resources = await getAllResources();

	return rss({
		title: "Elaren Studio",
		description:
			"Guides, teardowns, and templates from Elaren Studio for clean, durable websites.",
		site: context.site!,
		items: resources
			.filter((r) => r.data.date)
			.map((r) => ({
				title: r.data.title,
				description: r.data.description || "",
				pubDate: new Date(r.data.date! + "T12:00:00Z"),
				link: getResourceUrl(r),
			})),
	});
}
