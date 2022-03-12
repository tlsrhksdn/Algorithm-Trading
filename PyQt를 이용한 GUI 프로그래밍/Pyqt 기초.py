#pyQt는 매우 복잡하고 규모가 큰 라이브러리
#PyQt를 모두 다룰수는 없으며,알고리즘 트레이딩 프로그램 UI를 만들 수 있을 만큼만 정리

#화면에 출력되는 UI부문
#PyQt가 기본적으로 제공하는 위젯 클래스의 객체를 생성해서 만들 수 있다

#이벤트 루프
#QApplication 객체에서 exec_ 메서드를 호출해 이벤트 루프를 생성한다

#이벤트를 처리할 함수 또는 메서드를 구현
#버튼과 같은 위젯을 클릭하면 해당 위젯은 'clicked'라는 시그널을 발생시킨다
#'clicked'라는 시그널이 발생했을 때 호출되는 함수 또는 메서드를 구현해야 함

#특정 시그널이 발생했을 때 호출되는 함수 또는 메서드를 슬롯이라고 한다
#PyQy에서는 위젯에서 발생하는 시그널에 대해 어떤 슬롯으로 처리할지에 대해 미리 등록함으로써
#특정 위젯에서 시그널이 발생했을 때 이벤트 루프가 미리 연결된 슬롯을 자동으로 호출하게 되어 있다

#PyQt의 UI-시그널-슬롯-이벤트 루프의 관계
# import sys
# from PyQt5.QtWidgets import *

# def clicked_slot():
#     print('clicked')

# app=QApplication(sys.argv)

# label=QLabel("Hello,PyQt")
# label.show()

# print("Before event loop")
# app.exec_()
# print("After event loop")

# import sys
# from PyQt5.QtWidgets import *

# class MyWindow(QMainWindow):  #QMainWindow 클래스를 상속받고 있다
#     def __init__(self):
#         super().__init__()
#         self.setupUI()   #자기자신의 UI를 변경하는 메서드인 setupUI를 호출

#     def setupUI(self):
#         self.setWindowTitle("Review")

#         btn1 = QPushButton("Click me", self)
#         btn1.move(20, 20)
#         btn1.clicked.connect(self.btn1_clicked)

#     def btn1_clicked(self):
#         QMessageBox.about(self, "message", "clicked")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mywindow = MyWindow()
#     mywindow.show()
#     app.exec_()



