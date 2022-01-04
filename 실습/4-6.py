# 화면을 분할하여 그래프 여러개 그리기 - axe 객체 

import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager,rc
font_path = "예제/part4/malgun.ttf" # 폰트 파일 위치 
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font_name)


df = pd.read_excel('예제/part4/시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)

# 누락값(NaN)을 앞 데이터로 채움 (엑셀 양식 병합 부분)
df = df.fillna(method='ffill') # 전출지별 열 

# 서울에서 다른 지역으로 전출하는 데이터만 추출
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]

df_seoul = df_seoul.drop(['전출지별'], axis= 1) # 전출지별의 열 삭제 
df_seoul.rename(columns ={'전입지별' : '전입지'}, inplace=True)
df_seoul.set_index('전입지', inplace = True)
# 경기도로 전출간 데이터 
sr_one =df_seoul.loc['경기도'] # 시리즈

plt.style.use('ggplot')
# 그래프 객체 생성
fig = plt.figure(figsize= (10,10)) # 그림틀 생성
ax1 = fig.add_subplot(2,1,1)  #add_subplot() : 그림틀 분할, (2,1,1) : 2행 1열로 분할 1번째 
ax2 = fig.add_subplot(2,1,2)

# axe 객체에 plot 함수로 그래프 출력
ax1.plot(sr_one, 'o', markersize =10) # 점 그래프

ax2.plot(sr_one, marker ='o', markersize =10, markerfacecolor = 'red',
         color ='olive', linewidth =2, label= '서울 -> 경기')
ax2.legend(loc='best')

# y축 범위 지정
ax1.set_ylim(50000,800000)
ax2.set_ylim(50000,800000)

# 축 눈금 라벨 지정 및 회전
ax1.set_xticklabels(sr_one.index, rotation = 75)
ax2.set_xticklabels(sr_one.index, rotation = 75)

plt.show()