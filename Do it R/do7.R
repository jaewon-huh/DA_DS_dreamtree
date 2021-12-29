# 인터렉티브 그래프 : 마우스 움직임 따라 실시간으로 변화 
# 패키지 
install.packages("plotly")
library(plotly)
# ggplot2로 만든 그래프를 plotly에 ggplotly()에 적용.
library(ggplot2)
p <- ggplot(data = mpg, aes(x = displ, y = hwy , col = drv)) +
  geom_point()
ggplotly(p)
# 인터렉티브 막대그래프 
q <- ggplot(data = diamonds, aes(x = cut, fill = clarity)) +
  geom_bar(position = "dodge")
ggplotly(q)

# 인터렉티브 시계열 그래프 
install.packages("dygraphs")
library(dygraphs)

economics <- ggplot2 :: economics
head(economics)
# 데이터가 시간 순서 속성을 지니는 xts 데이터 타입으로 되어 있어야 함 
library(xts)
# economics의 실업자 수를 xts 타입으로 변경 
eco <- xts(economics$unemploy, order.by = economics$date)
head(eco)
dygraph(eco)
# 날짜 범위 선택 기능 추가 dyRangeSelector
dygraph(eco) %>%  dyRangeSelector()
# 여러 값 표현 : 실업자 수와 저축률을 그래프에 함께 표현 
eco_a <- xts(economics$psavert, order.by = economics$date)
eco_b <- xts(economics$unemploy/1000, order.by = economics$date) # 저축률과 단위 일치 
eco2 <- cbind(eco_a,eco_b) # 가로로 결합 
colnames(eco2) <- c("psavert", "unemploy") # 변수명 변경경
head(eco2)
dygraph(eco2) %>% dyRangeSelector()
