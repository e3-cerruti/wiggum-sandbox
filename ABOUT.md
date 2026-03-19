# Wiggum Sandbox

A standalone demo repo for Week 1 P3 of the Ralph Wiggum CAC Accelerator.

Students use this repo to experience a custom agent orchestrating two custom skills — **before** they build anything real.

---

## Getting Started with Codespaces

This repo is configured for **GitHub Codespaces**.

1. Open the repo in a new codespace.
2. Wait for the dev container to finish building.
3. The setup installs Copilot CLI automatically.
4. When the repo opens, the README should appear in preview mode.

Unlike the main project, hidden folders are intentionally visible here so students can inspect [.github/agents](.github/agents/), [.github/skills](.github/skills/), and the support files.

---

## What's in here

```
.github/
  agents/
    trip-planner.md       ← custom agent (orchestrates both skills)
    reflection-coach.md   ← guided reflection agent for the final artifact
  workflows/
    reflection-check.yml  ← validates the submitted reflection in GitHub Actions
  skills/
    weather-fetch/
      SKILL.md            ← fetches live weather for a location + dates
    activities-finder/
      SKILL.md            ← finds popular activities for a location
facilitation/
  week1-p3-guide.md       ← teacher facilitation guide (15–20 min)
reflections/
  week1-sandbox-reflection.md ← student summative product template
slides/
  week1-sandbox-deck.md   ← classroom deck source (Marp markdown)
  README.md               ← how to preview/export slides
tools/
  validate_week1_reflection.py ← local and CI validator for reflection completeness
```

---

## How to use it

1. Open this repo in Copilot Chat (Agent mode)
2. Select the **trip-planner** agent
3. Give it: a destination, travel dates, and trip purpose
4. Watch it call both skills and generate a packing list + itinerary
5. Select the **reflection-coach** agent ([.github/agents/reflection-coach.md](.github/agents/reflection-coach.md))
6. Complete the reflection in [reflections/week1-sandbox-reflection.md](reflections/week1-sandbox-reflection.md) (student-written; agent provides coaching only)
7. Commit and push the reflection as your submission artifact

---

## Summative Product

The summative product for this sandbox is the completed reflection file:

- [reflections/week1-sandbox-reflection.md](reflections/week1-sandbox-reflection.md)

Students may brainstorm in Spanish, but the final reflection must be in English.

GitHub Classroom can use the included workflow ([.github/workflows/reflection-check.yml](.github/workflows/reflection-check.yml)) to catch incomplete submissions such as:
- missing reflection file
- missing required sections
- template placeholders left in place
- sections with no evidence

To run the same check locally in Codespaces:

```bash
python tools/validate_week1_reflection.py
```

---

## Slides

This repo includes a slide deck source in markdown:

- [slides/week1-sandbox-deck.md](slides/week1-sandbox-deck.md)

Use Marp in VS Code to preview and export PDF/PPT. See [slides/README.md](slides/README.md).

---

## The lesson

| Concept | Demo |
|---|---|
| Agent = role/behavior | trip-planner stays focused on travel planning no matter what you ask |
| Skill = reusable operation | weather-fetch and activities-finder can be used by any agent |
| Prompt quality matters | vague input → generic list; detailed input → specific, useful list |

---

## Debrief question

> *"What changed when you gave it more detail? What happened when you gave it a made-up location?"*
