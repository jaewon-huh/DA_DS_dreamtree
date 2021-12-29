library(ggplot2)
?qplot
qplot(data = mpg, x =hwy)
# 선 그래프 형태 
qplot(data = mpg, x= drv, y= hwy, geom = "line")
# 상자 그림 형태 
qplot(data = mpg, x= drv, y= hwy, geom = "boxplot")

# 혼자 4-2
x <- data.frame(제품 = c("사과", "딸기", "수박"),
           가격 = c(1800, 1500, 3000),
           판매량 = c(24, 38, 13))
mean(x$가격)
exam <- read.csv("excel_exam.csv", header = T, stringsAsFactors = F)

#05-2 변수명 바꾸기 
df_raw <- data.frame(var1 = c(1,2,3),
                     var2 = c(2,3,2))
df_raw
library(dplyr) #rename 함수 이용 
df_new <- df_raw # 변수명 바꾸기전에 원본 보유하기위해 복사본 생성,
df_new
?rename
rename(df_new, v2 = var2)
# mpg 통합 연비 변수 
mpg$total <- (mpg$cty + mpg$hwy) / 2 
mean(mpg$total)
summary(mpg$total)
hist(mpg$total)
mpg$test <- ifelse(mpg$total >= 20 , "pass", "fall")
head(mpg)
table(mpg$test) # table() : 빈도표
mpg$grade <- ifelse(mpg$total >= 30 , "A",
                    ifelse(mpg$total >=20, "B", "C"))
head(mpg)
table(mpg$grade)
qplot(mpg$grade)
# 05 분석도전 
midwest <- data.frame(midwest)
midwest <-rename(midwest, 
                 total = poptotal,
                 asian = popasian)
midwest$asianpercent <- (midwest$asian / midwest$total) * 100
hist(midwest$asianpercent)
mean(midwest$asianpercent)
midwest$test <- ifelse(midwest$asianpercent > mean(midwest$asianpercent),
                       "large", "small")
table(midwest$test)
qplot(midwest$test)
