library(corrplot)
# 1-1
str(mtcars)
# str 함수를 통해 관측치 개수 , 변수 , 속성 파악 
dim(mtcars) # 관측치 32개 변수 11개 
summary(mtcars) # 각 변수들 요약 
head(mtcars) # 상단 6개의 값 

# 1-2 
car_cor <- cor(mtcars)
car_cor<- round(car_cor, 2 )
car_cor
# 유의성 검정 
cor.mtest(car_cor)
round(cor.mtest(car_cor)$p, 3) # p-value 만 확인 

# 1-3 
corrplot(car_cor)
# 가시성 있게 바꿨습니다.
corrplot(car_cor,
         method = "color",        # 색깔로 표현
         addCoef.col = "black")   # 상관계수 색깔
# 1-4 : 별도 파일
# cor.mtest의 p-vlaue 를 시각화 
corrplot(round(cor.mtest(car_cor)$p, 3),
         method = "color",        
         addCoef.col = "black") 


# 2-1 
result_lm <- lm(data = mtcars, mpg ~ wt)
summary(result_lm)

# 2-2 
# 회귀선 확인 : 계수가 -5.3445 로 선형적임
# 잔차 등분산성 검정 
plot(result_lm, which = 1) # 잔차와 예측값의 차이 
# 잔차의 정규성 검정
res <- residuals(result_lm) # 잔차 추출
qqnorm(res)
# 잔차의 독립성 검정 
library(lmtest)
dwtest(result_lm)
# DW값이 1.2517 이고 p-value 가 0.0102로 p < 0.05, 5%의 유의수준 

# 2-3 
summary(result_lm)
# 회귀 모형의 적합성 검정 
# F-statistic: 91.38 on 1 and 30 DF,  p-value: 1.294e-10
# F-검정통계량 p-value < 0.01. 따라서 회귀모형 적합

# 회귀 모형의 설명력 
# Multiple R-squared:  0.7528,	Adjusted R-squared:  0.7446 
# 결정계수 R^2 : 0.7528 로, 75.28%의 설명력을 가짐. 

# 2-4 : 별도 파일 