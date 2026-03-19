# Week 1 · Period 3 — Sandbox Facilitation Guide
## "What Can an AI Agent Actually Do?"

**Duration:** 40 minutes  
**Setting:** Full class — teacher-led demo → student explore → group debrief  
**Repo:** `wiggum-sandbox` (separate from the main project — no student code today)

---

## Learning Goal

Students experience the difference between a raw LLM prompt and an orchestrated agent + skill system — without touching their own project yet.

> **I can** explain what makes an agent different from a simple chatbot prompt.  
> **I can** describe how a skill gives an agent access to real-world data.  
> **I can** give an example of how prompt specificity changes output quality.

---

## Materials

- Student devices with Copilot (or teacher projector for whole-class demo)
- `wiggum-sandbox` repo open (or shared screen)
- Reflection file template: `reflections/week1-sandbox-reflection.md`
- Reflection agent: `.github/agents/reflection-coach.md`

---

## Timing

| Block | Time | What Happens |
|-------|------|--------------|
| Bell Ringer (Think-Pair-Share) | 5 min | Students activate prior knowledge while devices and logins finish loading |
| Concept Frame | 2 min | Teacher explains agent vs. skill (use whiteboard or slides) |
| Live Demo | 8 min | Teacher runs trip-planner agent on projector with class input |
| Student Try | 15 min | Students run it themselves — two rounds (vague → specific) |
| Debrief | 10 min | Structured group discussion |

---

## Bell Ringer (5 minutes) — Think-Pair-Share

Prompt on board:

> **"If you could go anywhere, where would you go and what would you do?"**

Flow:
1. **Think (1 min):** Students write one destination and 1–2 activities.
2. **Pair (2 min):** Share with a partner and ask one follow-up question.
3. **Share (2 min):** 2–3 volunteers share out.

Bridge line to lesson:

> "Great—now we’ll test how AI output changes when your travel idea is vague vs. specific."

UDL/EL support move:
- Students may brainstorm in Spanish first.
- Before share-out, ask for one English sentence using this frame:
   - "I would go to ___ and I would ___ because ___."

---

## Block 1: Concept Frame (2 minutes)

Draw or display this on the board:

```
Prompt alone:      "Plan my trip to Hawaii"
                          ↓
                    [LLM guesses]

Agent + Skills:    destination + dates + purpose
                          ↓
              [weather-fetch: wttr.in → real forecast]
              [activities-finder: web search → real places]
                          ↓
              [trip-planner: combines data → packing list]
```

Say to students:
> "Today you're going to use a trip planner that isn't just one prompt — it's an agent that calls two skills. One fetches real weather data. One searches for real activities. The agent puts it all together. Let's see what that looks like."

---

## Block 2: Live Demo (8 minutes)

Open the `trip-planner` agent on the projector. Use this as your demo input:

**Round 1 — Vague input:**
> "I'm going to Denver for a few days."

Show the class the output. Point out:
- What data did `weather-fetch` return?
- What did `activities-finder` find?
- What's in the packing list? What's missing because the input was vague?

**Round 2 — Specific input (same city):**
> "I'm going to Denver, Colorado from June 14–18. It's a hiking trip with two friends. We want to do at least one 14er and eat well."

Compare side by side with Round 1.  
Ask: *"What changed? Why?"*

---

## Block 3: Student Try (20 minutes)

**Instructions to give students:**

> "Open the wiggum-sandbox repo and use the trip-planner agent. Run it twice:  
> 1. Give it a real destination but very vague purpose — like 'I want to relax.'  
> 2. Give it the same destination but be very specific — include dates, who's going, and what you want to do.  
>  
> Screenshot or copy both outputs. You'll use them in the debrief."

**Optional challenge prompt (for fast finishers):**
> "Try a fake location — like 'Bikini Bottom' or 'Springfield, USA.' What happens? What does the agent do when skills can't find data?"

---

## Block 4: Debrief (10 minutes)

### Discussion questions (pick 2–3 based on time):

1. **What changed between your vague and specific inputs?**  
   *(Expected: more relevant packing items, better activity fit, more personalized tone)*

2. **Which part do you think is the hardest for the AI — fetching the weather, finding activities, or combining them into a packing list? Why?**

3. **The weather-fetch skill uses a real website (wttr.in) — it doesn't make up the forecast. Why does that matter?**  
   *(Connect to: hallucination, reliability, trust in AI outputs)*

4. **If you were building an app for your school community, what kind of "skill" would be useful to connect to it?**  
   *(This previews Week 2 need finding — let students brainstorm freely)*

5. **What would break this agent?**  
   *(Encourage: fake location, no dates, typos in city names, unsupported language)*

---

## Reflection Submission (GitHub Classroom)

Use the reflection agent in `.github/agents/reflection-coach.md` and save the final artifact in `reflections/week1-sandbox-reflection.md`.

The sandbox-wide language support baseline lives in `.github/UDL-EL-SUPPORT.md`.

Student flow:
1. Open the **reflection-coach** agent.
2. Answer the guided questions about the two trip-planner runs.
3. Keep the final reflection in English (students may brainstorm in another language first).
4. Student writes and saves `reflections/week1-sandbox-reflection.md` (agent gives coaching feedback only).
5. Commit and push the completed reflection.
6. GitHub Actions runs the classroom reflection check automatically.

---

## What to Avoid Today

- **Don't connect this to the student project** — this is exploration only.
- **Don't troubleshoot Codespaces setup** — that's for P1/P2 this week. If something's broken, skip and use the projector.
- **Don't let the demo run long** — cut off at 8 minutes even if output is interesting. Student time matters more.
- **Don't accept uncommitted reflections** — the commit is the submission evidence.

---

## Teacher Notes

- The `weather-fetch` skill calls `wttr.in` — it works in Codespaces with no API key. It fails gracefully if the location is too vague (e.g., "the mountains").
- The `activities-finder` skill uses web search as primary — if Copilot's web access is off, it falls back to Wikipedia. Worth testing before class.
- The `trip-planner` agent won't proceed without destination + dates + purpose — it asks for them. This is **intentional behavior to point out**: the agent has guardrails, just like students will build into their own apps.
- The reflection check workflow catches incomplete submissions by checking for required headings, placeholder text, and empty sections.
- If class energy allows, the debrief question *"What skill would be useful for your future app?"* makes an excellent bridge into Week 2's need-finding session.

---

## Exit Ticket (Single Question)

**In one sentence, explain the difference between an `agent` and a `skill` using this sandbox.**

Sentence frame (if needed):
- "In this sandbox, the agent is ___, and the skills are ___ because ___."
