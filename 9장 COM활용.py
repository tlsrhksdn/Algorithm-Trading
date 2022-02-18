class CpStockCode:
    def __init__(self):
        self.stocks={'유한양행':'A000100'}
    #주식 종목수를 반환
    def GetCount(self):
        return len(self.stocks)
    #종목명을 입력하면 해당 종목에 대한 종목 코드를 반환
    def NameToCode(self,name):
        return self.stocks[name]

InstCpStockCode=CpStockCode()
print(InstCpStockCode.GetCount())
print(InstCpStockCode.NameToCode('유한양행'))

import win32com.client

#엑셀값입력.저장
excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
wb=excel.Workbooks.Add()
ws=wb.Worksheets("Sheet1")
ws.Cells(1,1).Value="hello world"
wb.SaveAs("C:/Users/신관우/OneDrive/바탕 화면/test.xlsx")
excel.Quit()