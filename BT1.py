import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QColorDialog, QFontDialog
from PyQt5.QtCore import Qt

class TextDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hiển thi ứng dụng")
        self.setGeometry(100, 100, 400, 200)  # (x, y, width, height)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

  
        self.start_button = QPushButton("Bắt đầu Game")

        self.button = QPushButton("Thoát Game")
        

        layout = QVBoxLayout()

      
        layout.addWidget(self.start_button)
        layout.addWidget(self.button)
        

        central_widget.setLayout(layout)


        self.start_button.clicked.connect(self.show_Start)
        self.button.clicked.connect(self.dialog_Quit)

    def show_Start(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("!!!")

        label = QLabel("Chương trình đã bắt đầu")

        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)

        dialog.setLayout(dialog_layout)

        dialog.exec_()
        
    def dialog_Quit(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("!!!")

        label = QLabel("Bạn đã thoát game")

        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)

        dialog.setLayout(dialog_layout)

        dialog.exec_()
        
def main():
    app = QApplication(sys.argv)

    window = TextDisplayApp()

    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()