library(readxl)
library(dplyr)
library(ggplot2)
library(lmtest)
options(scipen = 99)
# 14년 01 ~ 21년 9월 까지의 기사량 데이터
news <- read.csv('amCharts.csv')
head(news)
str(news)
news$date <- as.Date(news$date)
str(news)
# 시계열 그래프로 기사량 동향 확인
ggplot(data = news, aes (x = date, y = data, group =1)) +
  geom_line() +
  ylim(0, 1000)
  
# 14 ~ 21 년 9월 리튬이차전지 수출량 hscode 850760
lit_export <- read_excel('리튬 월별 수출입 실적.xlsx')
lit_export <- rename(lit_export,
                     date1 = '기간',
                     export = '수출중량')
str(lit_export)
ggplot(data = lit_export, aes (x = date1, y = export, group = 1)) +
  geom_line() 

# 기사량 데이터와 리튬이차전지 수출량 의 관계 
news_lit_ex <- cbind(news,lit_export)
news_lit_ex <- news_lit_ex %>% 
  select(date,data,export)
head(news_lit_ex)
# 산점도 
plot(news_lit_ex$data, news_lit_ex$export)
# 상관관계 
cor(news_lit_ex$data, news_lit_ex$export)
cor.test(news_lit_ex$data, news_lit_ex$export)

library(lmtest)

# 회귀분석
result<- lm(data = news_lit_ex, news_lit_ex$export ~ news_lit_sam$data)
summary(result)

# 회귀분석 가정 충족 
# 등분산성
plot(result, which = 1)
# 정규성 검정
res <- residuals(result)
qqnorm(res)
# 독립성 검정 
dwtest(result)


# 리튬이차전지 주요 3사의 주가 데이터 비교 
sam <- read.csv('삼성SDI.KS.csv')
head(sam)
str(sam)
ggplot(data = sam, aes (x = Date, y = Close, group = 1)) +
  geom_line()

sk <- read.csv('SK이노.KS.csv')
str(sk)
ggplot(data = sk, aes (x = Date, y = Close, group = 1)) +
  geom_line()

lg <- read.csv('LG화학.KS.csv')
str(lg)
ggplot(data = lg, aes (x = Date, y = Close, group = 1)) +
  geom_line()

# 기사 데이터와 주가데이터의 상관관계 
# 삼성SDI
news_lit_sam <- cbind(news, sam)
news_lit_sam <- news_lit_sam %>% 
  select(date, data, Close)
head(news_lit_sam)

# 산점도 
plot(news_lit_sam$data, news_lit_sam$Close)
# 상관관계 
cor(news_lit_sam$data, news_lit_sam$Close)
cor.test(news_lit_sam$data, news_lit_sam$Close)

# 회귀분석
result2<- lm(data = news_lit_sam, news_lit_sam$Close ~ news_lit_sam$data)
summary(result2)

# 회귀분석 가정 충족 
# 등분산성
plot(result2, which = 1)
# 정규성 검정
res2 <- residuals(result2)
qqnorm(res2)
# 독립성 검정 
dwtest(result2)

summary(result2)

# sk
news_lit_sk <- cbind(news, sk)
news_lit_sk <- news_lit_sk %>% 
  select(date, data, Close)
head(news_lit_sk)

# 산점도 
plot(news_lit_sk$data, news_lit_sk$Close)
# 상관관계 
cor(news_lit_sk$data, news_lit_sk$Close)
cor.test(news_lit_sk$data, news_lit_sk$Close)

# 회귀분석
result3<- lm(data = news_lit_sk, news_lit_sk$Close ~ news_lit_sk$data)
summary(result3)

# 회귀분석 가정 충족 
# 등분산성
plot(result3, which = 1)
# 정규성 검정
res3 <- residuals(result3)
qqnorm(res3)
# 독립성 검정 
dwtest(result3)

summary(result3)


# lg
news_lit_lg <- cbind(news, lg)
news_lit_lg <- news_lit_lg %>% 
  select(date, data, Close)
head(news_lit_lg)

# 산점도 
plot(news_lit_lg$data, news_lit_lg$Close)
# 상관관계 
cor(news_lit_lg$data, news_lit_lg$Close)
cor.test(news_lit_lg$data, news_lit_lg$Close)

# 회귀분석
result4<- lm(data = news_lit_lg, news_lit_lg$Close ~ news_lit_lg$data)
summary(result4)

# 회귀분석 가정 충족 
# 등분산성
plot(result4, which = 1)
# 정규성 검정
res4 <- residuals(result4)
qqnorm(res4)
# 독립성 검정 
dwtest(result4)

summary(result4)

# 리튬의 원자재 가격 비교 
lit_price <- read_excel('리튬 가격.xls')
head(lit_price)
str(lit_price)
lit_price <- rename(lit_price,
                    price = '기준가격',
                    date1 = '기준일')

# 시계열 그래프 
ggplot(data = lit_price, aes (x = date1, y = price ,group =1)) +
  geom_line()

# 기사량 데이터와 리튬 원자재가의 관계 
news_lit_price <- cbind(news,lit_price)
news_lit_price <- news_lit_price %>% 
  select(date, data, price)
head(news_lit_price)
# 산점도 
plot(news_lit_price$data, news_lit_price$price)
# 상관관계 
cor(news_lit_price$data, news_lit_price$price)
cor.test(news_lit_price$data, news_lit_price$price)

# 회귀분석
result5<- lm(data = news_lit_price, news_lit_price$price ~ news_lit_price$data)
summary(result5)

# 회귀분석 가정 충족 
# 등분산성
plot(result5, which = 1)
# 정규성 검정
res5 <- residuals(result5)
qqnorm(res5)
# 독립성 검정 
dwtest(result5)

summary(result5)



# 14 ~ 21 년 9월 태양광 모듈 + 전지 수출량 hscode 
sun_export <- read_excel('태양광 수출량.xlsx')
sun_export
sun_export <- rename(sun_export,
                     date1 = '기간',
                     export = '수출중량')
ggplot(data = sun_export, aes (x = date1, y = export, group = 1)) +
  geom_line()

# 기사량 데이터와 태양전지 수출량 의 관계 
news_sun_ex <- cbind(news,sun_export)
news_sun_ex <- news_sun_ex %>% 
  select(date, data, export)
head(news_sun_ex)
# 산점도 
plot(news_sun_ex$data, news_sun_ex$export)
# 상관관계 
cor(news_sun_ex$data, news_sun_ex$export)
cor.test(news_sun_ex$data, news_sun_ex$export)

# 회귀분석

result6<- lm(data = news_sun_ex, news_sun_ex$export ~ news_sun_ex$data)
summary(result6)

# 회귀분석 가정 충족 
# 등분산성
plot(result6, which = 1)
# 정규성 검정
res6 <- residuals(result6)
qqnorm(res6)
# 독립성 검정 
dwtest(result6)


# 태양광전지 주요 2사의 주가 데이터 비교 
oci <- read.csv('OCI.KS.csv')
str(oci)
ggplot(data = oci, aes (x = Date, y = Close, group = 1)) +
  geom_line()

hanwha <- read.csv('한화솔루션.KS.csv')
str(hanwha)
ggplot(data = hanwha, aes (x = Date, y = Close, group = 1)) +
  geom_line()

# 기사 데이터와 주가데이터의 상관관계 
# OCI
news_sun_oci <- cbind(news, oci)
news_sun_oci <- news_sun_oci %>% 
  select(date, data, Close)
head(news_sun_oci)

# 산점도 
plot(news_sun_oci$data, news_sun_oci$Close)
# 상관관계 
cor(news_sun_oci$data, news_sun_oci$Close)
cor.test(news_sun_oci$data, news_sun_oci$Close)

# 회귀분석
result7<- lm(data = news_sun_oci, news_sun_oci$Close ~ news_sun_oci$data)
summary(result7)

# 회귀분석 가정 충족 
# 등분산성
plot(result7, which = 1)
# 정규성 검정
res7 <- residuals(result7)
qqnorm(res7)
# 독립성 검정 
dwtest(result7)

# 한화솔루션
news_sun_hanwha <- cbind(news, hanwha)
news_sun_hanwha <- news_sun_hanwha %>% 
  select(date, data, Close)
head(news_sun_hanwha)

# 산점도 
plot(news_sun_hanwha$data, news_sun_hanwha$Close)
# 상관관계 
cor(news_sun_hanwha$data, news_sun_hanwha$Close)
cor.test(news_sun_hanwha$data, news_sun_hanwha$Close)

# 회귀분석
result8<- lm(data = news_sun_hanwha, news_sun_hanwha$Close ~ news_sun_hanwha$data)
summary(result8)

# 회귀분석 가정 충족 
# 등분산성
plot(result8, which = 1)
# 정규성 검정
res8 <- residuals(result8)
qqnorm(res8)
# 독립성 검정 
dwtest(result8)


