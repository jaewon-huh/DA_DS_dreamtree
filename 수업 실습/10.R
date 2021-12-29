# ggplot 레이어 구조 (1. 배경(축) 2. 그래프 추가 3. 설정 (축범위 ,색 ,표식..))
library(ggplot2)
options(scipen = 99)
# 배경 생성 ggplot(data = , aes(x= ,y= ))
ggplot(data = mpg , aes(x = displ ,y = hwy))
#배경에 산점도 추가 geom_point() : 두 변수간 관계
ggplot(data = mpg , aes(x = displ ,y = hwy)) + geom_point()
# 축 범위 추가 
ggplot(data = mpg , aes(x = displ ,y = hwy)) + 
  geom_point() +
  xlim(3,6) +
  ylim(10,30)

# 막대그래프 geom_col() :집단간 차이 /  빈도 막대 그래프 geom_bar()
# 막대그래프 geom_col() :집단간 차이
# 구동방식 별 평균 고속도로 연비 
library(dplyr)
mpg <- ggplot2 :: mpg
df_mpg <- mpg %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy))
df_mpg
# 그래프 
ggplot(data = df_mpg, aes(x = drv, y = mean_hwy)) +
  geom_col() 
# 크기 순으로 정렬 reorder(x, 정렬 기준 변수 )
ggplot(data = df_mpg, aes(x= reorder(drv, mean_hwy) , y = mean_hwy)) +
  geom_col()
ggplot(data = df_mpg, aes(x= reorder(drv, -mean_hwy) , y = mean_hwy)) +
  geom_col() #내림차순  

# 빈도 막대 그래프 geom_bar() : x 축만 지정 , 값의 개수 
# 고속도로 연비 자동차 빈도 
ggplot(data = mpg, aes(x=hwy)) +
  geom_bar()

# 선그래프 : 시간에 따라 달라지는 데이터표현
# 시계열 그래프 (일별 환율 , 주가지수 ,,) : geom_line()
economics # 월별 미국 경제지표 
# 시간에 따른 실업자수  
ggplot(data = economics, aes(x =date, y= unemploy)) +
  geom_line()
# 시간에 따른 저축률 psavert 변화
ggplot(data = economics, aes(x =date, y= psavert)) +
  geom_line()

# 1970~ 2019년까지 전세계 수출 동향. 

# 상자그림 geom_boxplot() : 데이터의 분포 (특징 이해)
# mpg의 구동방식 drv 별 , hwy 고속도로 연비 
ggplot(data = mpg, aes(x= drv, y = hwy)) +
  geom_boxplot()

# class 별 cty 비교 
df_mpg <- mpg %>% 
  filter(class %in% c("compact", "subcompact", "suv"))
ggplot(data = df_mpg, aes(x = class, y = cty)) + 
  geom_boxplot()

