# axe 객체 그래프 꾸미기 

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
# 그래프 객체 생성 한개만 
fig = plt.figure(figsize= (20,5)) # 그림틀 생성
ax = fig.add_subplot(1,1,1)  # 한개의 서브 플롯

# plot 함수로 그래프 출력
ax.plot(sr_one, marker ='o', markerfacecolor ='orange', markersize =10,
        color = 'olive', linewidth =2 , label = '서울 -> 경기')
ax.legend(loc='best')
ax.set_ylim(50000,800000)

# 제목 및 축 이름 추가 
ax.set_title('서울 -> 경기 인구 이동', size=20)

ax.set_xlabel('기간', size=12)
ax.set_ylabel('이동 인구수', size = 12)

ax.set_xticklabels(sr_one.index, rotation=75)

# 축 눈금 라벨 크기
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)

plt.show()  