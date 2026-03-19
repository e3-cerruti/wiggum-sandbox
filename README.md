# Week 1 Sandbox — Trip Planner

You are going to use an AI agent that plans a trip using **real weather data** and **real activity suggestions**.

Your job today:
1. Run the agent **twice** — once with a vague prompt, once with a specific one
2. Write a reflection about what changed and why

---

## Step 1 — Open Copilot Chat in Agent Mode

1. Click the **Copilot Chat** icon in the left sidebar
2. At the top of the chat panel, switch the mode to **Agent**
3. Select the **trip-planner** agent from the list

---

## Step 2 — Run 1: Vague Prompt

Give the agent a real destination but keep the details minimal.

**Example:**
> I want to go to Denver for a few days.

Watch what the agent does:
- It calls a **weather skill** to get a real forecast
- It calls an **activities skill** to find things to do
- It combines both into a packing list and a sample day

**Scroll up in your chat to find this output** — you will compare it to Run 2.

---

## Step 3 — Run 2: Specific Prompt

Use the **same destination** but give the agent as much detail as possible.

Include all of these:
- Exact city and state
- Travel dates (start and end)
- Trip purpose (hiking, beach, family visit, etc.)
- Who is going (solo, with friends, family with kids, etc.)
- One thing you definitely want to do

**Example:**
> I'm going to Denver, Colorado from June 14–18. It's a hiking trip with two friends. We want to do at least one 14er and eat well downtown.

**Scroll up in your chat when you need to compare** — both runs stay in your chat history.

---

## Step 4 — Compare the Two Runs

Scroll up in your chat to find Run 1 and Run 2 side by side.

Look for **at least two specific differences**:

- Did the packing list change? What items appeared or disappeared?
- Were the activity suggestions different?
- Did the agent sound more confident or specific?

These differences are your evidence for the reflection.

---

## Step 5 — Write Your Reflection

1. Open **Copilot Chat** and switch to the **reflection-coach** agent
2. The coach will ask you questions about your two runs
3. Answer honestly using specific evidence from what you saw
4. The coach will help you turn your answers into a written reflection
5. When you are done, your reflection goes into this file:

   [reflections/week1-sandbox-reflection.md](reflections/week1-sandbox-reflection.md)

**You write it. The coach only asks questions and gives feedback.**

---

## Step 6 — Submit

1. Save [reflections/week1-sandbox-reflection.md](reflections/week1-sandbox-reflection.md)
2. Open the **Source Control** panel (the branch icon in the left sidebar)
3. Stage your file, write a commit message, and click **Commit**
4. Click **Sync** (or **Push**) to submit

GitHub will automatically check that your reflection is complete.

---

## Optional Challenge — Try a Fake Location

Once your reflection is submitted, try giving the agent a location that doesn't exist:

> I want to go to Bikini Bottom for a week. It's a beach trip.

**Questions to think about:**
- What does the agent do when the weather skill can't find data?
- What does it do when the activities skill has nothing to return?
- What does that tell you about how agents handle bad input?

---

## If Something Looks Wrong

| Problem | Try this |
|---|---|
| Weather data looks generic or missing | Use a full city name: "Denver, Colorado" not "the mountains" |
| Activities list is just a Wikipedia paragraph | Add a trip purpose like "hiking" or "sightseeing" |
| Agent keeps asking for more info | It needs destination, dates, and purpose before it will continue |
| Reflection coach says a section is empty | Go back and add a specific example from one of your two runs |
