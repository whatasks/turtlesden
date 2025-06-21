import sys
import threading
import random
import os
from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QTextEdit,
    QVBoxLayout, QComboBox, QCheckBox, QApplication, QFileDialog
)
from PyQt6.QtCore import pyqtSignal, QObject, Qt

# Mock certification bank
CERT_QUESTIONS = [
    "What is 2+2?",
    "How do you use a for loop?",
    "What is a lambda function?",
    "Explain recursion in simple terms."
]

# --- Mock agent response function ---
def mock_agent_response(prompt):
    if "2+2" in prompt:
        return "4"
    if "loop" in prompt:
        return "for i in range(10): print(i)"
    if "lambda" in prompt:
        return "lambda x: x * 2"
    if "recursion" in prompt:
        return "A function calling itself with a base case."
    return "Unsure."

# --- Certification simulator ---
def simulate_certification(prompt):
    answer = mock_agent_response(prompt)
    eval_result = "pass" if answer else "fail"
    reasoning = f"Prompt understood as '{prompt}', produced: '{answer}'"
    return {"question": prompt, "answer": answer, "evaluation": eval_result, "reasoning": reasoning}

# --- Signals class ---
class WorkerSignals(QObject):
    result_ready = pyqtSignal(dict)

# --- Background thread for training ---
class TrainingWorker(threading.Thread):
    def __init__(self, signals, running_flag):
        super().__init__()
        self.signals = signals
        self.running_flag = running_flag

    def run(self):
        while self.running_flag["enabled"]:
            q = random.choice(CERT_QUESTIONS)
            result = simulate_certification(q)
            self.signals.result_ready.emit(result)
            for _ in range(5):
                if not self.running_flag["enabled"]:
                    break
                threading.Event().wait(1)

# --- GUI Application ---
class OverseerApp_TrainingToggle(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Overseer Training View")
        self.resize(800, 600)

        self.training_enabled = {"enabled": False}

        self.agent_selector = QComboBox()
        self.agent_selector.addItems(["MockAgent"])

        self.toggle_training = QCheckBox("Enable Training Mode")
        self.toggle_training.stateChanged.connect(self.toggle_training_mode)

        self.drop_label = QLabel("Drag & Drop a File Here")
        self.drop_label.setStyleSheet("border: 2px dashed gray;")
        self.drop_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.drop_label.setFixedHeight(100)
        self.setAcceptDrops(True)

        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Select Agent:"))
        layout.addWidget(self.agent_selector)
        layout.addWidget(self.toggle_training)
        layout.addWidget(self.drop_label)
        layout.addWidget(QLabel("Training Log:"))
        layout.addWidget(self.results_display)
        self.setLayout(layout)

        self.signals = WorkerSignals()
        self.signals.result_ready.connect(self.display_result)

    def toggle_training_mode(self, state):
        if state == Qt.CheckState.Checked:
            self.training_enabled["enabled"] = True
            self.results_display.append("🔁 Training mode started...\n")
            self.worker = TrainingWorker(self.signals, self.training_enabled)
            self.worker.start()
        else:
            self.training_enabled["enabled"] = False
            self.results_display.append("⏹️ Training mode stopped.\n")

    def display_result(self, result):
        summary = (
            f"🧠 Thinking...\n"
            f"Q: {result['question']}\n"
            f"A: {result['answer']}\n"
            f"Evaluation: {result['evaluation'].upper()}\n"
            f"Reasoning: {result['reasoning']}\n\n"
        )
        self.results_display.append(summary)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        if files:
            file_info = os.path.basename(files[0])
            self.results_display.append(f"📁 File dropped: {file_info}\n")

# Entry point (for testing directly)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OverseerApp_TrainingToggle()
    window.show()
    sys.exit(app.exec())
