import threading
from datetime import datetime
import os
import json
from PyQt6.QtCore import QObject, pyqtSignal

from overseer_core.cert_engine import simulate_certification_test
from overseer_core.agent_mock import mock_agent_response

class WorkerSignals(QObject):
    result_ready = pyqtSignal(dict)

class CertificationWorker(threading.Thread):
    def __init__(self, agent_name, signals):
        super().__init__()
        self.agent_name = agent_name
        self.signals = signals

    def run(self):
        if self.agent_name == "MockAgent":
            results = simulate_certification_test(mock_agent_response)
        else:
            results = {
                "status": {
                    "question": "N/A",
                    "answer": "N/A",
                    "evaluation": f"Agent '{self.agent_name}' is not yet integrated."
                }
            }

        try:
            os.makedirs("logs", exist_ok=True)
            log_path = os.path.join("logs", "training_logs.json")

            log_entry = {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "agent": self.agent_name,
                "results": results
            }

            if os.path.exists(log_path):
                with open(log_path, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                        if not isinstance(data, list):
                            data = [data]
                    except json.JSONDecodeError:
                        data = []
            else:
                data = []

            data.append(log_entry)

            with open(log_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)

        except Exception as e:
            print(f"[Logging Error] Failed to write log: {e}")

        self.signals.result_ready.emit(results)