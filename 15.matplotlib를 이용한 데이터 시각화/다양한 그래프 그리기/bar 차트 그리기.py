# import matplotlib.pyplot as plt
# import numpy as np  
# from matplotlib import font_manager,rc  #그래프를 그릴 때 한글 폰트를 설정하는 데 사용

# font_name=font_manager.FontProperties(fname="C:\Windows\Fonts\H2GTRE.TTF").get_name()
# #폰트 파일이 설치된 상세 경로:C:\Windows\Font
# #파일 경로는 백슬래시로 표현
# rc('font',family=font_name)

# #bar차트는 수직,수평 모두 그릴 수 있다

# industry=['통신업','의료정밀','운수창고업','의약품','음식료품','전긱가스업','서비스업','전기전자','종이목재','증권']
# fluctuations=[1.83,1.30,1.30,1.26,1.06,0.93,0.77,0.68,0.65,0.61]

# fig=plt.figure(figsize=(12,8))
# ax=fig.add_subplot(111)

# #수평 방향의 bar차트: matplotlib.pyplot 모듈의 barh 함수를 사용해 그릴 수 있다
# #barh 함수의 첫 번째 인자는 각 bar가 그려질 위치이고, 두 번째 인자는 각 bar에 대한 수치이다
# #align은 bar 차트에서 bar의 정렬 위치를 설정하고 height는 수평 bar 차트의 높이를 설정한다

# #수평 방향의 bar 차트에서는 y축에 ticker를 표시한다
# ypos = np.arange(10)
# rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
# plt.yticks(ypos, industry)

# #각 수치의 의미를 알려주기 위해 label을 설정한 후 마지막으로 그래프를 화면에 출력한다
# plt.xlabel('등락률')
# plt.show()

# #스타일을 변경하려면 matplotlib.style이라는 모듈을 임포트한 후 style을 설정한다
# from matplotlib import style
# style.use('ggplot')
    
# # 전체 코드
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import font_manager, rc
# from matplotlib import style

# font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
# rc('font', family=font_name)
# style.use('ggplot')

# industry = ['통신업', '의료정밀', '운수창고업', '의약품', '음식료품', '전기가스업', '서비스업', '전기전자', '종이목재', '증권']
# fluctuations = [1.83, 1.30, 1.30, 1.26, 1.06, 0.93, 0.77, 0.68, 0.65, 0.61]

# fig = plt.figure(figsize=(12, 8))
# ax = fig.add_subplot(111)

# ypos = np.arange(10)
# rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
# plt.yticks(ypos, industry)

# # bar 차트의 각 bar에 등락률 데이터를 출력
# # text함수의 인자:text가 출력되는 x축 위치,text가 출력되는 y축 위치,실제로 표시된 값
# # ha:수평 방향으로의 정렬,va:수직 방향으로의 정렬

# for i, rect in enumerate(rects):
#     ax.text(0.95 * rect.get_width(), rect.get_y() + rect.get_height() / 2.0, str(fluctuations[i]) + '%', ha='right', va='center')

# # 첫 번째 인자의 rect:bar 차트에서 각 bar에 해당한다.
# # 각 bar의 너비(길이)를 알아낸 후 그 너비의 95% 지점이 텍스트가 출력될 x축 위치가 된다
# # 두 번째 인자: 먼저 bar가 출력된 y축 위치를 rect.get_y를 통해 얻은 후 bar 높이의 절반을 더함으로써 y축 위치를 계산한다

# plt.xlabel('등락률')
# plt.show()