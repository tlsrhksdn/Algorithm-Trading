import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager,rc
from matplotlib import style

font_name=font_manager.FontProperties(fname="C:\Windows\Fonts\H2GTRE.TTF").get_name()
rc('font',family=font_name)
style.use('ggplot')


#pie차트를 그리는 데 필요한 데이터:범주와 각 범주가 데이터에서 차지하는 비율
labels=['삼성전자','SK하이닉스','LG전자','네이버','카카오']
ratio=[50,20,10,10,10]
#차트 색상을 설정하려면 각 범주에 해당하는 색상을 리스트 형태로 전달한다
colors=['gold','yellowgreen','lightcoral','lightskyblue','red']
#특정 pie를 확대하려면 각 범주에 확대 값을 리스트 형태로 전달한다
explode=(0.0,0.1,0.0,0.0,0.0)

#pie함수의 첫 번째 인자:각 범주가 데이터에서 차지하는 비율
#labels를 통해 범주를 전달,'shadow=True'를 통해 pie 차트에 그림자를 설정할 수 있다
#'startangle'=첫 번째 pie의 시작 각도
plt.pie(ratio, labels=labels, shadow=True, startangle=90)
plt.show()