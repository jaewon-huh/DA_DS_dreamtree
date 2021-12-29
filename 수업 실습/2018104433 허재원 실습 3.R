deathrates <- read.csv("deathrates.csv", header = T)
pop <- read.csv("popcities10.csv", header = T)
library(dplyr)
# 1-1
hist(deathrates$death,
     xlab = "Death rates",
     ylab = "Frequency")
# 1-2
deathrates <- deathrates %>% arrange(death) #사망률을 오름차순으로 정렬시킴
barplot(deathrates$death,
        names.arg = deathrates$country,
        xlab = "Countries",   # x축 설명
        ylab = "Death rates") # y축 설명
# 1-3 
summary(deathrates$death)
deathrates$death_cut<- cut(deathrates$death,
    breaks = c(0, 11, 18, Inf),
    labels = c("낮음", "보통", "높음")) 
# 1-4
summary(deathrates$death_cut) 
# summary()를 통해 분류된 deathrates$death_cut의 빈도분포를 구함.
deathrates_bar <- table(deathrates$death_cut)
deathrates_bar
barplot(summary(deathrates$death_cut),
        main = "Traffic fatalities in each country",
        xlab = "Traffic Death Rates",
        ylab = "Number of Countries",
        col = "lightblue")

#2-1
pop %>% filter(municipality == "Gunsan") # 군산 데이터 찾기 
plot_t <- t(pop[38,6:4]) #군산의 인구수 데이터를 데이터프레임화 
plot_t
plot(plot_t,
     main = "Population Changes in Gunsan, 2000 - 2010",
     xlab = "Years",
     ylab = "Population")

mean(plot_t) # 군산의 평균인구
abline(h = mean(plot_t), col ="red", lty =1, lwd =2 )
# x축의 인덱스 값을 년도로 표시하는것은 방법을 모르겠습니다.
pop_gunsan <- pop %>% 
    filter(municipality == "Gunsan") %>% 
    mutate(mean = (pop10 + pop05 + pop00) / 3)
pop_gunsan



plot(c(2000, 2005, 2010), # x축에는 벡터만 
     c(pop_gunsan$pop00, pop_gunsan$pop05, pop_gunsan$pop10), 
     xlab = "Years",
     ylab = "Population",
     main = "Population Changes in Gusan, 2000-2010",
     type = "b")
abline(h = 257867.7, col = "red", lty = 1, lwd = 1)


#2-2
hist(pop$pop10/ 10000, #단위 10000명
     labels = T,
     main = "Distribution of Populatuion in 2010",
     xlab = "Population (10000)",
     ylab = "Frequency") 
# 2-3 
pop_gyeonggi <- filter(pop, provinces == "Gyeonggi") # 경기도 추출
options(scipen = 5)
barplot(pop_gyeonggi$pop10[1:5],
        names.arg = pop_gyeonggi$municipality[1:5],
        main = "Top 5 Population of Gyeonggi in 2010",
        xlab = "City Name",
        ylab = "Population")
# 2-4
beside_t <- t(pop[1:5,4:6]) #2010년 인구가 가장많은 5개 도시의 2000~2010년 인구 추출출
beside_t
barplot(beside_t,
        beside = T,
        col = c("Gold1", "Gold2", "Gold3"),
        names.arg = pop$municipality[1:5],
        main = "The Population of cities Top5",
        xlab = "City Name",
        ylab = "Population")     
# 2-5
x <- (pop$pop10-pop$pop00)/pop$pop00 *100 # 00년 ~ 10년의 인구증가율
pop$increase <- round(x,1)
pop %>% 
    arrange(desc(increase)) %>% 
    select(municipality) %>% 
    head(7)

# 2-6
pop_1 <- arrange(pop,desc(increase))
barplot(pop_1$increase[1:7],
        names.arg = pop_1$municipality[1:7],
        main = "Population Growth Rate Top 7",
        xlab = "Cities",
        ylab = "Population Growth Rate (%) ")

