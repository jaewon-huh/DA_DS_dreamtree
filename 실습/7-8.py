# DBSCAN : 데이터가 위치하고 있는 공간 밀집도를 기준으로 클러스터 구분
# 자기를 중심으로 R 

import pandas as pd 
import folium

'''
Step 1 : 데이터 준비 
'''

# 서울 시내 중학교 진학률 데이터 셋 
file_path = '예제/part7/2016_middle_shcool_graduates_report.xlsx'
df = pd.read_excel(file_path, header=0)

# IPython Console 디스플레이 옵션 설정하기
pd.set_option('display.width', None)        # 출력화면의 너비
pd.set_option('display.max_rows', 100)      # 출력할 행의 개수 한도
pd.set_option('display.max_columns', 10)    # 출력할 열의 개수 한도
pd.set_option('display.max_colwidth', 20)   # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)   # 유니코드 사용 너비 조정

# 열 이름 배열 출력
print(df.columns.values)

'''
Step2 : 데이터 탐색
'''
print(df.head(), '/n')
print(df.info(), '/n')
print(df.describe(),'\n')

# 지도에 위치 표시 
mschool_map = folium.Map(location=[37.55,126.98], tile = 'Stamen Terrain', zoom_start= 12)

# 중학교 위치 정보를 CircleMarker 로 표시
for name, lat ,lng in zip(df.학교명 , df.위도, df.경도):
    folium.CircleMarker([lat,lng],
                        radius=5,
                        color ='brown',
                        fill = True,
                        fill_color ='coral',
                        fill_opacity = 0.7,
                        popup= name
                        ).add_to(mschool_map)

# 저장 
mschool_map.save('seoul_mschool_location.html')

'''
Step 3 : 데이터 전처리
'''
# 문자열 데이터 더미변수로 전환 
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
onehot_encoder = preprocessing.OneHotEncoder()

onehot_location = label_encoder.fit_transform(df['지역'])
onehot_code = label_encoder.fit_transform(df['코드'])
onehot_type = label_encoder.fit_transform(df['유형'])
onehot_day = label_encoder.fit_transform(df['주야'])

df['location'] = onehot_location
df['code'] = onehot_code
df['type'] = onehot_type
df['day'] = onehot_day

print(df.head())

'''
Step 4 : DBSCAN 군집 모형 
'''
from sklearn import cluster 

# 분석에 사용할 속성 선택(과학고, 외고_국제고, 자사고 진학률)
columns_list = [10,11,14]
X = df.iloc[:, columns_list]
print([X[:5]], '\n')

# 설명 변수 데이터 정규화
X = preprocessing.StandardScaler().fit(X).transform(X)

# DBSCAN 객체 생성
dbm = cluster.DBSCAN(eps = 0.2, min_samples=5)  # 반지름 0.2 , 최소포인트 개수 5

# 모형 학습
dbm.fit(X)
# 예측
cluster_label = dbm.labels_
print(cluster_label, '\n')  # -1 0 1 2 3 

# 예측 결과를 df에 추가 
df['Cluster'] = cluster_label
print(df.head())

# 클러스터 값으로 그룹하하고 그룹별로 내용 출력 
grouped_cols = [1,2,4] + columns_list    # 지역, 학교명, 유형 , 과학고 ,외고_국제고 ,자사고
grouped = df.groupby('Cluster')
for key, group in grouped : 
    print('*key :', key)
    print('*number :', len(group))
    print(group.iloc[:, grouped_cols].head(5), '\n')

# -1 : Noise , 0 1 2 3 : 4개의 클러스터 

# 그래프로 표현 - 시각화
colors = {-1:'gray', 0:'coral', 1:'blue', 2:'green', 3:'red', 4:'purple', 
          5:'orange', 6:'brown', 7:'brick', 8:'yellow', 9:'magenta', 10:'cyan', 11:'tan'}

cluster_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster):  
    folium.CircleMarker([lat, lng],
                        radius=5,                   # 원의 반지름
                        color=colors[clus],         # 원의 둘레 색상
                        fill=True,
                        fill_color=colors[clus],    # 원을 채우는 색
                        fill_opacity=0.7,           # 투명도    
                        popup=name
    ).add_to(cluster_map)

# 지도를 html 파일로 저장하기
cluster_map.save('seoul_mschool_cluster.html')

# X2 데이터 셋에 대하여 위의 과정을 반복
columns_list2= [10, 11, 14, 23]   # type열 (자사고 진학률 + 설립유형)
X2 = df.iloc[:, columns_list2]
print(X2[:5], '\n')

# 설명 변수 데이터 정규화
X2 = preprocessing.StandardScaler().fit(X2).transform(X2)

# DBSCAN 객체 생성
dbm2 = cluster.DBSCAN(eps = 0.2, min_samples=5)  # 반지름 0.2 , 최소포인트 개수 5

# 모형 학습
dbm2.fit(X2)
df['Cluster2'] = dbm2.labels_

# 클러스터 값으로 그룹하하고 그룹별로 내용 출력 
grouped2_cols = [1,2,4] + columns_list2   # 지역, 학교명, 유형 , 과학고 ,외고_국제고 ,자사고
grouped2 = df.groupby('Cluster2')
for key, group in grouped2 : 
    print('*key :', key)
    print('*number :', len(group))
    print(group.iloc[:, grouped2_cols].head(5), '\n')

# -1 인 노이즈의개수 281개 / 0~10 11개의 클러스터로 구분 

# 그래프로 표현 - 시각화

cluster2_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                          zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster2):  
    folium.CircleMarker([lat, lng],
                        radius=5,                   # 원의 반지름
                        color=colors[clus],         # 원의 둘레 색상
                        fill=True,
                        fill_color=colors[clus],    # 원을 채우는 색
                        fill_opacity=0.7,           # 투명도    
                        popup=name
    ).add_to(cluster2_map)

# 저장 
cluster2_map.save('seoul_mschool_cluster2.html')   