# Decision Tree : 트리구조, 노드 - 분석 대상의 속성(설명변수)
# 엔트로피가 낮을수록 분류 잘 된 것.
import pandas as pd 
import numpy as np
from pandas.core.indexing import is_nested_tuple

'''
Step 1 : 데이터 준비 
'''
# Breast cancer 데이터 셋 
uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/\
breast-cancer-wisconsin/breast-cancer-wisconsin.data'
df = pd.read_csv(uci_path, header=None)

df.columns = ['id', 'clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
              'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses', 'class']

pd.set_option('display.max_columns', 15)

print(df.head(),'\n')

'''
Step2 : 데이터 탐색 
'''
print(df.info(),'\n') # bare_nuclei 만 문자열 / 나머지 숫자열 
print(df.describe())

# bare_nuclei 열을 숫자형으로 변경
print(df['bare_nuclei'].unique(),'/n')  # '?' 발생 
df['bare_nuclei'].replace('?', np.nan, inplace = True)
df.dropna(subset = ['bare_nuclei'], axis =0 , inplace =True) # 누락 데이터 행 삭제 
df['bare_nuclei'] = df['bare_nuclei'].astype('int')

print(df.describe())


'''
Step3 : 데이터 구분 (훈련 / 검증 )
'''
# 설명변수 X / 예측(종속)변수 Y = 'class'
X = df[['clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
        'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses']]  # 설명 변수 X
y = df['class']  # 예측 변수 Y

# 설명 변수 데이터를 정규화
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

# train data 와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

print('train data 개수: ', X_train.shape)
print('test data 개수: ', X_test.shape)
print('\n')

'''
Step 4 : Decision Tree 분류 모형 
'''
from sklearn import tree

# 모델 객체 생성 (criterion = 'entropy')
tree_model = tree.DecisionTreeClassifier(criterion= 'entropy', max_depth= 5) 
# 분류 정도 평가 기준 엔트로피 , 트리레벨 5

# train data를 가지고 모형학습
tree_model.fit(X_train, y_train)
# test data를 가지고 y_hat 예측 
y_hat = tree_model.predict(X_test)   # 2 : 양성(benign) , 4 : 악성(malignant)

print(y_hat[0:10])
print(y_test.values[0:10], '\n')

# 모형 성능 평가 - confusion_matrix()
from sklearn import metrics
tree_matrix = metrics.confusion_matrix(y_test, y_hat)
print(tree_matrix, '\n')
# 모형 성능 평가 - 평가지표 계산
tree_report = metrics.classification_report(y_test,y_hat)
print(tree_report)