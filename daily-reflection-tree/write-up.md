# Design Rationale: The Daily Reflection Tree

## 1. Core Objective
The goal of this Knowledge Engineering project was to translate abstract psychological concepts—Locus of Control, Contribution Orientation, and Altrocentrism—into a deterministic, branching logic tree. The design ensures that a tired employee at the end of their day is guided toward self-awareness without the unpredictability or "hallucination" risks associated with live LLMs.

## 2. Psychological Grounding
The tree is built upon three foundational psychological pillars:
* **Axis 1: Locus (Victim vs. Victor):** Based on Julian Rotter’s Locus of Control. The questions detect whether the user attributes their day's outcomes to external forces (Victim) or their own actions (Victor).
* **Axis 2: Orientation (Contribution vs. Entitlement):** This section draws from Organizational Citizenship Behavior (OCB). It surfaces whether an employee is focused on what the company "owes" them or how they can "add value" beyond their job description.
* **Axis 3: Radius (Self-Centrism vs. Altrocentrism):** Inspired by Maslow’s concept of Self-Transcendence. It measures if the employee’s mental "radius" includes the team’s struggles or is limited to personal stress.

## 3. Design Trade-offs & Branching Logic
* **Subtlety over Directness:** I chose not to use "labeling" language. Instead of asking "Are you being entitled?", I asked about their "primary focus" during moments of frustration. This reduces social desirability bias (the tendency for people to answer in a way that makes them look good).
* **Deterministic Flow:** I opted for a "Hard Tree" structure. While an AI agent could summarize free text, a deterministic tree provides an auditable path. This ensures that the same mindset always leads to the same reflection, building a "predictable mirror" for the user over time.
* **Reframing Tone:** The final nodes do not "judge." Instead, they reframe the user's path. For example, if a user lands in a "Victim/Self-Centric" path, the summary gently suggests looking for one small area of agency for the next day.

## 4. Sources Informed
* *Julian Rotter (1966):* Internal vs. External Locus of Control Scale.
* *Organ (1988):* Organizational Citizenship Behavior.
* *Abraham Maslow (1969):* Theory of Self-Transcendence.

## 5. Future Improvements
With more time, I would:
1. Implement **State Persistence** to track if a user is consistently moving from "Victim" to "Victor" over a 30-day period.
2. Add **Dynamic Interpolation** to the final summaries, allowing the tree to reference specific words the user chose in earlier branches for a more personalized "deterministic" feel.