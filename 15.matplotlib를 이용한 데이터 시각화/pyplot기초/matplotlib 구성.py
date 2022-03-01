#4.matplotlib 구성

#matploblib으로 그래프를 그리려면 Figure 객체와 하나 이상의 subplot(Axes)객체가 필요하다
#Axes 객체는 다시 두 개의 Axis 객체를 포함

# import matplotlib
# import matplotlib.pyplot as plt

# fig=plt.figure()

# type(fig)

# #빈 Figure 객체에 Axes 객체를 생성하려면 add_subplot 메서드를 사용한다
# #add_subplot(1,1,1)은 Figure 객체에 하나의 AxesSubplot 객체를 생성한다

# ax=fig.add_subplot(1,1,1)

# type(ax)


# #Figure 객체를 생성하고 해당 Figure 객체에 여러 개의 AxesSubplot 객체를 생성하는
# #두 가지 작업을 한번에 할 때는 plt.subplots를 사용한다

# fig,ax_list=plt.subplots(2,2)

# fig

# ax_list

#2x2 구조의 AxesSubplot 객체에 접근하려면 
#ax_list[0][0], ax_list[0][1], ax_list[1][0], ax_list[1][1]을 통해 각 행과 열에 위치에 존재하는 AxesSubplot 객체에 접근할 수 있습니다.
#ax_list[0][0]

#ax_list[0][0]이 바인딩하고 있는 왼쪽 상단의 AxesSuplot 객체에 그래프를 그린 후 그래프를 화면에 출력

# ax_list[0][0].plot([1,2,3,4])

# plt.show()