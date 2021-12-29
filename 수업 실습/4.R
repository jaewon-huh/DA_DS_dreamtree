7 / 3 #나누기
7 %/% 3 # 몫
7 %% 3 # 나머지 
7 / (3 + 4)
7 / (3 + sqrt(4)) # 7/5 sprt() : 제곱근 루트 
7 %/% (3 + sqrt(4))
7 %% (3 + sqrt(4))
x <- 7 / (3 + sqrt(4))

#행렬의 연산 
x <- matrix(1:4, 2,2)
x
x + x^2
x + 1:2   

x + 1:10 # 행렬보다 긺 , 길이 안맞음 
x + 1:3  # 결과는 뜸 , 배수 관계 x 

# 곱셈 
x * x  # x^2
x %*% x # 행렬의 곱셈 

# 연속형 변수의 변환 cut(x, breaks, labels = , ...) -> 연속형 변수를 구간으로 
?summary
?cut() 

cars <- datasets::cars # :: 패키지 안의 함수나 데이터  불러오기 
cars$speed[1:5]
summary(cars$speed) #요약 통계
cars$speed_cut <- cut(cars$speed, 
                      breaks = c(-Inf, 12, 15, 19, Inf),
                      labels = c("A", "B", "C", "D"))
cars$speed_cut
cars$speed_cut[1:5]

# 연속형 변수를 더미 변수로 변환 ifelse(조건, T , F)
cars$dist[1:5]
summary(cars$dist)
cars$dist_dummy <- ifelse(cars$dist > 42.98, "High", "Low")
cars$dist_dummy[1:5]

# 파생 변수의 추가
exam <- read.csv("excel_exam.csv", header = T)
exam$total <- exam$math + exam$english + exam$science
head(exam)
exam$mean <- round(exam$total / 3, digits = 1) # 소수점 첫째까지만
head(exam)
# 직관적 transform(x, ) # 데이터의 열을 생 %>% 성 or 수정 
exam <- transform(exam,
                  total_new = (math + english + science))
head(exam)

install.packages("dplyr")
library(dplyr)
# rename()
exam <- read.csv("excel_exam.csv", header = T)
names(exam)
exam <- rename(exam,
               "ID" = "id",
               "Class" = "class",
               "Math" = "math",
               "English" = "english",
               "Science" = "science")
names(exam)

#filter() : 행 추출  
?filter
exam <- read.csv("excel_exam.csv", header = T)
exam <- filter(exam, class == 1)

# %>% , 파이프 (연결)연산자 , 객체 중복 입력 최소화 
# 단축키 Ctrl +Shift + M
exam %>% filter(class == 1) 
# and & , or ㅣ
exam <- read.csv("excel_exam.csv", header = T)
exam %>% filter(class ==1 & math >=50)
exam %>% filter(math >= 90 | science >= 90)

#select() : 열 추출 
exam <- read.csv("excel_exam.csv", header = T)
exam %>% select(math) %>% head(5)
exam %>% select(math : science) %>% head(5)

# filter() 와 select() 함수 조합 
exam %>% 
  filter(class == 1) %>% 
  select(english)

# arrange(x, , by_group = F) : 데이터 정렬 
?arrange()
exam %>% 
  arrange(math) %>% # math 기준 오름차순 min
  head(3)
exam %>% 
  arrange(desc(math)) %>% # math 기준 내림차순 max
  head(3)

# exam <- arrange(exam, math) , 이렇게 하면 원본데이터가 변화 
exam %>% 
  arrange(class) 
# mutate() : 파생변수 추가 = $변수명, transform()
exam <- read.csv("excel_exam.csv", header = T)
exam %>% 
  mutate(total = math + english + science) %>%
  head()
head(exam) #원래 데이터에는 영향 x 

exam %>% 
  mutate(total = math + english + science,
         mean = total / 3) %>%
  head()

exam %>% 
  mutate(total = math + english + science,
         mean = total / 3,
         result = ifelse(mean >= 60 , "P", "F")) %>%
  head()

exam %>%  
  mutate(total = math + english + science) %>%
  arrange(total) %>% 
  head()

# group_by() : 그룹화 분리 , summarise() : 그룹별 요약
exam %>% summarise(mean_math = mean(math)) # 수학점수 평균

exam %>% 
  group_by(class) %>%  # 클래스 별 그룹화 
  summarise(mean_math = mean(math))

exam %>% 
  group_by(class) %>% 
  summarise(mean_math = mean(math),
            sum_math = sum(math),
            median_math = median(math),
            n = n())
  
#left_join() : 가로로 합치기 , bind_rows() : 세로로 합치기 
?left_join
# 중간고사와 기말고사 데이터 합치기 
set.seed(1234) # 똑같은 수치 생성 
exam1 <- data.frame(id = c(1:5),
                    midterm1 = sample(80:100, 5))
exam2 <- data.frame(id = c(1:5),
                    midterm2 = sample(80:100, 5)) # id가 동일 
exam1
exam2
exam_join <- left_join(exam1, exam2, by= "id")
exam_join

# 세로로 합치기 : 한 열로 
?bind_rows
set.seed(1234)
group1 <- data.frame(id = c(1:3),
                     midterm = sample(80:100, 3))
group2 <- data.frame(id = c(4:6),
                     midterm = sample(80:100, 3))
exam_bind <- bind_rows(group1, group2)
exam_bind

