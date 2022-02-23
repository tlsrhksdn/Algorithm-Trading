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