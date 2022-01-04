import pandas as pd
import matplotlib.pyplot as plt
# matplotlib 
# 선그래프 plt.plot
df = pd.read_excel('예제/part4/시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)

# 누락값(NaN)을 앞 데이터로 채움 (엑셀 양식 병합 부분)
df = df.fillna(method='ffill') # 전출지별 열 

print(df.head())

# 서울에서 다른 지역으로 전출하는 데이터만 추출
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
print(df_seoul.head())
print('------------------------------------------')
df_seoul = df_seoul.drop(['전출지별'], axis= 1) # 전출지별의 열 삭제 
df_seoul.rename(columns ={'전입지별' : '전입지'}, inplace=True)
df_seoul.set_index('전입지', inplace = True)

print(df_seoul.head(8))
print('------------------------------------------')

# 경기도로 전출간 데이터 선택
sr_one =df_seoul.loc['경기도'] # 시리즈
print(sr_one.head())
# 선 그래프 ㄱ 
plt.plot(sr_one)
# plt.plot(sr_one.index , sr_one.values)
plt.show()

# 제목 및 축 이름 추가 
plt.plot(sr_one)
plt.title('서울 -> 경기도 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.show()
# 한글이 깨짐 & x축 눈금 라벨 겹침