#DataFrame:여러 개의 칼럼으로 구성된 2차원 형태의 자료구조

#DataFrame 객체를 사용하는 가장 쉬운 방법: 파이썬의 딕셔너리를 사용한다

#딕셔너리를 통해 각 칼럼에 대한 데이터를 저장한 후
#딕셔너리를 DataFrame 클래스의 생성자 인자로 넘겨주면  DataFrame 객체가 생성된다


from pandas import Series, DataFrame

raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)
print(data)

#DataFrame에 있는 각 칼럼은 Series 객체임을 알 수 있다.
#즉,DataFrame을 인덱스가 같은 여러 개의 Series 객체로 구성된 자료구조로 생각해도 무방하다.

from pandas import Series, DataFrame

daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

daeshin_day = DataFrame(daeshin)
print(daeshin_day)

#DataFrame 객체에서 칼럼의 순서: DataFrame 객체를 생성할 때 columns라는 키워드를 지정할 수 있다
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'])

#DataFrame에서 인덱스 역시 DataFrame 객체를 생성하는 시점에 지정 가능
#먼저 인덱싱에 사용할 값을 만든 후 이를 DataFrame 객체 생성 시점에 지정한다
date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)

#DataFrame 객체의 종가 칼럼은 'close'를 사용해 접근할 수 있다
close = daeshin_day['close']
print(close)

#DataFrame 객체의 로우에 접근하려면 loc 메서드를 사용해 인덱스 값을 넘겨준다
day_data = daeshin_day.loc['16.02.24']
print(day_data)
print(type(day_data))

#DataFrame 객체의 칼럼 이름과 인덱스 값을 확인하려면 각각 columns와 index 속성을 사용하면 됩니다.

print(daeshin_day.columns)
print(daeshin_day.index)

# Index(['open', 'high', 'low', 'close'], dtype='object')
# Index(['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23'], dtype='object')