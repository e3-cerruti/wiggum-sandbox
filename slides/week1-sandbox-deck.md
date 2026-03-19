---
marp: true
theme: default
paginate: true
size: 16:9
title: Week 1 Sandbox — Agents, Skills, and Prompt Quality
---

# Week 1 Sandbox
## Agents, Skills, and Prompt Quality

**e3 Civic High**  
Congressional App Challenge Accelerator

---

## Bell Ringer (Think-Pair-Share)

**Prompt:**  
If you could go anywhere, where would you go and what would you do?

- **Think (1 min):** write destination + 1–2 activities
- **Pair (2 min):** share and ask one follow-up
- **Share (2 min):** 2–3 volunteers

Sentence frame:  
**I would go to ___ and I would ___ because ___.**

---

## Learning Targets

- I can explain the difference between an `agent` and a `skill`.
- I can describe how prompt specificity changes output quality.
- I can use evidence from two runs to support my claims.

---

## The Problem with Prompts

Prompt-only requests can be:
- too vague
- too generic
- less reliable

Example:
- “Plan my trip” → broad output
- “Plan my Denver hiking trip, June 14–18, with two friends” → focused output

---

## Agents

An `agent` is a role-focused helper that:
- follows a job
- asks for missing details
- combines tools/skills to complete a task

In this sandbox:
- `trip-planner` is the agent

---

## Skills

A `skill` is a reusable tool action that:
- does one specific job well
- can be reused by different agents

In this sandbox:
- `weather-fetch` gets forecast data
- `activities-finder` gets destination activities

---

## Today's Example

Flow:
1. Student prompt (destination + dates + purpose)
2. `trip-planner` agent orchestrates
3. `weather-fetch` + `activities-finder` run
4. Output: focused packing list

Why this matters:
- better prompts + right tools = better outputs

<!--
---
## Demo Flow (Teacher)

1. Run `trip-planner` with a vague input
2. Run `trip-planner` with a specific input
3. Compare outputs

Look for:
- specificity of packing list
- relevance of activities
- confidence/trust in output
-->

---

## Student Activity (Two Runs)

Run 1: **Vague prompt**  
Run 2: **Specific prompt** (destination, dates, purpose, who’s going, must-do activity)

Capture evidence:
- at least **2 exact differences**
- what prompt detail caused each difference

---

## Reflection Submission (Student-Written)

Open `reflection-coach` for guidance.  
You write your own final reflection in:

`reflections/week1-sandbox-reflection.md`

Requirements:
- all five sections filled in
- final text in English
- concrete evidence from both runs (two exact differences)

---

## Turn-In Workflow

1. Save reflection in repo
2. Commit + push
3. GitHub Classroom checks completeness automatically

The check catches:
- missing file
- missing sections
- placeholder text left in file
- sections with no evidence

---

## Bridge to Week 2

Need finding starts next.

Question to carry forward:
- What skill might your future CAC app need?
- Who in your community would it help?

---

## Exit Ticket (1 question)

In one sentence, explain the difference between an `agent` and a `skill` using this sandbox.

Sentence frame:  
**In this sandbox, the agent is ___, and the skills are ___ because ___.**
