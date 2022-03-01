


 

  


import matplotlib.pyplot as plt
import pandas_datareader.data as web

sk_hynix=web.DataReader("000660.KS","yahoo")

fig=plt.figure(figsize=(12,8))  #figsize라는 인자를 통해 Figure 객체의 크기를 조정

top_axes = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)  #subplot의 위치나 크기를 조절
bottom_axes = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)
#거래량 값으로서 큰 값이 발생할 때 그 값을 오일러 상수의 지수 형태로 표현되지 않게 해 준다
bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)

top_axes.plot(sk_hynix.index, sk_hynix['Adj Close'], label='Adjusted Close')  #수정 종가 그래프
bottom_axes.plot(sk_hynix.index, sk_hynix['Volume'])  #거래량

#subplot들이 Figure 객체의 영역 내에서 자동으로 최대 크기로 출력되게 해준다
plt.tight_layout()
plt.show()