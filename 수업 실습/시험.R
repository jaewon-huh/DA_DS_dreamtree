library(readxl)
library(dplyr)
# 14년 01 ~ 20년 12월 까지의 기사량 데이터
news <- read_excel(file.choose())
# 14년 01~ 20년 12월 까지의 lit etf 주가 
lit2 <- read.csv(file.choose())
news_lit <- cbind(news, lit2)
# 기사량과 lit etf 종가 의 관계  
# 산점도
plot(news_lit$`친환경 무역`, news_lit$Close)
# 상관계수
cor(news_lit$`친환경 무역`, news_lit$Close)
# 0.25
# 통계적 유의성
cor.test(news_lit$`친환경 무역`, news_lit$Close)
# p- value : 0.02 < 0.05  95% 신뢰성
# 회귀분석
result<- lm(data = news_lit, news_lit$Close ~ news_lit$`친환경 무역`)
summary(result)

library(lmtest)
# 회귀분석 가정 충족 
# 등분산성
plot(result, which = 1)
# 정규성 검정
res <- residuals(result)
qqnorm(res)
# 독립성 검정 
dwtest(result)
# DW 값 0.18 로 양의 상관관계 , p-value < 0.01 ***

summary(result)
# t 검정 신뢰성 5% 유의수준 
# F 검정 p-value < 0.05 5% 유의수준 
# 설명력은 낮음 R- squared : 0.064 

# 모형은 적합하나 상관관계 및 설명력이 낮음. 
# 국내 기사량 -> 미국 etf (lit) 설정의 잘못된 변수 선정의 문제이거나
# 통제하지 못한 변수의 영향력 때문일 수도 있을 것.