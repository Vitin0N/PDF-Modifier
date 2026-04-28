from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QStackedWidget, QLabel
)

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PDF Modifier')
        self.resize(800, 600)

        centralWidget =  QWidget()
        self.setCentralWidget(centralWidget)

        mainLayout = QHBoxLayout(centralWidget)

        menuLayout = QVBoxLayout()

        self.homeBtn = QPushButton('Home')
        self.mergeBtn = QPushButton('Merge PDFs')

        menuLayout.addWidget(self.homeBtn)
        menuLayout.addWidget(self.mergeBtn)
        menuLayout.addStretch()

        self.stackWidget =  QStackedWidget()

        homeScreen = QLabel('Welcome to PDFs Modifier')
        mergeScreen = QLabel('Merge PDFs')


        self.stackWidget.addWidget(homeScreen)  # index 0 
        self.stackWidget.addWidget(mergeScreen) # index 1

        mainLayout.addLayout(menuLayout)
        mainLayout.addWidget(self.stackWidget)

        self.homeBtn.clicked.connect(self.showHomeScreen)
        self.mergeBtn.clicked.connect(self.showMergeScreen)

    def showHomeScreen(self):
        print('home screen')
        self.stackWidget.setCurrentIndex(0)

    def showMergeScreen(self):
        print('merge srcreen')
        self.stackWidget.setCurrentIndex(1)
