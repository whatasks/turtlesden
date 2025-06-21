### File Manifest

* **Entry Points:**
    * [`overseer_main.py`](./overseer_main.py): The main script to launch the primary application.
    * [`launch_training_gui.py`](./launch_training_gui.py): The script to launch the training-focused UI.

* **Configuration:**
    * [`.env`](./.env): Stores environment variables like API keys.
    * [`requirements.txt`](./requirements.txt): A list of all Python dependencies for the project.

* **Core Logic (`overseer_core/`):**
    * [`config.py`](./overseer_core/config.py): Loads and manages configuration settings.
    * [`cert_engine.py`](./overseer_core/cert_engine.py): The engine for running certification tests.
    * [`certification_worker.py`](./overseer_core/certification_worker.py): The background worker thread for tests.
    * [`web_search.py`](./overseer_core/web_search.py): Provides web search capabilities.
    * **Agents:**
        * [`agent_mock.py`](./overseer_core/agent_mock.py): A simple mock agent for testing.
        * [`agent_gemini.py`](./overseer_core/agent_gemini.py): The agent powered by the Gemini API.
    * **UI Files:**
        * [`ui_main.py`](./overseer_core/ui_main.py): Defines the main PyQt6 GUI window.
        * [`ui_training.py`](./overseer_core/ui_training.py): Defines the specialized training GUI.

* **GUI Module (`overseer_gui/`):**
    * [`app.py`](./overseer_gui/app.py): The main application setup for the GUI.
