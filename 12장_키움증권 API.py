import sys
from PyQt5.QtWidgets import *

#12-01
# app=QApplication(sys.argv)
# label=QLabel("Hello PyQt")
# label.show()
# app.exec_()

#12-02
# app=QApplication(sys.argv)
# label=QPushButton("Quit")
# label.show()
# app.exec_()

#12-03
# app=QApplication(sys.argv)
# print(sys.argv)
# label=QLabel("Hello PyQt")
# label.show()
# app.exec_()

#12-04.QMainWindow를 이용한 윈도우 생성

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyStock")        #윈도우의 타이틀 창의 택스트를 바꾸는 메서드
#         self.setGeometry(300,300,300,400)     #창의 위치 및 크기를 조절하는 메서드

# class Parent:
#     house="yong-san"
#     def __init__(self):
#         self.money=10000
        
# class Child1(Parent):
#     def __init__(self):
#         super().__init__()  #부모 클래스의 생성자를 명시적으로 호출
#         pass
    
# class Child2(Parent):
#     def __init__(self):
#         pass

# child1=Child1()
# child2=Child2()

# print('Child1',dir(child1))
# print('Child2',dir(child2))
        
        
# if __name__=="__main__":
#     app=QApplication(sys.argv)
#     mywindow=MyWindow()
#     mywindow.show()
#     app.exec_()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300,300,300,400)
        
        btn1=QPushButton("Click me",self)
        btn1.move(20,20)
        btn1.clicked.connect(self.btn1_clicked)
        
    def btn1_clicked(self):
        QMessageBox.about(self,"message","clicked")
        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    myWindow=MyWindow()
    myWindow.show()
    app.exec_()