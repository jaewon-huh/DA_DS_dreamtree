# list() : 텍스트 분석 결과물들은 list 형식 
# vector: 원자적 / list : 다속성, 구분 
myvector <- c(1:6, "a")
myvector
class(myvector)
 mylist <- list(1:6,"a")
mylist
# 리스트 인덱싱 
obj1 <- 1:4
obj2 <- 6:10
obj3 <- list(obj1,obj2)
obj3

mylist <- list(obj1,obj2,obj3) # [[1]] / [[2]] / [[3]] 
mylist

# 벡터 인덱싱은 [], 리스트 형식은 [[]]
# [] 리스트 반환 , [[]] : 벡터 반환 
mylist[[1]]
mylist[[1]][3]

mylist[[3]]
mylist[[3]][[1]]
mylist[[3]][[1]][[4]]
# unlist() : 라스트를 벡터로 반환 
text <- list("my", "name", "is", "R")
text
unlist(text)

# 텍스트 분석을 위한 stringr 패키지 
library(stringr)
temp <- "hello. my name is hello!"
temp
# str_extract() & str_extract_all() : 지정된 표현 추출 
str_extract(temp, "hello") # 처음 등장하는 hello
str_extract_all(temp, "hello") # 모든 hello
# str_locate() & str_locate_all() : 지정된 표현의 위치 (시작점 ~ 끝점)
str_locate(temp, "hello") # 처음 등장한 hello
str_locate_all(temp, "hello")
# str_replace() & str_replace_all() : 지정한 표현을 교체 
str_replace(temp, "hello", "HI") # 처음 등장한 것만 
str_replace_all(temp, "hello", "HI")
str_replace_all(temp, "e", "a")
str_replace_all(temp, "\\W", "") # 숫자와 알파벳 제외한 모든것 제거 
# str_split() & str_split_fixed() : 분해
str_split(temp, " ") # 공백 기준으로 분해 
str_split(temp, "\\.") # 마침표 기준 
str_split_fixed(temp, " ", 3) # 고정된 수치에 맞도록 분해 (3개로)
# str_count() : 지정된 표현의 빈도 
str_count(temp, "hello")
str_count(temp, " ")
# str_sub() : 원하는 위치의 표현을 추출 
?str_sub
hw <- "Hadley Wickham"
str_sub(hw, 1, 3) 
str_sub(hw, end = 6)
str_sub(temp, 1, 5)
# str_dup() : 지정된 표현을 반복 , 하나로 묶음 
str_dup("hello", 3)
rep("hello",3)
# str_length() : 지정된 표현의 글자수 계산 
str_length("hello")
nchar("hello")
# str_c() : 지정된 표현을 연결   
temp1 <- "hello. my name is hello!"
temp2 <- " "
temp3 <- "i'm 24 years old"
str_c(temp1, temp2, temp3)

# 유용한 정규 표현 
triplets <- c("bts", "the", "BTS", "The",
              "010", "070", ":-)", "^^;")

# 3개로 숫자로 표현된 모든 텍스트 추출
unlist(str_extract_all(triplets, "\\d{3}"))
# 1개 이상 숫자로 표현된 모든 텍스트 제외 
unlist(str_extract_all(triplets, "\\D+"))
# 1개 이상의 숫자 or 문자로 표현된 모든 텍스트 추출
unlist(str_extract_all(triplets, "\\w+"))
# 1개 이상의 숫자 or 문자로 표현된 모든 텍스트 제외
unlist(str_extract_all(triplets, "\\W+")) # 특문 
# 1개 이상의 공란으로 표현된 모든 텍스트 
unlist(str_extract_all(triplets, "\\s+"))
# 공란 제외 
unlist(str_extract_all(triplets, "\\S+"))

# 1회 이상 소문자 알파벳으로 표시된 텍스트 
unlist(str_extract_all(triplets, "[[:lower:]]+"))
# 1회 이상 대소문자 알파벳으로 표시된 텍스트
unlist(str_extract_all(triplets, "[[:alpha:]]+"))
# 1회 이상 숫자로 표시된 텍스트
unlist(str_extract_all(triplets, "[[:digit:]]+"))
# 1회 이상 구두점으로 표시된 텍스트 (쉼표,마침표)
unlist(str_extract_all(triplets, "[[:punct:]]+"))
# "^", "~" 등 특수문자를 매칭하지 않아 입력해야함 
unlist(str_extract_all(triplets, "[[:punct:]~^]+"))

# 텍스트 마이닝 
install.packages("pdftools")
install.packages("tm")
library(pdftools)
library(stringr)
library(wordcloud)
library(tm)

bts_text <- pdf_text(file.choose())
class(bts_text)
bts_text

# 전처리 
# 하나의 문장으로 
bts_string <- str_c(bts_text, collapse = " ")
# 참고문헌 삭제 5번쨰 references
str_locate_all(tolower(bts_string), "references") 
str_sub(bts_string, 91107)
# str_trunc : 삭제
bts_trunc <- str_trunc(bts_string, 91107, side = "right")
bts_trunc
# 공백 1개 이상을 공백 한개로 변경
bts_nospace <- str_replace_all(bts_trunc, "[[:space:]]{1,}", " ")
bts_nospace
# 영어가 아닌거 삭제 
bts_eng <- str_replace_all(bts_nospace, "[^[:ascii:]]{1,}", " ")
# [545] 수치 삭제 
bts_eng <- tolower(bts_eng) # 소문자로 변경 
bts_eng
bts_notice <- str_replace_all(bts_eng, "\\[[[:digit:]]+]\\ | \\([[:digit:]]+\\)", "")
bts_notice
# 기호 삭제 
bts_nopunct <- str_replace_all(bts_notice, "[[:punct:]^]+", "")
bts_nopunct
# 스페이스 삭제 
bts_nospace <- str_replace_all(bts_nopunct, "[[:space:]]{1,}", " ")
# 불용어 제거 
stopwords("en")
bts_stopwords <- removeWords(bts_nospace, stopwords("en"))
bts_stopwords

# 집계
# 단어로 쪼개기 
bts_word <- unlist(str_split(bts_stopwords, " "))
bts_word
# 빈도표 
bts_freq <- sort(table(bts_word), decreasing = T)
bts_freq
# 데이터 프레임화 
bts_df <- data.frame(bts_freq)[-1,]
head(bts_df)

# 워드 클라우드 
windows(width = 15, height = 10)
# 난수 고정 
set.seed(1234)
wordcloud(words = bts_df$bts_word, # 단어
          freq = bts_df$Freq,   # 빈도
          min.freq = 1,         # 최소 단어 빈도
          max.words = 200,      # 표현 단어 수
          random.order = F,     # 고빈도 단어 중앙 배치
          rot.per = .35,        # 회전 단어 비율
          scale = c(10,1),      # 단어 크기 범위
          colors = brewer.pal(8, "Dark2"))         # 색상 목록
