# 다항 회귀분석 : Y = aX^2 + bX +c 
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
X=ndf[['weight']]  #독립 변수 X
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
Step 5: 비선형회귀분석 모형 - sklearn 사용
'''

# sklearn 라이브러리에서 선형회귀분석 모듈 가져오기
from sklearn.linear_model import LinearRegression     # 선형회귀분석
from sklearn.preprocessing import PolynomialFeatures  # 다항식 변환

# 다항식 변환
poly = PolynomialFeatures(degree= 2)                #2차항 적용
X_train_poly = poly.fit_transform(X_train)          #X_train 데이터를 2차항으로 변형

print('원 데이터 : ', X_train.shape)
print('2차항 변환 데이터 :', X_train_poly.shape)
# X_train_poly 열이 3개로 증가함

# train data를 가지고 모형 학습
pr = LinearRegression()         # 회귀분석 모형 객체 생성
pr.fit(X_train_poly, y_train)   # 학습

# 학습을 마친 모형에 test data를 적용하여 결정계수(R-제곱) 계산
X_test_poly = poly.fit_transform(X_test)  # 검증 데이터역시 poly 객체로 2차항 변환  
r_square = pr.score(X_test_poly, y_test)  # score(x,y) : 결정계수 구하는 함수 
print(r_square)   # R제곱 : 설명력 (더 높아짐)
print('\n')

# train data의 산점도와 test data로 예측한 회귀선을 그래프로 출력
y_hat_test = pr.predict(X_test_poly)

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
ax.plot(X_train, y_train, 'o', label = 'Train Data')              # 데이터 분포
ax.plot(X_test, y_hat_test, 'r+', label = 'Predict Value')        # 모형이 학습한 회귀선 
ax.legend(loc ='best')
plt.xlabel('weight')
plt.ylabel('mpg')

plt.show()
plt.close()

#  모형이 예측한 결과(y_hat)와 실제 값(y) 비교 
X_poly = poly.fit_transform(X)   # 전체 X데이터를 2차항으로 변환
y_hat = pr.predict(X_poly)       # predict 메소드 전달

# 커널 밀도 추정 
plt.figure(figsize= (10,5))
ax1 = sns.kdeplot(y, label = "y")
ax2 = sns.kdeplot(y_hat, label = "y_hat", ax =ax1)
plt.show()       # 더 적합한 모형
plt.close() 