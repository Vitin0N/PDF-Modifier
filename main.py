import sys
from PySide6.QtWidgets import QApplication

from interface.appWindow import AppWindow

app = QApplication(sys.argv)

window = AppWindow()

window.show()

sys.exit(app.exec())