# SVM : Support Vector Machine
# 같은 분류 값을 갖는 데이터 끼리 같은 공간에 위치하도록 벡터공간을 분리 

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

# age / embarked / deck 열의 누락데이터 존재 
# deck과 embarked_town 열 삭제 
rdf = df.drop(['deck', 'embark_town'], axis =1)

# age열 누락 데이터 승객 삭제 (행)
rdf = rdf.dropna(subset = ['age'], how ='any', axis = 0)

# embarked의 누락데이터는 가장 많은 도시명으로 치환 
most_freq = rdf['embarked'].value_counts(dropna =True).idxmax()

rdf['embarked'].fillna(most_freq, inplace =True)

'''
Step 3 - 분석에 사용할 속성 선택
'''
ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]

# sex , embarked 열의 범주형 데이터를 숫자형으로 변환 (더미변수- 원핫인코딩)
onehot_sex = pd.get_dummies(ndf['sex'])
# 변수 연결
ndf = pd.concat([ndf,onehot_sex], axis =1)
onehot_embarked = pd.get_dummies(ndf['embarked'], prefix ='town') # 접두어 붙이기
ndf =pd.concat([ndf, onehot_embarked], axis =1)

ndf.drop(['sex', 'embarked'], axis = 1 , inplace = True)

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
Step 5 - SVM 분류 모형 
'''
from sklearn import svm
# 모형 객체 생성 (kernal = 'rbf' : 커널 함수,데이터를 벡터공간으로 매핑 RBF)
svm_model = svm.SVC(kernel='rbf')
# 훈련데이터 학습
svm_model.fit(X_train,y_train)
# 검증 데이터 예측 y_hat
y_hat = svm_model.predict(X_test)

# 모형 예측값과 실제 데이터 비교 
print(y_hat[0:10])
print(y_test.values[0:10], '\n')  # 10 중 8 일치 

# 모형 성능 평가 - confusion_matrix()
from sklearn import metrics
svm_matrix = metrics.confusion_matrix(y_test, y_hat)
print(svm_matrix, '\n')
# 모형 성능 평가 - 평가지표 계산
svm_report = metrics.classification_report(y_test,y_hat)
print(svm_report)