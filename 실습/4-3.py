# 그래프 스타일 서식 지정 
# plt.style.use('ggplot')  -> 다른 파일에도 계속 적용됨 

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

# 스타일 서식 지정
plt.style.use('ggplot')
plt.figure(figsize=(14,5)) # 가로 사이즈 확대 (14인치, 5인치)
plt.xticks(rotation ='vertical', size =10) # x축 눈금 라벨을 수직으로 


# 선그래프  
plt.plot(sr_one, marker ='o' , markersize =10) # 마커 표시

plt.title('서울 -> 경기도 이동')
plt.xlabel('기간', size =20)
plt.ylabel('이동 인구수', size = 20)
plt.legend(labels =['서울 -> 경기'], loc ='best', fontsize = 15) # loc = location 위치 
plt.show()


