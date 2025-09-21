# AI Fitness & Nutrition Tracker (Hackathon Project)

This is a Streamlit web app powered by Ollama LLM, helping users get personalized fitness and nutrition plans, and track their progress over time.

## Features
- User inputs body measurements and sets fitness goals.
- AI creates diet and workout plans based on the data.
- Weekly progress tracking and adaptive plan updates.
- All data processed locally for privacy.

## Setup

1. Clone this repo.
2. Set up Python 3.10+ and install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. [Install Ollama](https://ollama.com) and download your LLM (e.g., `ollama pull llama2`).
4. Start Ollama (`ollama run llama2` or server as needed).
5. Run the app:
    ```
    streamlit run app.py
    ```

## Folder Structure

- `frontend/` – All Streamlit UI code/modules.
- `backend/` – Ollama integration, data logic.
- `data/` – (Optional) Local storage for user data or weekly tracking.

**Refer to the `requirements.txt` and `.gitignore` in the root.**

## Contribution

- Use meaningful branch names (e.g., `feature/ui-inputs` or `feature/ollama-integration`)
- Submit PRs for review.
- Update/read issues to track task assignments.

*Built for Hackathon 2025.*
