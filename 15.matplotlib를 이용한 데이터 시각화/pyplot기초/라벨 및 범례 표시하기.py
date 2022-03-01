#sine과 cosine 그래프-2

#  import numpy as np
#  import matplotlib.pyplot as plt
 
#  x=np.arange(0.0,2*np.pi,0.1)
#  sin_y=np.sin(x)
#  cos_y=np.cos(x)
 
#  fig=plt.figure()
#  ax1=fig.add_subplot(211)
#  ax2=fig.add_subplot(212)
 
#  ax1.plot(x,sin_y,'b--')
#  ax2.plot(x,cos_y,'r--')
 
#  ax1.set_xlabel('x')
#  ax1.set_ylabel('sin(x)')
 
#  ax2.set_xlabel('x')
#  ax2.set_ylabel('cos(x)')
 
#  plt.show()


# import pandas_datareader.data as web

# lg=web.DataReader('066570.KS','yahoo')
# samsung=web.DataReader('005930.KS','yahoo')

# import matplotlib.pyplot as plt
# plt.plot(lg.index,lg['Adj Close'],label='LG Electronics')
# #label이라는 인자를 통해 라벨을 지정
# #label을 통해 전달된 문자열이 범례에 표시된다

# plt.legend(loc='upper left')
# #범례는 legend 함수를 통해 추가할 수 있다
# #loc라는 함수 인자를 통해 범례가 표시되는 위치를 지정할 수 있다
#범례의 위치는 'location string'을 입력하거나 'location string'에 대응되는 'location code'를 사용해도 된다
#범례 표시 위치를 직접 지정하지 않고 'best'옵션을 사용하면 그래프를 가리지 않도록 적절한 위치에 범례를 자동으로 표시한다

# plt.show()