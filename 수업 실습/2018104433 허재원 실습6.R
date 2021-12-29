library(ggiraphExtra)
library(ggplot2)
library(maps)
library(ggmap)
library(mapproj)

# 1-1
# 수출 데이터 호출 
wld_kor <- read.csv(file.choose(), header = T, stringsAsFactors = F)
# 구조 파악 
str(wld_kor)
View(wld_kor)
head(wld_kor)
# 변수명 깨진거 바꾸기.
library(dplyr)
wld_kor <- rename(wld_kor,
                  "year" = "癤퓓ear")
head(wld_kor)
options(scipen = 99)

# 시계열 그래프 
ggplot(data = wld_kor, aes(x = year, y = korea)) +
  geom_line() 
  
# 1-2
# 대한민국 시도별 수출입 정보 호출 
kor_export <- read.csv(file.choose(), header = T, stringsAsFactors = F)
# 구조 파악 
kor_export
str(kor_export)
# 대한민국 시도별 지도 데이터 
library(kormaps2014)
str(changeCode(kormap1))
# 대한민국 시도별 수출량 단계구분도
ggChoropleth(data = kor_export,     # 지도에 표시할 데이터   
             aes(fill = export,     # 색깔별 표현할 변수
                 map_id = code,     # 지역 기준 변수 = 지역 코드
                 tooltip = name),   # 지도위 표시할 지역명 
             map = kormap1,         # 지도 데이터 
             interactive = T)
