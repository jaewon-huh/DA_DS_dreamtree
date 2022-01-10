# 분류 알고리즘 : 스팸메일 필터링 , 고객 분류 , 질병 진단 ...
# 목표 변수(종속)가 갖고있는 카테고리 값 중 하나로 분류 (0,1) 
# KNN : k-nearest-Neighbors  : k개의 이웃을 찾고 분류값


# titanic 데이터 -> 탑승객의 생존여부 예측 (survived = 1 / 0)

import pandas as pd
import seaborn as sns

'''
Step 1 데이터 준비
'''
df = sns.load_dataset('titanic')
print(df.head())

'''
Step 2 전처리
'''
print(df.info())
# age / embarked / deck 열의 누락데이터 존재 
# deck과 embarked_town 열 삭제 
rdf = df.drop(['deck', 'embark_town'], axis =1)
print(rdf.columns.values)
# age열 누락 데이터 승객 삭제 (행)
rdf = rdf.dropna(subset = ['age'], how ='any', axis = 0)
print(len(rdf),'\n')
# embarked의 누락데이터는 가장 많은 도시명으로 치환 
most_freq = rdf['embarked'].value_counts(dropna =True).idxmax()
print(most_freq, '\n')
rdf['embarked'].fillna(most_freq, inplace =True)

'''
Step 3 - 분석에 사용할 속성 선택
'''
ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
print(ndf.head())   
print('\n')

# sex , embarked 열의 범주형 데이터를 숫자형으로 변환 (더미변수- 원핫인코딩)
onehot_sex = pd.get_dummies(ndf['sex'])
# 변수 연결
ndf = pd.concat([ndf,onehot_sex], axis =1)
onehot_embarked = pd.get_dummies(ndf['embarked'], prefix ='town') # 접두어 붙이기
ndf =pd.concat([ndf, onehot_embarked], axis =1)

ndf.drop(['sex', 'embarked'], axis = 1 , inplace = True)
print(ndf.head())

'''
Step 4 - 훈련/검증 데이터 분할
'''
# 독립(설명) 종속(예측변수) 지정 
X=ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male', 
       'town_C', 'town_Q', 'town_S']]  #독립 변수 X
y=ndf['survived']                      #종속 변수 Y

# 설명 변수 데이터를 정규화 
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

# train_data와  test data로 구분 (7:3)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,               #독립 변수 
                                                    y,               #종속 변수
                                                    test_size=0.3,   #검증 30%
                                                    random_state=10) #랜덤 추출 값 : 무작위 섞기를 고정함.

print('train data 개수 :', X_train.shape)
print('test data 개수 :', X_test.shape)

'''
Step 5 - 모형 학습 및 검증 
'''

# Sklearn 라이브러리에서 KNN 분류 모형 
from sklearn.neighbors import KNeighborsClassifier

# 모형 객체 생성
knn = KNeighborsClassifier(n_neighbors= 5)  # 이웃의 숫자 5

# train data를 가지고 학습 
knn.fit(X_train, y_train)

# test data를 가지고 y_hat을 예측
y_hat = knn.predict(X_test)
# 비교 
print(y_hat[0:10])
print(y_test.values[0:10], '\n')

# 모형의  예측능력을 평가 : metrics 모듈의 confusion_matrix()
from sklearn import metrics
knn_matrix = metrics.confusion_matrix(y_test, y_hat)
print(knn_matrix)
# 215 승객 중 TP : 110 , FP :15 , FN :26 , FF : 64 

# 모형 성능평가 - 평가 지표 계산 : metrics 모듈 classification_report()
knn_report = metrics.classification_report(y_test,y_hat)
print(knn_report)
# f1-score : 0- 0.84  미생존자 예측의 정확도 0.84 , 1 -0.76 생존자 예측 정확도 0.76