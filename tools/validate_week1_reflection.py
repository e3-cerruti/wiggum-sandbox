from __future__ import annotations

import re
import sys
from pathlib import Path

REFLECTION_PATH = Path("reflections/week1-sandbox-reflection.md")
REQUIRED_HEADINGS = [
    "# Week 1 Sandbox Reflection — Prompt Quality, Agents, and Skills",
    "## 1) My Two Prompt Runs",
    "### Vague Prompt",
    "### Specific Prompt",
    "## 2) Evidence of Change in Output",
    "## 3) Why the Output Changed",
    "## 4) Trust, Limits, and Improvements",
    "## 5) Connection to My CAC Project Thinking",
    "Graduate Profile Alignment:",
]
PLACEHOLDERS = [
    "REPLACE_WITH_DATE",
    "REPLACE_WITH_NAME",
    "REPLACE_WITH_YOUR_VAGUE_PROMPT",
    "REPLACE_WITH_YOUR_SPECIFIC_PROMPT",
    "REPLACE_WITH_2_OR_MORE_EXACT_DIFFERENCES_BETWEEN_OUTPUTS",
    "REPLACE_WITH_CAUSE_AND_EFFECT_EXPLANATION",
    "REPLACE_WITH_WHAT_WAS_TRUSTWORTHY_WHAT_FAILED_AND_ONE_IMPROVEMENT",
    "REPLACE_WITH_ONE_SKILL_IDEA_AND_COMMUNITY_BENEFIT",
]
SECTION_LABELS = [
    "### Vague Prompt",
    "### Specific Prompt",
    "## 2) Evidence of Change in Output",
    "## 3) Why the Output Changed",
    "## 4) Trust, Limits, and Improvements",
    "## 5) Connection to My CAC Project Thinking",
]


def fail(message: str) -> None:
    print(f"❌ {message}")
    raise SystemExit(1)


def extract_section(text: str, heading: str, next_heading: str | None = None) -> str:
    pattern = re.escape(heading) + r"\n(.*?)"
    if next_heading:
        pattern += r"(?=\n" + re.escape(next_heading) + r")"
    else:
        pattern += r"\Z"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""


def word_count(text: str) -> int:
    cleaned = re.sub(r"[`#>*_\-]", " ", text)
    return len(re.findall(r"\b[\w']+\b", cleaned))


def main() -> None:
    if not REFLECTION_PATH.exists():
        fail(f"Missing required file: {REFLECTION_PATH}")

    text = REFLECTION_PATH.read_text(encoding="utf-8")

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            fail(f"Missing required heading or label: {heading}")

    remaining_placeholders = [item for item in PLACEHOLDERS if item in text]
    if remaining_placeholders:
        fail("Reflection still contains template placeholders.")

    for index, label in enumerate(SECTION_LABELS):
        next_heading = SECTION_LABELS[index + 1] if index + 1 < len(SECTION_LABELS) else "Graduate Profile Alignment:"
        section_text = extract_section(text, label, next_heading)
        if word_count(section_text) < 5:
            fail(f"Section appears empty — add your evidence: {label}")

    print("✅ Reflection is complete enough for submission.")


if __name__ == "__main__":
    main()
