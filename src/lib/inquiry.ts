export const INQUIRY_ENDPOINT = "https://formsubmit.co/ajax/6ce64b567952517019a3b75ba1d51e67";

export function providerAccepted(response: unknown): boolean {
  if (!response || typeof response !== "object") return false;
  const result = response as { success?: unknown; message?: unknown };
  return (result.success === true || result.success === "true") &&
    typeof result.message === "string" &&
    result.message === "The form was submitted successfully.";
}

export async function submitInquiry(payload: Record<string, string>, send: typeof fetch = fetch): Promise<void> {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 20_000);
  try {
    const response = await send(INQUIRY_ENDPOINT, {
      method: "POST",
      headers: { "Accept": "application/json", "Content-Type": "application/json" },
      body: JSON.stringify(payload),
      signal: controller.signal,
    });
    if (!response.ok || !providerAccepted(await response.json())) throw new Error("Submission not confirmed");
  } finally {
    clearTimeout(timeout);
  }
}
