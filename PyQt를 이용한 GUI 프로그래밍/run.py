# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic

# form_class = uic.loadUiType("main_window.ui")[0]

# class MyWindow(QMainWindow, form_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = MyWindow()
#     myWindow.show()
#     app.exec_()

#시그널과 슬롯을 연결하는 코드와 슬롯 구현부를 추가
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main_window.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        #버튼 객체에 접근하기 위해 self.pushButton을 사용
    def btn_clicked(self):
        QMessageBox.about(self, "message", "clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()