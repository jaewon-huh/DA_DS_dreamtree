# 지도 스타일 적용하기 

import folium

# map() 함수에 tiles 옵션 적용 
seoul_map2 = folium.Map(location=[37.55,126.98],tiles ='Stamen Terrain',
                        zoom_start=12)
seoul_map3 = folium.Map(location=[37.55,126.98],tiles ='Stamen Toner',
                        zoom_start=15)

seoul_map2.save('실습/seoul2.html')
seoul_map3.save('실습/seoul3.html')