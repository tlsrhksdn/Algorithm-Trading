#로그인 여부 자동 확인

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