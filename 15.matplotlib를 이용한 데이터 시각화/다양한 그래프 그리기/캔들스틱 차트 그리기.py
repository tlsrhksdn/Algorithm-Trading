# import pandas_datareader.data as web
# import datetime
# start=datetime.datetime(2016,3,1)
# end=datetime.datetime(2016,3,31)
# skhynix=web.DataReader("000660.KS","yahoo",start,end)

# skhynix.head()


# import pandas_datareader.data as web
# import datetime
# import matplotlib.pyplot as plt
# import mpl_finance
# # import matplotlib.finance as matfin (matplotlib.finance 모듈이 mpl_finance로 교채)
# #참고 https://github.com/matplotlib/mplfinance#usage

# start = datetime.datetime(2010, 3, 1)
# end = datetime.datetime(2022, 3, 1)
# skhynix = web.DataReader("000660.KS", "yahoo", start, end)
# skhynix = skhynix[skhynix['Volume'] > 0]

# fig = plt.figure(figsize=(12, 8))
# ax = fig.add_subplot(111)

# mpl_finance.candlestick2_ohlc(ax, skhynix['Open'], skhynix['High'], skhynix['Low'], skhynix['Close'], width=0.5, colorup='r', colordown='b')
# #width:봉의 몸통의 넓이를 조절하는 파라미터
# #colorup:양봉을 표현하는 색상,colordown:음봉을 표현하는 색상을 지정하는 데 사용한 파라미터
# plt.show()

#그래프의 x축에 정수 인덱스가 아닌 날짜가 출력되도록 변경한다
from sqlite3 import Timestamp
import pandas_datareader.data as web

import datetime

start = datetime.datetime(2016, 3, 1)

end = datetime.datetime(2016, 3, 31)

skhynix = web.DataReader("000660.KS", "yahoo", start, end)

skhynix.index

# skhynix.index[0]은 '2016-03-01 00:00:00'을 의미한다
# 객체 타입은 pandas의 Timestamp이다.
# Timestamp 객체의 그래프의 x축에 출력하기에는 공간이 부족
#출력에 필요한 최소 부분만 뽑아내는 작업이 필요하다

#Pandas의 Timestamp 객체는 strftimee 메서드에 출력 포멧을 전달해서 문자열로 변환할 수 있다

#연도,월,시간 등은 제외하고 '일자'만 문자열로 만들어서 x축에 출력

#name_list라는 비어있는 리스트를 만들고, 
#반복문을 사용해 각 날짜에서 ‘일자’만 문자열로 변환한 후 변환된 문자열을 리스트에 추가합니다.

# name_list = []

# for day in skhynix.index:
#     name_list.append(day.strftime('%d'))
    
# name_list
