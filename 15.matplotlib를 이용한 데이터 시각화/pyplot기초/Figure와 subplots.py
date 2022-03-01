#sin과 cosine 그래프 그려보기

# import numpy as np
# import matplotlib.pyplot as plt

# x=np.arange(0.0,2*np.pi,0.1)
# #x값이 실수 범위이므로 range를 사용할 수 없고 대신 numpy 모듈의 arange를 사용한다
# #numpy모듈을 먼저 임포트한 후 arange함수를 호출해서 0~2pi사이에서 0.1 간격으로 x값을 만든다.
# sin_y=np.sin(x)
# cos_y=np.cos(x)

# fig=plt.figure()
# ax1=fig.add_subplot(2,1,1)
# ax2=fig.add_subplot(2,1,2)

# ax1.plot(x,sin_y,'b--')
# ax2.plot(x,cos_y,'r--')

# plt.show()