# import sys
# from PyQt5.QtWidgets import *

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

#위젯:사용자 인터페이스를 구성하는 가장 기본적인 부품 역할

# class MyWindow(QMainWindow): 
#     def __init__(self):
#         super().__init__()    #부모 클래스에 정의된 __init__()을 호출한다
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

# print('Child1',dir(child1))  #정의된 클래스의 인스턴스를 생성한 후 dir 내장함수를 이용해 객체의 속성값을 확인
# print('Child2',dir(child2))
        
        
# if __name__=="__main__":     
#     app=QApplication(sys.argv)
#     mywindow=MyWindow()
#     mywindow.show()
#     app.exec_()

# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyStock")
#         self.setGeometry(300,300,300,400)
        
#         btn1=QPushButton("Click me",self)
#         btn1.move(20,20)
#         btn1.clicked.connect(self.btn1_clicked)
        
#     def btn1_clicked(self):
#         QMessageBox.about(self,"message","clicked")
        
# if __name__ == "__main__":
#     app=QApplication(sys.argv)
#     myWindow=MyWindow()
#     myWindow.show()
#     app.exec_()


#Open API+ 로그인하기

# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QAxContainer import * #부합하는 파일 x  #16장 헤결법 참고

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyStock")
#         self.setGeometry(300,300,300,150)
        
#         self.kiwoom=QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
                
#         btn1=QPushButton("Login",self)
#         btn1.move(20,20)
#         btn1.clicked.connect(self.btn1_clicked)
        
#         btn2=QPushButton("Check state",self)
#         btn2.move(20,70)
#         btn2.clicked.connect(self.btn2_clicked)
        
#     def btn1_clicked(self):
#         ret=self.kiwoom.dynamicCall("CommConnect()") 
#         #OCX방식: QAxBase 클래스의 dynamicCall 매서드를 사용해 원하는 메서드를 호출
#         #CommConnect 매서드를 통해 키움증권 서버에 로그인을 시도
#     def btn2_clicked(self):
#         if self.kiwoom.dynamicCall("GetConnectState()")==0:
#             self.statusBar().showMessage("Not connected")
#         else:
#             self.statusBar().showMessage("Connected")
            
# if __name__=="__main__":
#     app=QApplication(sys.argv)
#     mywindow=MyWindow()
#     mywindow.show()
#     app.exec_()

# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QAxContainer import *

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyStock")
#         self.setGeometry(300,300,300,150)
        
#         self.kiwoom=QAxWidget("KHOPENAPI.KHOPENAPICtrl.1")
#         self.kiwoom.dynamicCall("CommConnect()")
        
#         self.text_edit=QTextEdit(self)
#         self.text_edit.setGeometry(10,60,200,80)   #QTextEdit 클래스의 크기 및 출력 위치를 조절
#         self.text_edit.setEnabled(False)   #QTextEdit 클래스의 읽기/쓰기 모드를 변경
        
#         self.kiwoom.OnEventConnect.connect(self.event_connect)

#         #OnEventConnect 이벤트를 처리해 로그인 성공 여부를 출력하는 프로그램
#     def event_connect(self,err_code):
#         if err_code==0:
#             self.text_edit.append("로그인 성공")
            
# if __name__=="__main__":
#     app=QApplication(sys.argv)
#     MyWindow=MyWindow()
#     MyWindow.show()
#     app.exec_()

#프로그램의 UI를 구성하는 코드

# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QAxContainer import *

# #예제에 사용된 PyQt 위젯
# # QLabel:간단한 텍스트 출력
# # QLineEdit:간단한 사용자 입력 처리
# # QPushButton:버튼 생성
# # QTextEdit:메시지 출력

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyStock")
#         self.setGeometry(300,300,300,150)
        
#         label=QLabel("종목코드 : ",self)
#         label.move(20,20)
        
#         self.code_edit=QLineEdit(self) #사용자로부터 종목 코드를 입력받는다
#         self.code_edit.move(80,20)
#         self.code_edit.setText("039490")
        
#         btn1=QPushButton("조회",self)
#         btn1.move(100,20)
        
#         self.text_edit=QTextEdit(self)    #로그인 처리 결과 혹은 Open API+ 결과를 출력
#         self.text_edit.setGeometry(10,60,280,80)
#         self.text_edit.setEnabled(False)
        
# if __name__=="__main__":
#     app=QApplication(sys.argv)
#     myWindow=MyWindow()
#     myWindow.show()
#     app.exec_()

#QLineEdit 위젯에 종목 코드를 입력한 후 [조회]버튼을 클릭하면
#입력된 종목 코드가 QTextEdit 위젯에 출력되도록 코드를 수정한다.

# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QAxContainer import *

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.kiwoom=QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
#         self.kiwoom.dynamicCall("CommConnect()")
#         self.kiwoom.OnEventConnect.connect(self.event_connect)

#         self.setWindowTitle("PyStock")
#         self.setGeometry(300, 300, 300, 150)

#         label = QLabel('종목코드: ', self)
#         label.move(20, 20)

#         self.code_edit = QLineEdit(self)
#         self.code_edit.move(80, 20)
#         self.code_edit.setText("039490")

#         btn1 = QPushButton("조회", self)
#         btn1.move(190, 20)
#         btn1.clicked.connect(self.btn1_clicked)

#         self.text_edit = QTextEdit(self)
#         self.text_edit.setGeometry(10, 60, 280, 80)
#         self.text_edit.setEnabled(False)

#     def event_connect(self, err_code):
#         if err_code == 0:
#             self.text_edit.append("로그인 성공")

#     def btn1_clicked(self):
#         code = self.code_edit.text()
#         self.text_edit.append("종목코드: " + code)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = MyWindow()
#     myWindow.show()
#     app.exec_()

#사용자에게서 입력받은 종목 코드와 Open API+가 제공하는 TR 메서드를 통해
#기본 정보를 가져오는 코드를 작성한다.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Kiwoom Login
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        # OpenAPI+ Event
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)

        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)

        label = QLabel('종목코드: ', self)
        label.move(20, 20)

        self.code_edit = QLineEdit(self)
        self.code_edit.move(80, 20)
        self.code_edit.setText("039490")

        btn1 = QPushButton("조회", self)
        btn1.move(190, 20)
        btn1.clicked.connect(self.btn1_clicked)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.setEnabled(False)

    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")

    def btn1_clicked(self):
        code = self.code_edit.text()
        self.text_edit.append("종목코드: " + code)

        # SetInputValue
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)

        # CommRqData
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")

    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        if rqname == "opt10001_req":
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")

            self.text_edit.append("종목명: " + name.strip())
            self.text_edit.append("거래량: " + volume.strip())
        
            #rqname값이 'opt10001_req'인지 확인
            #rqname이 'opt10001_req'이면 CommGetData 메서드를 호출해 '종목명'과 '거래량'에 해당하는 값을 가져온다
            #CommGetData 메서드를 호출해 '종목명'과 '거래량' 값을 가져왔다면->strip 메서드를 호출해 문자열의 공백을 제거하고,이후 QTexEdit 객체에 해당 문자열을 추가한다

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    

#OpenAPI+의 TR 처리 순서
# SetInputValue 메서드를 사용해 TR 입력 값을 설정한다
# CommRqData 메서드를 사용해 TR을 서버로 송신한다
# 서버로부터 이벤트가 발생할 때까지 이벤트 루프를 사용해 대기한다
# CommGetData 메서드를 사용해 수신 데이터를 가져온다