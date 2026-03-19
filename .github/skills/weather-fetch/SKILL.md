---
name: weather-fetch
description: Fetches the current weather forecast for a given location and date range using wttr.in. Returns temperature, conditions, and precipitation summary. No API key required.
allowed-tools: Bash, Read
---

# Weather Fetch

Retrieves a live weather forecast for a location and travel dates.

---

## Auto-Triggers

Auto-triggered by keywords:

- "weather", "forecast", "what's the weather"
- "weather for my trip", "check the weather in"

---

## Workflow

### 1. Confirm Inputs

Required:
- **Location** — city name or city + state (e.g. "San Diego" or "San Diego, CA")
- **Travel dates** — start and end date (e.g. "March 20–23")

If either is missing, ask before proceeding.

### 2. Fetch Forecast

Run the following command, replacing `{LOCATION}` with the URL-encoded location:

```bash
curl -s "wttr.in/{LOCATION}?format=4"
```

For a compact 3-day forecast:
```bash
curl -s "wttr.in/{LOCATION}?format=%l:+%c+%t+%h+%w%n"
```

Example for San Diego:
```bash
curl -s "wttr.in/San+Diego?format=4"
```

### 3. Parse and Return

Return a structured summary:

```
Location: [city]
Dates: [travel dates]
Forecast:
  - Day 1: [conditions], high [temp], low [temp], precipitation [%]
  - Day 2: ...
  - Day 3: ...
Overall: [one sentence summary — e.g. "Warm and sunny with no rain expected"]
```

---

## Guardrails

- If `wttr.in` returns an error or empty result, say: *"I couldn't fetch live weather for that location. Try a nearby major city."*
- Do not invent weather data. Only report what the API returns.
- If travel dates are more than 3 days out, note that forecasts beyond 3 days are estimates.

## UDL + EL Supports (Required)

- Follow the shared baseline in `.github/UDL-EL-SUPPORT.md`.
- Front-load simple vocabulary when needed: `forecast`, `conditions`, `temperature`, `estimate`.
- If a student gives a vague place, ask for a more specific city or region.
- If a student struggles to explain the result, give a frame: “The forecast for ___ shows ___, so I should pack ___.”
- Keep final returned weather summary in English.
- Before final output, confirm the quick checklist in `.github/UDL-EL-SUPPORT.md` was met.
