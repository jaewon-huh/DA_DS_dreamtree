# 벡터의 요약 및 집계
# 데이터 요약 (기술 통계량)
x <- 1: 100
mean(x)
length(x)
range(x) # 범위 (최대&최소값)
sd(x) # 표준편차 
summary(x)
y <- summary(x)
# 인덱싱 조회 가능
y[1]
y[1:3]
y[c(3,4)]
# summary() 에 다양한 유형의 객체 사용 가능 , 객체 유형에 따라 다른 결과 
letters # 알파벳
summary(letters) # 문자형 벡터 
summary(list(a = 1:5, b = letters[1:5]))  # 리스트 
summary(factor(c("cat","cat","cat","dog")))

# table() : 범주형 데이터 요약 (빈도요약,도수분포표)
?table()
library(ggplot2)
mpg <- ggplot2 :: mpg
table(mpg$manufacturer) # 제조사 빈도분포 
table(mpg$manufacturer)[1:4] 
table(mpg$class) #차종
table(mpg$class)[1:4]
# 두개 이상의 범주형 데이터 
table(mpg$manufacturer, mpg$class)[1:4, 1:4]
# 비율 확인 
?apply # apply(x, 1 : 행기준, 2: 열 기준 , sum)
tb <- table(mpg$manufacturer, mpg$class)
tb[1:4,1:4]
tb / apply(tb, 1, sum)
round(tb/apply(tb, 1, sum), 2)[1:4,1:4]

# 데이터 프레임과 리스트 요약 및 집계
# 데이터 프레임 구조 파악
nrow(mpg) # 행 개수 
ncol(mpg) # 열 개수 
dim(mpg)  # 행과 열 동시에 
head(mpg[,1:5]) # 6 X 5
str(mpg) # 행과열 ,각 변수들의 데이터 타입입

# 데이터 프레임 요약  (평균)
mean(mpg$displ)
mean(mpg$cyl)
mean(mpg$cty)
mean(mpg$hwy)
# apply(x : df or array , margin (1,2), FUN : 적용할 함수)
m <- matrix(1:9, ncol =3)
m
apply(m, 1, sum)
apply(m, 2, sum)
# mpg 데이터의 배기량, 실린더 개수 , 도시연비 , 고속도로 연비의 평균을 계산 
apply(mpg[,c("displ", "cyl", "cty", "hwy")], 2, mean) 
# x는 array, df에서 따라서 지정 

# 각 값의 최대 최소값의 차이를 계산 
maxmin <- function(x){
  max(x) - min(x)
} # 차이를 계산하는 함수 생성  
apply(mpg[,c("displ", "cyl", "cty", "hwy")], 2, maxmin)

# 데이터프레임 집계 
# aggregate() 하나의 변수를 기준으로 요약, 그룹별 연산 
# aggregate(formula : 연산대상 ~ 기준이 되는 열 , data : 전체 df, Fun)
?aggregate()
# 자동차 종류 "suv" 와 "pickup" 의 배기량(displ) 평균 계산 
mean(mpg$displ[mpg$class == "suv"])
mean(mpg$displ[mpg$class == "pickup"])

# 차종 class에 따른 배기량 displ 평균 
aggregate(mpg$displ, list(class = mpg$class), mean) # 방법1 df.frame
aggregate(displ ~ class, mpg, mean) # 방법2 : formula
# 제조 회사별(manufacturer) 도시연비(cty) 평균 계산 
aggregate(cty ~ manufacturer, mpg, mean)
# 차종(class)과 생산연도(year) 별로 분류 , 도시연비(cty) 평균 계산  (기준 2)
agg_mpg<- aggregate(cty ~ class + year, mpg, mean)
head(agg_mpg)

# 차종별 배기량 평균 계산 , 막대그래프로 확인 
class_dpl <- aggregate(displ ~ class, mpg, mean)
barplot(class_dpl$displ,
        names.arg = class_dpl$class,
        xlab = "Class",
        ylab = "Displ",
        ylim = c(0, 10),
        main = "Average of displ by class"
          )

# 리스트 요약 lapply() : list+apply, lapply(list, FUN)
lapply(as.list(mpg[,c(3,5,8,9)]), mean) # 출력이 리스트의 형식 

# 요인 변수의 집계 (범주형)
# tapply(vector : 연산대상 벡터 , index : 분류기준 (그룹지표), FUN)
# 연료 종류별(fl) 도시연비(cty)의 평균 
tapply(mpg$cty, mpg$fl , mean)
barplot(tapply(mpg$cty, mpg$fl , mean))
        