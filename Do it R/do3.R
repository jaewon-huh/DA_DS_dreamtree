# 결측치 
df <- data.frame(sex = c(" M", "F", NA, "M", "F"),
                 score = c(5, 4, 3, 4, NA))
df
is.na(df) # 결측지 확인 
table(is.na(df))
library(dplyr)
df %>% filter(!is.na(score)) # 결측치 제거함
df_nomiss <- df %>% filter(!is.na(sex) & !is.na(score))
df_nomiss
df_nomiss2 <- na.omit(df) # 모든 결측치 행 제거 
df_nomiss2
# 함수의 결측치 제외기능  na.rm 파라미터 
mean(df$score, na.rm = T)
sum(df$score, na.rm = T)
# 결측치 대체 
exam
exam[c(3,8,15), "math"] <- NA
exam
exam %>% summarise(mean_math = mean(math, na.rm = T))
# 결측치를 평균값으로 대체 
exam$math <- ifelse(is.na(exam$math), 55 , exam$math)
exam
# 이상치 정제 
outlier <- data.frame(sex = c(1,2,1,3,2,1),
                      score = c(5, 4, 3, 4, 2, 6))
outlier # sex = 3 & score = 6 
table(outlier)
# 이상치를 결측치로 변환 
outlier$sex <- ifelse(outlier$sex == 3 , NA , outlier$sex)
outlier$score <- ifelse(outlier$score == 6 , NA, outlier$score)
outlier
# 그후 분석 
outlier %>% 
  filter(!is.na(outlier$score) & !is.na(outlier$sex)) %>% 
  group_by(sex) %>% 
  summarise(mean_score = mean(score))
# 이상치 (극단치) 제거 
# 상자그림으로 극단치 기준 정하기 정규분포표
mpg <- ggplot2 :: mpg
boxplot(mpg$hwy)
summary(mpg$hwy)
boxplot(mpg$hwy)$stats # 상자 그림 통계치 출력
# (아래 극단치 경계 , 1사분위, 중앙값, 3사분위, 위 극단치 경계)
# 12~ 37을 벗어나면 극단치로 분류 , NA 할당 
mpg$hwy <- ifelse(mpg$hwy < 12 | mpg$hwy > 37 , NA , mpg$hwy)
table(is.na(mpg$hwy))
mpg %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy, na.rm = T))

# 그래프 만들기 ggplot2 
# ggplot 레이어 구조 (1. 배경(축) 2. 그래프 추가 3. 설정 (축범위 ,색 ,표식..))
library(ggplot2)
#ggplot(data = , aes(x= ,y= ))
ggplot(data = mpg , aes(x = displ ,y = hwy))
#배경에 산점도 추가 geom_point() : 두 변수간 관계
ggplot(data = mpg , aes(x = displ ,y = hwy)) + geom_point()
# 축 범위 추가 
ggplot(data = mpg , aes(x = displ ,y = hwy)) + 
  geom_point() +
  xlim(3,6) +
  ylim(10,30)
# 이거랑 똑같네 ?
plot(mpg$displ, mpg$hwy,
     xlim = c(3,6),
     ylim = c(10,30))
# 막대그래프 geom_col() :집단간 차이
# 구동방식 별 평균 고속도로 연비 
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
# 똑같다
df_mpg <- df_mpg %>% arrange(desc(mean_hwy)) #내림차순
barplot(df_mpg$mean_hwy,
        xlab = "drv",
        ylab = "mean_hwy")
# 빈도 막대 그래프 geom_bar() : x 축만 지정 , 값의 개수 
ggplot(data = mpg, aes(x=drv)) +
  geom_bar()
# 똑같다 
table(mpg$drv) # 빈도표 
barplot(table(mpg$drv))
# 연속변수 지정  : 값의 분포 파악
ggplot(data = mpg, aes(x= hwy)) +
  geom_bar()
# 비슷하다 .
hist(mpg$hwy)

# 선그래프 : 시간에 따라 달라지는 데이터표현
# 시계열 그래프 (일별 환율 , 주가지수 ,,) : geom_line()
economics # 월별 미국 경제지표 
# 시간에 따른 실업자수 
ggplot(data = economics, aes(x =date, y= unemploy)) +
  geom_line()
# 시간에 따른 저축률 psavert 변화
ggplot(data = economics, aes(x =date, y= psavert)) +
  geom_line()
# 상자그림 geom_boxplot() : 데이터의 분포 (특징 이해)
# mpg의 구동방식 drv 별 , hwy 고속도로 연비 
ggplot(data = mpg, aes(x= drv, y = hwy)) +
  geom_boxplot()
