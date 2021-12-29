# 지도 시각화 : 단계 구분도(choropleth map )
# 미국 주별 범죄율 데이터 
# 패키지 로드 
install.packages("ggmap")
library(ggiraphExtra)
library(ggplot2)
library(maps)
library(ggmap)
library(mapproj)

str(USArrests)
head(USArrests)
View(USArrests)

# 지역명 변수가 따로 없고 행이름이 지역명으로 되어있음 
library(tibble)
crime <- rownames_to_column(USArrests, var = "state") # 행이름을 state 변수로 
crime$state <- tolower(crime$state) #소문자로 변환
str(crime)

# 미국주 지도 데이터 
install.packages("maps")
library(ggplot2)
states_map <- map_data("state")
str(states_map)
# 단계 구분도 
ggChoropleth(data = crime,        # 지도에 표현할 데이터 
             aes(fill = Murder,   # 색깔별로 표시할 변수
                 map_id = state), # 지역 기준 변수 
             map = states_map,    # 지도 데이터 
             interactive = T)     # 인터렉티브 

# 대한민국 시도별 인구 , 결핵 환자 수 단계 구분도 kormaps2014
# 패키지 준비 
install.packages("stringi")
install.packages("devtools")
devtools::install_github("cardiomoon/kormaps2014") # 깃허브의 패키지 설치 
library(kormaps2014)
# 대한민국 시도별 인구데이터 
# korpop1 : 시도별 , korpop2 : 시군구별 , korpop3 읍면동별
str(changeCode(korpop1)) # 한글이 깨지지 않게
# 변수명 영문으로 
library(dplyr)
korpop1 <- rename(korpop1, 
                  pop = 총인구_명,
                  name = 행정구역별_읍면동)
korpop1
korpop1$name # 이름 다깨짐 
korpop1$name <- iconv(korpop1$name, "UTF-8", "CP949")
?iconv # (x, from = , to = )
# 대한민국 시도별 지도데이터 
str(changeCode(kormap1))
# 단계 구분도 만들기 
ggChoropleth(data = korpop1,     # 지도에 표시할 데이터   
             aes(fill = pop,     # 색깔별 표현할 변수
                 map_id = code,  # 지역 기준 변수 = 지역 코드
                 tooltip = name), # 지도위 표시할 지역명 
             map = kormap1,      # 지도 데이터 
             interactive = T)

# 대한민국 시도별 결핵 환자 수 단계 구분도. tbc
str(changeCode(tbc)) # NewPts : 결핵환자 수 
tbc$name <- iconv(tbc$name,"UTF-8", "CP949")
ggChoropleth(data = tbc,
             aes(fill = NewPts,
                 map_id = code,
                 tooltip = name),
             map = kormap1,
             interactive = T)
