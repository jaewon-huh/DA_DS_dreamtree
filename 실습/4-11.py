# 막대그래프 barplot : plot(kind = 'bar')
# 세로형 막대 : 시계열 데이터의 차이 비교 적절 

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
# 2010~ 2017의 str 리스트 생성
# map(함수, 리스트) : 리스트의 요소를 함수에 넣고 리턴 값으로 새 리스트 , 출력값 이터레이터 list() 출력
col_years = list(map(str, range(2010,2018)))
df_4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'], col_years]
df_4 = df_4.T  # 행렬 전치 

plt.style.use('ggplot')

df_4.index = df_4.index.map(int) # 년도를 정수형으로 바꿈 
print(df_4.head())
# 막대그래프 그리기 
df_4.plot(kind='bar', figsize= (20,10), width = 0.7,
         color = ['red', 'orange', 'green', 'blue'])

plt.title('서울 -> 타시도 인구 이동', size =30)
plt.ylabel('이동 인구수', size = 20)
plt.xlabel('기간', size= 20)
plt.ylim(5000,30000)
plt.legend(loc ='best', fontsize =10)

plt.show()

