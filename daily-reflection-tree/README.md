# Daily Reflection Tree Agent

This repository contains a deterministic reflection tool designed for the DeepThought Knowledge Engineering Fellowship. The agent guides employees through a structured end-of-day reflection across three psychological axes: Locus of Control, Contribution Orientation, and Radius of Concern.

## Project Structure
- **/tree/**: Contains the deterministic logic.
    - `reflection-tree.json`: The structured data defining the conversation paths.
    - `tree-diagram.jpg`: Visual representation of the branching logic.
- **/agent/**: Contains the execution logic.
    - `main.py`: Python script that loads the tree and runs the interactive session.
- **/transcripts/**: Sample outputs proving the deterministic branching.
    - `persona-1-victor.md`: Growth-oriented reflection path.
    - `persona-2-victim.md`: Fixed-mindset reflection path.
- `write-up.md`: Detailed psychological rationale and design methodology.

## How to Run the Agent
1. Ensure you have **Python 3.x** installed on your system.
2. Clone this repository.
3. Open your terminal or command prompt.
4. Navigate to the `/agent/` directory:
   ```bash
   cd agent
   ```
5. Run the agent:
   ```bash
   python main.py
   ```

## Features
- **Deterministic Logic:** No LLM is used at runtime, ensuring predictable and auditable outcomes.
- **Fixed Options:** Users choose from predefined paths to surface psychological orientation.
- **Psychological Grounding:** Built on frameworks like Rotter's Locus of Control and Maslow's Self-Transcendence.
