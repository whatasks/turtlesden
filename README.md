Overseer AI Controller
📖 Project Overview
Overseer is a Python-based Hivemind Controller for managing and certifying the capabilities of various AI agents. It features a robust testing engine, performance logging, and a PyQt6 graphical user interface to orchestrate and evaluate AI agent performance on a variety of tasks.

The system is designed to be modular, allowing for different AI agents (e.g., a local mock agent, a Gemini-powered agent) to be plugged in and evaluated against a standardized set of certifications.

🚀 Key Components
The project is organized into several core modules, each with a specific responsibility.

File Manifest
overseer_project/
├── .env                  # Stores environment variables like API keys securely.
├── launch_training_gui.py# Script to launch the specialized training UI.
├── overseer_main.py      # The main entry point to launch the primary Overseer application.
├── requirements.txt      # A list of all Python dependencies for the project.
│
├── logs/                 # Directory for all runtime-generated logs.
│   ├── failure_memory.jsonl  # A log of all failed certification tests for later analysis.
│   └── training_logs.jsonl   # A complete history of all training and certification runs.
│
├── overseer_core/        # Core backend logic for the entire application.
│   ├── __init__.py
│   ├── agent_gemini.py   # Logic for the agent powered by the Google Gemini API.
│   ├── agent_mock.py     # A simple, predictable mock agent for testing.
│   ├── cert_engine.py    # The main engine for running certification tests against an agent.
│   ├── certification_worker.py # Handles running tests in a background thread to keep the UI responsive.
│   ├── config.py         # Loads and manages configuration settings for the project.
│   ├── ui_main.py        # Defines the main PyQt6 GUI window and its logic.
│   ├── ui_training.py    # Defines the specialized training GUI window.
│   └── web_search.py     # Provides the agent with the ability to search the web.
│
└── overseer_gui/         # (Potential future home for modular GUI components).
    ├── __init__.py
    └── app.py            # Likely the main application setup for the GUI.
⚙️ Setup and Installation
To get the Overseer project running on your local machine, follow these steps.

1. Clone the Repository

Bash

git clone https://github.com/whatasks/Overseer-AI-Controller.git
cd Overseer-AI-Controller
2. Set Up a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.

Bash

# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install all required Python packages using the requirements.txt file.

Bash

pip install -r requirements.txt
4. Configure Environment Variables
Create a file named .env in the root directory and add any necessary API keys.

# .env file
GEMINI_API_KEY="YOUR_API_KEY_HERE"
▶️ How to Run
There are two main ways to run the application, depending on which interface you wish to use.

1. Run the Main Overseer Application:
Execute the overseer_main.py script to launch the primary certification and agent management GUI.

Bash

python overseer_main.py
2. Run the Specialized Training GUI:
Execute the launch_training_gui.py script for the training-focused interface.

Bash

python launch_training_gui.py
