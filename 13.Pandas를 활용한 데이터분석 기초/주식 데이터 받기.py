#jupyter QtConsole 활용해 실습

#DataReader 함수:웹 상의 데이터를 DataFrame 객체로 만드는 기능 제공

#첫 번째 인자: 조회할 종목, 두 번째 인자: 데이터를 가져올 소스(야후)에 대한 정보, 세 번째와 네 번째 인자: 조회 기간의 시작일과 종료일을 입력

#DataFrame 객체에서 info 메서드를 호출하면 DataFrame 객체를 요약해서 볼 수 있다

#Pandas를 이용한 주가이동평균 계산



#주가이동평균선 그리기
#범례를 표시하기 위해 legend 함수를 호출
#loc 인자를 통해 범례 표시 위치를 지정할 수 있다
#범례가 적절한 위치에 자동으로 출력되게 하려면 loc='best'옵션을 사용하면 된다
#그래프 값을 좀 더 편리하게 확인하기 위한 격자 (grid)를 표시하려면 grid 함수를 호출한다.
#그래프 출력을 위한 함수 호출을 완료했다면 show 함수를 호출해 화면에 그래프를 출력해 본다

#수정 종가 및 주가이동평균선(5,20,60,120일)을 그래프로 출력하는 전체 코드
# import pandas as pd
# import pandas_datareader.data as web
# import matplotlib.pyplot as plt

# # Get GS Data from Yahoo
# gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
# new_gs = gs[gs['Volume']!=0]

# # Moving average
# ma5 = new_gs['Adj Close'].rolling(window=5).mean()
# ma20 = new_gs['Adj Close'].rolling(window=20).mean()
# ma60 = new_gs['Adj Close'].rolling(window=60).mean()
# ma120 = new_gs['Adj Close'].rolling(window=120).mean()

# # Insert columns
# new_gs.insert(len(new_gs.columns), "MA5", ma5)
# new_gs.insert(len(new_gs.columns), "MA20", ma20)
# new_gs.insert(len(new_gs.columns), "MA60", ma60)
# new_gs.insert(len(new_gs.columns), "MA120", ma120)

# # Plot
# plt.plot(new_gs.index, new_gs['Adj Close'], label='Adj Close')
# plt.plot(new_gs.index, new_gs['MA5'], label='MA5')
# plt.plot(new_gs.index, new_gs['MA20'], label='MA20')
# plt.plot(new_gs.index, new_gs['MA60'], label='MA60')
# plt.plot(new_gs.index, new_gs['MA120'], label='MA120')

# plt.legend(loc="best")
# plt.grid()
# plt.show()