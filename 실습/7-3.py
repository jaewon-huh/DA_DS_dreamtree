# 다중회귀분석 : 여러개의 독립변수가 종속변수에 영향 & 선형관계 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

'''
[Step 1] 데이터 준비 - read_csv() 함수로 자동차 연비 데이터셋 가져오기
'''
# CSV 파일을 데이터프레임으로 변환
df = pd.read_csv('예제/part7/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 

'''
[Step 2] 데이터 탐색
'''


df['horsepower'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)   # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')      # 문자열을 실수형으로 변환

# 분석에 활용할 열 선택 
ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]

# 속성(변수) 선택
X=ndf[['cylinders', 'horsepower', 'weight']]  #독립 변수 X : x1 ,x2, x3
y=ndf['mpg']       #종속 변수 Y

# train data 와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,               #독립 변수 
                                                    y,               #종속 변수
                                                    test_size=0.3,   #검증 30%
                                                    random_state=10) #랜덤 추출 값 : 무작위 섞기를 고정함.

print('훈련데이터 : ', X_train.shape)
print('검증데이터 : ', X_test.shape)

'''
Step 5: 단순회귀분석 모형 - sklearn 사용
'''

# sklearn 라이브러리에서 선형회귀분석 모듈 가져오기
from sklearn.linear_model import LinearRegression

# 단순회귀분석 모형 객체 생성
lr = LinearRegression()   

# train data를 가지고 모형 학습
lr.fit(X_train, y_train)

# 결정계수 : 검증 데이터를 score() a메소드에 전달 
r_square = lr.score(X_test, y_test)
print(r_square)
print('\n')

# 회귀식의 기울기 coefficients
print('X 변수의 계수 a: ', lr.coef_)
print('\n')

# 회귀식의 y절편  
print('상수항 b', lr.intercept_)
print('\n')

# Y = -0.6 X1 + -0.03 X2 + -0.005 X3 + 46.414

# 모형 예측결과y_hat 과 실제값 비교 y_test
y_hat = lr.predict(X_test)  

# 커널 밀도추정 
plt.figure(figsize=(10, 5))
ax1 = sns.kdeplot(y_test, label="y_test")
ax2 = sns.kdeplot(y_hat, label="y_hat", ax=ax1) # 그래프 겹쳐 
plt.legend()
plt.show()
# -> 단순회귀분석 결과외 비교할때 편향은 그대로, 첨도가 누그러짐 