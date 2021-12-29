# 각 국가의 교통사고 사망률 
traffic <- read.csv("deathrates.csv", header = T)
head(traffic)
#막대 기둥 그림표 히스토그램
hist(traffic$death)
?hist
hist(traffic$death,
     col = "lightblue",            # 색상
     labels = T,                   # 라벨 추가(값 크기) 
     xlab = "Death rates",         # x축 이름
     ylab = "Frequency",           # y축 이름
     main = "Traffic Death rates", # 제목
     ylim =c(0,20))                # y축 범위
colors()
# 막대 그래프 :빈도분포표 , 이산형 or 범주형 변수 barplot()
pop <- read.csv("popcities10.csv", header = T)
pop
?barplot
dbarplot(pop$pop10[1:7])
barplot(pop$pop10[1:7],
        names.arg = pop$municipality[1:7]) # x축
# 인구 단위수를 바꿔 
barplot(pop$pop10[1:7] / 1000, #단위 1000명
        names.arg = pop$municipality[1:7],
        ylab = "Population (in thousands)",
        main = "Population of Major Cities (2010)")        
# 지수가 아닌 숫자로 
options(scipen = 5)
barplot(pop$pop10[1:7],
        names.arg = pop$municipality[1:7],
        ylab = "Population (in thousands)",
        main = "Population of Major Cities (2010)")  
# 수평 막대 그래프 : x축이 인구수 
barplot(pop$pop10[1:7], 
        col = "lightblue",
        names.arg = pop$municipality[1:7],
        xlab = "Population",
        main = "Population of Major Cities (2010)",
        horiz = T)  
# 막대그래프 색 설정 
barplot(pop$pop10[1:4],
        col = c("Green1", "Green2", "Green3", "Green4"),
        names.arg = pop$municipality[1:4],
        ylab = "Population",
        main = "Population of Major Cities (2010)")

?t(x) # x = matrix, data.frame
# 00, 05, 10 년 막대 beside
beside_t <- t(pop[1:3,4:6])
beside_t
barplot(beside_t,
        col = c("Gold1", "Gold3", "Gold4"),
        beside = T,
        names.arg = pop$municipality[1:3])
# 범례로 막대그래프 알려주기 
?legend
legend("topright",
       c("2010", "2005", "2000"),
       cex =1, 
       fill = c("Gold1", "Gold3", "Gold4"))

# 원형그래프 pie() : 전체에서 차지 비율 , 텍스트 & 백분율
?pie()  #  x는 벡터 
cities <- pop$pop10[1:7]
names(cities) <- pop$municipality[1:7] # 벡터에 이름 할당 
cities[1:5]
pie(cities)
# 각 항목이 몇 % 차지 알고 싶음 : labels()
pr <- round(cities / sum(cities) * 100 ,1)  # 전체 중 비율, 소수점 1자리 
pr

?paste() # 하나로 합치되 sep = 구분 문자열 , collapse = 사이사이  
paste(c("a","b","c"),c("A","B","C"),sep="+",collapse="@")

paste("1st", "2nd", "3rd", sep = ", ")
paste(names(cities),
      "(", pr , "%)", sep = "") # 구분 없이 바로""

pie(cities,
    labels = paste(names(cities),
                   "(", pr , "%)", sep = ""))

# 산점도 : 두 변수간 관계 관찰 x축 y축, plot(x,y)
flights <- read.csv("outsourcing.csv", header = T)
head(flights)
?plot()
plot(flights$outsourcing, flights$delays)
plot(flights$outsourcing, flights$delays,
     xlab = "Maintenance Outsourcing(%)",
     ylab = "Flights Delay(%)",
     col = "red",
     pch = 19,
     main = "Outsourcing vs Flights Delays")
# 산점도의 선 긋기 lty 선 종류 , lwd 선 굵기 
?abline # h = y절편 (horizontal) , v = x 절편 (vertical)
abline(h = 20 , col = "red", lty = 2, lwd =2)
