import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QColorDialog, QFontDialog

class WidgetPropertiesApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widget Properties")
        self.setGeometry(100, 100, 300, 200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.button = QPushButton("Bắt đầu Game")
        self.button = QPushButton("Thoát Game")

        layout = QVBoxLayout()

        layout.addWidget(self.button)

        central_widget.setLayout(layout)


   

def main():
    app = QApplication(sys.argv)

    window = WidgetPropertiesApp()

    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
