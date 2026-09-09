import { defineCollection } from "astro:content";
import { z } from "astro/zod";
import { glob } from "astro/loaders";

const faqItemSchema = z.object({
	q: z.string(),
	a: z.string(),
});

const areaServedSchema = z.object({
	type: z.enum(["City", "State", "Country", "AdministrativeArea"]),
	name: z.string(),
	state: z.string().optional(),
});

const seoPages = defineCollection({
	loader: glob({ pattern: "**/*.mdx", base: "./content/seo-pages" }),
	schema: z.object({
		title: z.string(),
		description: z.string(),
		h1: z.string(),
		heroKicker: z.string(),
		heroSubtitle: z.string(),
		trustLine: z.string().default("Clear scope. No surprises. No long-term contracts."),
		ctaPreset: z.enum(["audit", "call", "contact"]).default("audit"),
		ctaText: z.string().optional(),
		ctaHref: z.string().optional(),
		finalCtaHeadline: z.string(),
		finalCtaSubtext: z.string().optional(),

		vertical: z.string(),
		geo: z.string().optional(),
		region: z.string().optional(),
		pageType: z.enum(["geo", "vertical", "practice-type"]),

		relatedPages: z.array(z.string()).default([]),

		areaServed: areaServedSchema.optional(),

		faqs: z.array(faqItemSchema).default([]),

		faqSectionTitle: z.string().optional(),
		faqSectionSubtitle: z.string().optional(),
	}),
});

const resources = defineCollection({
	loader: glob({ pattern: "**/*.mdx", base: "./content/resources" }),
	schema: z.object({
		title: z.string(),
		description: z.string().default(""),
		date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "Date must be YYYY-MM-DD").optional(),
		type: z.enum(["teardown", "guide", "template"]),
		updatedDate: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "Updated date must be YYYY-MM-DD").optional(),
		tags: z.array(z.string()).default([]),
		vertical: z.string().optional(),
		draft: z.boolean().default(false),
	}),
});

export const collections = { seoPages, resources };
