# 근무환경 만족 과 직장만족 간 상관관계
work <- read.csv("work_cor.csv", header = T)
head(work,3) 
summary(work) # environt 평균 92.4 직장 평균 93.1
# 산점도로 두 변수 간 관계 분석
plot(work$environment, work$satisfaction,
     xlab = "working environment",
     ylab = "job satisfaction")
# 상관분석
cor(work$environment, work$satisfaction) # 상관계수 0.303
cor.test(work$environment, work$satisfaction)
# 유의성 p-value = 0.014 < 0.05 따라서 유의미함 
# 근무환경 만족과 직장만족 간에  뚜렷한 양의 상관관계

# 상관분석 시각화 : corrplot() 상관행렬 히트맵 , 매트릭스여야 함 
y <- c(41,49,69,65,40,50,58,57,31,36,44,57,19,31,33,43)
x1 <- c(1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4)
x2 <- c(5,5,5,5,10,10,10,10,15,15,15,15,20,20,20,20)
ne
x3 <- rep(1:4,4)
x4 <- rep(c(5,10,15,20), each =4)
x4
xy <- cbind(x1,x2,y)
cor(xy)
library(corrplot)
cor <- cor(xy)
corrplot(cor) 

 # 회귀분석  lm(data, 종속 ~ 독립 , ...)
# cars 데이터 , 속도에 따른 거리의 관계분석 
result_lm<- lm(data = cars , dist ~ speed)
summary(result_lm)
# coefficients : 계수 & 절편 -> y = -17.59 = 3.9324 x 

# 회귀분석 절차 
# 기본가정 충족 ? 
# 잔차 등분산성(일정한 분산) & 정규성(오차 기대값 0, 정규분포 따르나 ) 검정
plot(result_lm, which = 1) 

# 잔차와 적합값의 분포  : 등분산성 따르는지 , 빨간선 기울기 0일수록 굿 

res <- residuals(result_lm) # 잔차 추출 
qqnorm(res) # 잔차의 정규성 검정

# 잔차의 독립성 검정 (더빈-왓슨값) : dwtest()
install.packages("lmtest")
library(lmtest)
dwtest(result_lm)
# DW 값 0 ~ 2 ~ 4 , 0 + 상관 2 독립 4 - 상관 & p-value 유의성  

# 회귀계수 유의미 t검정  : pr(t) 
# 회귀모형 적합성 F 검정 : F-statistic
summary(result_lm)

# 회귀모형 설명력 : 결정계수 R^2 , 0 ~ 1 , 1 설명력 높음 
# -> Multiple R-squared : 0.6511 : 65.11 % 설명함 .

# 결과표 
plot(cars$speed, cars$dist,
     xlab = "speed",
     ylab = "dist",
     main = "speed -> dist")
abline(result_lm, col = "blue")
