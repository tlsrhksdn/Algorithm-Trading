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

