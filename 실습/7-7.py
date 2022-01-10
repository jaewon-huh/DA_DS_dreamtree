# 군집  : 데이터셋의 관측값이 갖고 있는 여러 속성을 분석해 서로 비슷한 특징을 갖는 관측값끼리 같은 집단으로 묶음
# 클러스터 별로 서로 완전 구분 -> 어느 집단에도 속하지 못하는 관측값 (이상값 및 중복값) 관측.
# 비지도 학습 : 정답x, 데이터 자체의 유사성만을 기준으로 판단. 
# 구매 패턴 분석 등 소비자 행동 특성을 그룹화

# K-Means : 데이터 간 유사성 , 각 클러스터의 중심까지의 거리 
import pandas as pd 
import matplotlib.pyplot as plt 

'''
Step 1 데이터 준비 
'''
# 도매업 고객 데이터셋 
uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/\
00292/Wholesale%20customers%20data.csv'
df = pd.read_csv(uci_path, header=0)


''' 
Step 2 데이터 탐색
'''
print(df.head(), '\n')
print(df.info(), '\n')
print(df.describe())

# df 전체를 모형의 학습데이터로 사용, 비지도 -> 예측변수 x 모든 변수를 설명변수로 

'''
Step 3 : 데이터 전처리 
'''
# 분석에 사용할 속성
X = df.iloc[ : ,]
print(X[:5],'\n')

# 설명 변수 데이터 정규화  : preprocessing , StandardScaler
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

print(X[:5])

'''
Step 4 : 모형 학습 및 검증 - cluster 모듈 Kmeans()
'''
from sklearn import cluster 

# 모형 객체 생성
kmeans = cluster.KMeans(init="k-means++", n_clusters= 5, n_init= 10)  # 클러스터 개수 5 
# 모형 학습
kmeans.fit(X)

# 예측 
cluster_label = kmeans.labels_ 
print(cluster_label, '\n')       # 0~4 , 5개의 클러스터로 구분
# 예측결과를 df에 추가 
df['Cluster'] = cluster_label 
print(df.head())

# 그래프로 표현 - 시각화 
# 2개의 변수를 선택해 관측값의 분포
df.plot(kind ='scatter', x = 'Grocery', y = 'Frozen', c ='Cluster', cmap ='Set1',
        colorbar = False, figsize =(10,10))
df.plot(kind ='scatter', x = 'Milk', y = 'Delicassen', c ='Cluster', cmap ='Set1',
        colorbar = True, figsize =(10,10))
plt.show()
plt.close()

# 큰 값으로 구성된 클러스터(0,4)를 제외하고 다시 - 값이 몰려있는 구간 분석
mask = (df['Cluster'] == 0) | (df['Cluster'] == 4)
ndf = df[-mask]

ndf.plot(kind ='scatter', x = 'Grocery', y = 'Frozen', c ='Cluster', cmap ='Set1',
        colorbar = False, figsize =(10,10))
ndf.plot(kind ='scatter', x = 'Milk', y = 'Delicassen', c ='Cluster', cmap ='Set1',
        colorbar = True, figsize =(10,10))

plt.show()
plt.close()