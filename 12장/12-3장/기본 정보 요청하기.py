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
#로그인 이벤트 처리도 추가

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
