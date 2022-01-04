# 지도에 마커 표시하기 

import pandas as pd 
import folium

# 대학교 리스트 df로 
df =pd.read_excel('예제/part4/서울지역 대학교 위치.xlsx', index_col= 'Unnamed: 0')

print(df.head())
# 서울지도 
seoul_map = folium.Map(location=[37.55,126.98],tiles ='Stamen Terrain',
                        zoom_start=12)

# 대학교 위치 정보를 CircleMarker로 표시
# Marker() 함수에 위도, 경도 정보 표시 , popup 옵션 
for name, lat, lng in zip(df.index, df.위도 , df.경도):
    folium.CircleMarker([lat,lng],
                        radius= 10,           #원 반지름
                        color = 'brown',      #원 둘레 색상
                        fill = True, 
                        fill_color = 'coral', #원 색상
                        fill_opacity =0.7,    #투명도 
                        popup= name
    ).add_to(seoul_map)

seoul_map.save('실습/seoul_colleges2.html')