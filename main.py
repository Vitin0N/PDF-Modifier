import sys
from PySide6.QtWidgets import QApplication

from appWindow import AppWindow

app = QApplication(sys.argv)

window = AppWindow()

window.show()

sys.exit(app.exec())