# foreign 패키지 : 통계분석 소프트 웨어 파일 사용 
install.packages("foreign")
install.packages("readxl")
library(foreign)
library(dplyr)   # 전처리
library(ggplot2) # 시각화
library(readxl)  # 엑셀 파일 불러오기 
# 데이터 불러오기 : 한국 복지 패널  
raw_welfare <- read.spss(file = "Koweps_hpc10_2015_beta1.sav",
                         to.data.frame = T) # 데이터를 df 형태로 
welfare <- raw_welfare # 복사본
# 데이터 검토 
head(welfare)
dim(welfare)
# 변수명 바꾸기 
welfare <- rename(welfare,
                  sex = h10_g3,            # 성별
                  birth = h10_g4,         # 출생 년도
                  marriage = h10_g10,     # 혼인 상태
                  religion = h10_g11,     # 종교
                  income = p1002_8aq1,    # 월급
                  code_job = h10_eco9,    # 직업 코드
                  code_region = h10_reg7) # 지역 코드

# 성별에 따른 월급차이 

# 변수 검토 및 전처리 
class(welfare$sex)
table(welfare$sex)
# 이상치 결측 처리 
welfare$sex <- ifelse(welfare$sex == 9 , NA , welfare$sex)
table(is.na(welfare$sex))
# 값 수정 
welfare$sex <- ifelse(welfare$sex == 1, "male", "female")
table(welfare$sex)
qplot(welfare$sex)
# 월급 변수 전처리 
summary(welfare$income) # 평균 241.6 중앙값 192,5 결측치 12030개 
qplot(welfare$income) + xlim(0,1000)
# 결측치 9999 & 월급 0원 -> 결측처리 
welfare$income <- ifelse(welfare$income == 9999 | welfare$income == 0 ,
                         NA, welfare$income)
table(is.na(welfare$income))
# 관계 분석 
sex_income <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(sex) %>% 
  summarise(mean_income = mean(income))
sex_income # 남 평균 임금 312만 / 여 163만 
# 그래프
ggplot(data = sex_income, aes(x = sex, y = mean_income)) +
  geom_col()

# 나이와 월급의 관계 

# 나이 전처리 (birth만 나와있음. )
summary(welfare$birth) # 1907생 ~ 2014 생 
welfare$birth <- ifelse(welfare$birth == 9999 , NA, welfare$birth)
# 파생변수 만들기 2015년 기준이므로 2015 - 출생년 + 1  = 나이 
welfare$age <- 2015 - welfare$birth + 1  
summary(welfare$age) # 2살 ~ 109살  
qplot(welfare$age)
# 관계 분석 
age_income <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age) %>% 
  summarise(mean_income = mean(income))
age_income
# 그래프 
ggplot(data = age_income, aes(x = age, y = mean_income)) + 
  geom_line()
# 연령대 별 월급 분석 

# 연령대 변수 만들기 
welfare <- welfare %>% 
  mutate(ageg = ifelse(age < 30 , "young",
                       ifelse (age < 60 , "middle", "old")))
table(welfare$ageg)
qplot(welfare$ageg)
# 관계 분석 
ageg_income <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(ageg) %>% 
  summarise(mean_income = mean(income))
ageg_income
ggplot(data = ageg_income, aes(x = ageg, y = mean_income)) +
  geom_col() +
  scale_x_discrete(limits = c("young", "middle", "old")) # 범주 순서 지정 

# 연령대 및 성별 월급 차이 : 성별 월급차이가 연령대 별로 다른가 ?
# x = ageg, y = sex_income 
sex_income <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(ageg, sex) %>% 
  summarise(mean_income = mean(income))
sex_income
# 그래프 
# fill = sex : 성별에 따라 다른값으로 표현되도록 
ggplot(data = sex_income, aes(x = ageg, y = mean_income, fill = sex)) +
  geom_col() +
  scale_x_discrete(limits = c("young", "middle", "old"))
# 막대 그룹화 : geom_col(position = "dodge)
ggplot(data = sex_income, aes(x = ageg, y = mean_income, fill = sex)) +
  geom_col(position = "dodge") +
  scale_x_discrete(limits = c("young", "middle", "old"))

# barplot() , beside = T 를  이용해 똑같이 만들기 

# 나이 및 성별 월급 차이 분석하기 
sex_age <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age,sex) %>% 
  summarise(mean_income = mean(income))
# 선그래프 , 성별에 따라 다른 색 col = sex
ggplot(data = sex_age, aes(x=age, y = mean_income , col = sex)) +
  geom_line()

# 직업별 월급 차이 
# 직업 변수 전처리 
table(welfare$code_job) # 직업 코드라 무엇이 어떤 직업을 의미하는지 모름 
list_job <- read_excel("Koweps_Codebook.xlsx", col_names = T, sheet = 2)
# col_names = T : 열 이름 가져오기
head(list_job) # 변수 2개 코드 & 직업명
dim(list_job) # 직업 149개
# 원본에 결합 
welfare <- left_join(welfare, list_job, by = "code_job")
welfare %>% 
  filter(!is.na(code_job)) %>% 
  select(code_job, job) %>% 
  head(5)
# 직업 별 월급 평균 
job_income <- welfare %>% 
  filter(!is.na(job) & !is.na(income)) %>% 
  group_by(job) %>% 
  summarise(mean_income = mean(income))
head(job_income)
# 직업별 월급 내림차순 정렬
top10 <- job_income %>% 
  arrange(desc(mean_income)) %>%
  head(10)
top10
# 그래프 : 크기 순 정렬 reorder(x, 기준변수),옆으로 눕힌 그래프 
ggplot(data = top10, aes(x = reorder(job, mean_income), y = mean_income)) +
  geom_col() +
  coord_flip() # 수평을 수직으로 , 수직을 수평으로
# 하위 10 월급
bottom10 <- job_income %>%
  arrange(mean_income) %>% 
  head(10)
bottom10
ggplot(data = bottom10, aes(x = reorder(job, -mean_income), y = mean_income)) +
  geom_col() +
  coord_flip() + # 수평을 수직으로 , 수직을 수평으로
  ylim(0,850) # top 10과 비교되도록 y축 설정
# barplot() & horiz = T로 구현 ?

# 성별에 따른 직업 빈도 : 남- 직업 / 여 - 직업
job_male <- welfare %>% 
  filter(!is.na(job) & sex == "male") %>% 
  group_by(job) %>% 
  summarise(n = n()) %>%  # job 별 남자수 
  arrange(desc(n)) %>% 
  head(10)
job_male
job_female <- welfare %>% 
  filter(!is.na(job) & sex == "female") %>% 
  group_by(job) %>% 
  summarise(n = n()) %>%  # job 별 여자수 
  arrange(desc(n)) %>% 
  head(10)
job_female
# 그래프 
# 남자 직업 빈도 
ggplot(data = job_male, aes(x = reorder(job, n), y = n)) +
  geom_col() +
  coord_flip() 
# 여자 
ggplot(data = job_female, aes(x = reorder(job, n), y = n)) +
  geom_col() +
  coord_flip() 
# geom_bar() : 원자료를 이용해 막대 그래프 / geom_col() : 요약표 (group, summarise)

# 종교 유무에 따른 이혼율 
table(welfare$religion)
# 1 = 종교 있음 , 2 = 없음 
welfare$religion <- ifelse(welfare$religion == 1 , "yes", "no")
table(welfare$religion)
qplot(welfare$religion)
# 결혼 
table(welfare$marriage) # 1 = 유배우 / 3 = 이혼 
# 파생변수 : 이혼 여부 
welfare$group_marriage <- ifelse(welfare$marriage == 1 , "marriage",
                                 ifelse(welfare$marriage == 3, "divorce", NA))
table(welfare$group_marriage)
table(is.na(welfare$group_marriage)) # 결측치 7521개 결혼 x 
qplot(welfare$group_marriage)
# 종교 유무에 따른 이혼율 분석 
religion_marriage <- welfare %>% 
  filter(!is.na(group_marriage)) %>%  # 결혼 안한 놈들 제외 
  group_by(religion, group_marriage) %>% 
  summarise(n = n()) %>% 
  mutate(tot_group = sum(n)) %>% 
  mutate(pct = round(n/tot_group * 100 , 1)) # 종교 집단 별 비율 
religion_marriage
# 집단별 빈도 구하는 함수 count()
religion_marriage <- welfare %>% 
  filter(!is.na(group_marriage)) %>% 
  count(religion, group_marriage) %>%  # 빈도 분석 n
  group_by(religion) %>%  # 종교로 나눔
  mutate(pct = round(n/sum(n) * 100, 1)) # pct =  이혼 or 결혼 /종교여부
religion_marriage
# 이혼율 표 구하기 
divorce <- religion_marriage %>%
  filter(group_marriage == "divorce") %>% 
  select(religion, pct)
divorce # 이혼율 종교 o 7.2 % , 종교 x 8.3 %
ggplot(data = divorce , aes(x = religion, y =pct)) +
  geom_col() # 대상이 전체 대상임 ,

# 연령대 및 종교 유무에 따른 이혼율 분석 

# 연령대별 이혼율 표 
ageg_marriage <- welfare %>% 
  filter(!is.na(group_marriage)) %>% 
  count(ageg, group_marriage) %>% 
  group_by(ageg) %>%
  mutate(pct = round(n/sum(n) * 100, 1))

ageg_marriage  
# 초년 제외 & 이혼율만 
ageg_marriage <- ageg_marriage %>% 
  filter(ageg != "young" & group_marriage == "divorce") %>% 
  select(ageg, pct)
ageg_marriage #  중년 8.9% 이혼 / 노년 6.6 이혼
# 그래프 
ggplot(data = ageg_marriage, aes(x = ageg , y = pct)) +
  geom_col()
# 종교 유무에 따른 이혼율 차이가 연령대 별로 다른가 ?
# 연령대 , 종교, 결혼상태 별 분석
ageg_religion_marriage <- welfare %>% 
  filter(!is.na(group_marriage) & ageg != "young") %>% # 결혼안한놈들 & 초년 제외  
  count(ageg, religion, group_marriage) %>% 
  group_by(ageg, religion) %>% # 연령대와 종교 유무로 그룹화 (연령대= & 종교 = 가 한그룹) 
  mutate(pct = round(n/sum(n)* 100, 1))
ageg_religion_marriage
# 이혼한 사람만
df_divorce <- ageg_religion_marriage %>% 
  filter(group_marriage == "divorce") %>% 
  select(ageg, religion, pct)
df_divorce
# 그래프 
ggplot(data = df_divorce, aes(x = ageg, y = pct, fill = religion)) +
  geom_col(position = "dodge")
# 종교에 따라 색 다르게 & 막대 그룹화 
# 중년층 종교 o 이혼율이 1.8 % 더 낮고 , 노년층은 종교 o 이혼율이 0.1% 더 높다.

# 지역별 연령대 비율 - 노년층이 많은 지역은 어디 ?
# 지역 변수 
table(welfare$code_region) # 1~ 7 이름 모름 
# 지역명 변수 추가 
list_region <- data.frame(code_region = c(1:7),
                          region = c("서울",
                                     "수도권(인천/경기)",
                                     "부산/경남/울산",
                                     "대구/경북",
                                     "대전/충남",
                                     "강원/충북",
                                     "광주/전남/전북/제주"))
list_region
# 원본에 지역명 변수 추가 
welfare <- left_join(welfare, list_region, by = "code_region")
welfare %>% 
  select(code_region, region) %>% 
  head()

# 지역별 연령대 비율표 
region_ageg <- welfare %>% 
  count(region, ageg) %>%
  group_by(region) %>% # 지역별 그룹화 
  mutate(pct = round(n/sum(n) * 100, 2))
region_ageg  # 강원 초/중/노
# 그래프 만들기 
ggplot(data = region_ageg, aes(x = region, y = pct, fill = ageg)) +
  geom_col() + # 막대 분류화는 필요 x
  coord_flip() # 옆으로 눕혀 비교 쉽게 

# 노년층이 많은 순으로 그래프 정렬 
list_order_old <- region_ageg %>% 
  filter(ageg == "old") %>% 
  arrange(pct)  # 노년층 비율 순으로 지역명이 정렬된 변수 (오름차순)
# 지역명 순서 만 추출
order <- list_order_old$region
order

ggplot(data = region_ageg, aes(x = region, y = pct, fill = ageg)) +
  geom_col() + # 막대 분류화는 필요 x
  coord_flip() + # 옆으로 눕혀 비교 쉽게 
  scale_x_discrete(limits = order) # x축을 order 순으로 재정렬

# 연령대 순으로 막대 색 나열 
# fill = 파라미터에 지정할 변수 ageg 의 범주(levels) 순서를 지정 
class(region_ageg$ageg) # chr
# factor로 변환하고 범주 레벨 지정 
region_ageg$ageg <- factor(region_ageg$ageg,
                           levels = c("old", "middle", "young"))
class(region_ageg$ageg)

ggplot(data = region_ageg, aes(x = region, y = pct, fill = ageg)) +
  geom_col() + # 막대 분류화는 필요 x
  coord_flip() + # 옆으로 눕혀 비교 쉽게 
  scale_x_discrete(limits = order) # x축을 order 순으로 재정렬
