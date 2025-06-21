
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys

def run_app():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Overseer GUI")
    layout = QVBoxLayout()
    layout.addWidget(QLabel("Welcome to Overseer"))
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())
