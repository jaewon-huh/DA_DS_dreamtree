# 06
library(dplyr)
exam <- read.csv("excel_exam.csv", header = T, stringsAsFactors = F)
# filter 행 추출
exam %>% filter(class %in% c(1,3,5)) #%in% 변수가 지정 조건에 해당하면 추출 
# 혼자서 해보기 
# Q1
displ4 <- mpg %>% filter(displ <= 4) 
mean(displ4$hwy)
displ5 <- mpg %>% filter(displ >= 5)
mean(displ5$hwy)
# Q2
audi <- mpg %>% filter(manufacturer == "audi")
mean(audi$cty)
toyota <- mpg %>% filter(manufacturer == "toyota")
mean(toyota$cty)
# Q3
cfh <- mpg %>% filter(manufacturer %in% c("chevrolet", "ford", "honda"))
mean(cfh$hwy)
# 혼자서 해보기 열추출
# Q1 
mpg_new <- mpg %>% select(class,cty)
head(mpg_new)
mpg_a <- mpg %>% filter(class == "suv") 
mean(mpg_a$cty)
# group_by 집단 나누기 여러변수 지정 
mpg %>% 
  group_by(manufacturer, drv) %>%  #회사별 & 구동방식 별 분리
  summarise(mean_cty = mean(cty)) %>%  #cty의 평균
  head(10)
# 혼자서 해보기 
#Q3
mpg %>% 
  group_by(manufacturer) %>% 
  summarise(mean_hwy = mean(hwy)) %>% 
  arrange(desc(mean_hwy)) %>%
  head(3)
# 가로로 합치기 left_join()
# exam + 반별 담임 교사 명단
exam
name <- data.frame(class = c(1,2,3,4,5),
                   teacher = c("kim", "lee", "park", "han", "heo"))
name
exam_new <- left_join(exam, name, by = "class")
exam_new
# 세로로 합치기 : bind_rows(a,b) , 두데이터의 변수 명이 같아야함 . 다를경우 rename()
# 혼자서 해보기 
fuel <- data.frame(fl = c("c", "d", "e", "p", "r"),
                   price_fl = c(2.34, 2.38, 2.11, 2.76, 2.22),
                   stringsAsFactors = F)
fuel # 연료별 가격 
# mpg에 d연료가격 변수 추가 
mpg_new1 <- left_join(mpg, fuel, by = "fl")
mpg_new1 %>%
  select(model, fl, price_fl) %>% 
  head(5)

# 분석 도전
library(ggplot2)
midwest <- data.frame(midwest)
# Q1 전체인구 대비 미성년 인구 백분율
midwest$perkids <- ((midwest$poptotal - midwest$popadults) / midwest$poptotal) * 100
# Q2 미성년 인구 백분율이 가장 높은 상위 5개 county의 미성년 인구 백분율
midwest %>% 
  arrange(desc(perkids)) %>%
  select(county, perkids) %>% 
  head(5)
# Q3 분류표에따라 등급변수 추가 
midwest_new <- midwest %>% mutate(grade = ifelse(perkids >= 40 , "large",
                                     ifelse(perkids >=30, "middle", "small")))
table(midwest_new$grade)
# Q4 전체 인구 대비 아시아인 인구 백분율 
midwest$percasian1 <- (midwest$popasian / midwest$poptotal) * 100
midwest %>% 
  select(state, county, percasian1) %>% 
  arrange(percasian1) %>% 
  head(10)
