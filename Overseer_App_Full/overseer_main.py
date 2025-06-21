from overseer_core.ui_main import OverseerApp
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    window = OverseerApp()
    window.show()
    app.exec()