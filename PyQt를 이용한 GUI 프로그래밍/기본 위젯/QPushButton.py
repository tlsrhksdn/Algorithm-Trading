#QPushButtonL:버튼을 생성하기 위해 사용하는 위젯

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        btn1 = QPushButton("닫기", self)
        btn1.move(20, 20)
        btn1.clicked.connect(QCoreApplication.instance().quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
    
#QCoreApplication.instance()를 이용하면 예제 16.4에서 
#app이라는 변수가 바인딩하고 있는 동일 객체를 얻어올 수 있다.
#app이 바인딩하고 있는 객체는 QApplication 클래스의 인스턴스인데 해당 객체는 quit라는 메서드를 포함한다.
#버튼을 클릭했을 때 QApplication이 제공하는 quit 메서드를 호출하도록 연결함으로서 윈도우가 종료된다