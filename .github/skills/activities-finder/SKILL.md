---
name: activities-finder
description: Finds popular activities and attractions for a given location using web search and Wikipedia. Returns a categorized list of things to do. No API key required.
allowed-tools: Bash, WebSearch, Read
---

# Activities Finder

Finds popular activities and attractions for a travel destination.

---

## Auto-Triggers

Auto-triggered by keywords:

- "activities", "things to do", "what to do in"
- "attractions", "popular spots", "what's fun in"

---

## Workflow

### 1. Confirm Input

Required:
- **Location** — city or region name
- **Trip purpose** (optional but improves results) — e.g. camping, beach, sightseeing, family trip

### 2. Fetch Location Summary (Wikipedia fallback)

```bash
LOCATION="{LOCATION_URL_ENCODED}"
curl -s "https://en.wikipedia.org/api/rest_v1/page/summary/${LOCATION}" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('extract','No summary found.'))"
```

### 3. Web Search (primary)

Search for:
```
top things to do in {LOCATION} {TRIP_PURPOSE}
```

Return the top 8–10 results, grouped by category:

```
📍 {Location} — Popular Activities

🏞️ Outdoors
  - [Activity name]: [one sentence description]

🍽️ Food & Drink
  - [Activity name]: [one sentence description]

🎭 Arts & Culture
  - [Activity name]: [one sentence description]

🏄 Adventure / Active
  - [Activity name]: [one sentence description]

💡 Local Tips
  - [One practical tip for visitors]
```

### 4. Filter by Trip Purpose

If trip purpose is provided, prioritize matching categories:
- **Camping / hiking** → Outdoors + Adventure
- **Beach** → Outdoors + Food nearby
- **City / sightseeing** → Arts & Culture + Food
- **Family** → mix of all, flag kid-friendly options

---

## Guardrails

- Do not invent activities. Only return results grounded in search or Wikipedia.
- If the location is too small for search results, suggest the nearest major city or region.
- Keep descriptions to one sentence each — this is a planning aid, not a travel guide.

## UDL + EL Supports (Required)

- Follow the shared baseline in `.github/UDL-EL-SUPPORT.md`.
- Front-load simple vocabulary when needed: `activity`, `category`, `local tip`, `relevance`.
- If trip purpose is unclear, ask one short clarifying question.
- If a student struggles to explain why an activity fits, give a frame: “This activity fits the trip because ___.”
- Keep final activity list in English.
- Before final output, confirm the quick checklist in `.github/UDL-EL-SUPPORT.md` was met.
