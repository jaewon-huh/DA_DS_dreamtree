# 범주형 변수 더미변수 변환 , 원핫인코딩 (0/1)
# sklearn 라이브러리 이용 
import pandas as pd
import numpy as np

# UCL 자동차 연비 데이터 셋
df = pd.read_csv('예제/part5/auto-mpg.csv', header= None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 

# horsepower 열 데이터 : 마력 
df['horsepower'].replace('?' , np.nan , inplace = True)
df.dropna(subset = ['horsepower'], axis = 0, inplace =True)
df['horsepower'] = df['horsepower'].astype('float') # 실수형으로 변환

# horsepower을 저출력 / 중출력 / 고출력으로 구분 -> 4개의 경계값 필요 
# np.histogram() 
count, bin_dividers = np.histogram(df['horsepower'], bins=3) # bins - 구간 개수
# count = 각 구간에 속하는 값 개수 / bin_dividers = 경계 값 
print(bin_dividers)
print('\n')

bin_names = ['저출력', '보통출력', '고출력']
# pd.cut() 함수로 각 데이터를 3개의 bin에 할당 
df['hp_bin'] = pd.cut(x= df['horsepower'],   # 데이터 : 1차원
                      bins =bin_dividers,    # 구간을 나눌 기준 : 리스트
                      labels= bin_names,     # 구간에 대해 레이블을 명시
                      include_lowest= True)  # 첫 경계값을 포함한다
            
# sklern 라이브러리 불러오기
from sklearn import preprocessing    

# 전처리를 위한 encoder 객체 만들기
label_encoder = preprocessing.LabelEncoder()       # label encoder 생성
onehot_encoder = preprocessing.OneHotEncoder()   # one hot encoder 생성

# label encoder로 문자열 범주를 숫자형 범주로 변환
onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15))  
print(onehot_labeled) # 1차원 벡터
print(type(onehot_labeled))

# 2차원 행렬로 형태 변경
onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled), 1) 
print(onehot_reshaped) # 2차원 행렬
print(type(onehot_reshaped))

# 희소행렬로 변환 : (행,열) 좌표 & 값 
onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted) 
print(type(onehot_fitted))



