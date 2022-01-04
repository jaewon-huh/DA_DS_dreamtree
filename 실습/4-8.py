# 동일한 그림에 여러 그래프 추가 

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

# 서울에서 충청 ,경상, 강원도로 이동한 인구 데이터 값만 선택 
# 1970~ 2017의 str 리스트 생성
# map(함수, 리스트) : 리스트의 요소를 함수에 넣고 리턴 값으로 새 리스트 , 출력값 이터레이터 list() 출력
col_years = list(map(str, range(1970,2018)))
df_3 = df_seoul.loc[['충청남도','경상북도','강원도'], col_years]
print(df_3.head())
plt.style.use('ggplot') # 스타일 서식 지정 

# 그래프 객체 생성
fig = plt.figure(figsize =(20,5))
ax = fig.add_subplot(1,1,1)

# axe 객체에 plot 함수로 그래프 출력
ax.plot(col_years, df_3.loc['충청남도',:],
        marker ='o', markerfacecolor ='green' , markersize = 10,
        color ='olive', linewidth = 2, label ='서울 -> 충남')
ax.plot(col_years, df_3.loc['경상북도',:],
        marker ='o', markerfacecolor ='blue' , markersize = 10,
        color ='skyblue', linewidth = 2, label ='서울 -> 경북') 
ax.plot(col_years, df_3.loc['강원도',:],
        marker ='o', markerfacecolor ='red' , markersize = 10,
        color ='magenta', linewidth = 2, label ='서울 -> 강원')   

ax.legend(loc ='best') 

# 차트 이름 및 축
ax.set_title('서울 -> 충남, 경북, 강원 인구 이동', size=20)


ax.set_xlabel('기간', size=12)
ax.set_ylabel('이동 인구수', size = 12)


ax.set_xticklabels(col_years, rotation=90)

ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)

plt.show()  # 변경사항 저장하고 그래프 출력
