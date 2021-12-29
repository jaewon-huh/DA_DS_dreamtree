# 1번 문제 
# (1)
student <- c(30, 60, 30, 5, 25, 15, 100, 40, 20, 45)
student #확인
# (2)
student[c(1,10)] <- c(20, NA)
student #확인
# (3)
student[4:6]
# (4)
student[c(4,5,6)]
student[-c(1:3,7:10)]

# 2번 문제 
# (1)
goal <- c(23, 22, 22, 20, 19, 18, 18, 17, 17, 17)
assist <- c(5, 3, 2, 1, 10, 2, 7, 7, 6, 6)
foul <- c(19, 14, 37, 31, 16, 37, 46, 21, 28, 40)
# (2)
goal[-10]
# (3)
assist[seq(1,8,2)]
# (4)
# foul30 벡터는 foul < 30 이면 True를 리턴, else >=30 이면 다음 if else 문으로,
# 다음 if else 문에서 foul == 30이면 30 리턴, foul > 30 이면 F 리턴.
# 해당되지는 않지만 foul 값이 30인 경우도 포함하였습니다.
foul30 <- ifelse (foul < 30, T,
                  ifelse (foul == 30, 30,F))
foul30
# (5)
effective <- c(43, 42, 38, 39, 59, 37, 36, 44, 40, 43)
shooting <- c(89, 93, 93, 100, 131, 82, 78, 95, 80, 117)
accuracy <- (effective / shooting)

accuracy

# 3번 문제 
# (1)
trade <- read.csv("trade2000-2019.csv", header = T)
# (2)
trade[,seq(1,22,2)]  
# (3) 
subset(trade, X2010 >= 5000000, select = "국가명")
trade$국가명[trade$X2010 >= 5000000]
# (4)
subset(trade, X2000 <= 600000 & X2015 >= 1400000, select = "국가명" )
trade$국가명[trade$X2000 <= 600000 & trade$X2015 >= 1400000]
# (5)
trade$국가명[trade$X2019 - trade$X2000 >= 35000000]
# (6)
#trade_50을 문제의 조건을 만족하는 객체로 정의하였습니다. 
trade_50 <- trade$국가명[trade$X2019 * 2/3 >= trade$X2000] 
trade_50
length(trade_50) 












