from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel
)
from PySide6.QtCore import Qt

class HomeView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        text = QLabel('Welcome to PDF Modifier!\nSelect a process to continue.')

        text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(text)