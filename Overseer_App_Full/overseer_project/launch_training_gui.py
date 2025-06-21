import sys
from PyQt6.QtWidgets import QApplication
from overseer_core.ui_training import OverseerApp_TrainingToggle

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OverseerApp_TrainingToggle()
    window.show()
    sys.exit(app.exec())
