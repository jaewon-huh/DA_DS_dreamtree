# 텍스트 마이닝 
# 패키지 설치 
install.packages("rJava")
install.packages("memoise")
install.packages("KoNLP")
library(KoNLP)

extractNoun('인하대학교 공학대학원 블록체인 전공입니다.')
useNIADic()
# 데이터 불러오기 
txt <- readLines("hiphop.txt")
head(txt)
# 특수문자 제거 
library(stringr) # 문자 처리 패키지 
?str_remove_all
txt <- str_replace_all(txt, "\\W", " ") # \\W : 특수문자
# str_replace_all(대상 , 바꿀거 , 뭐로 바꾸는지)
head(txt)
# 명사 추출 
extractNoun("대한민국의 영토는 한반도와 그 부속도서로 한다")
# 힙합 가사 명사 추출 & 빈도표 
nouns <- extractNoun(txt)
nouns
# 리스트인 nouns를 빈도테이블로
wordcount <- table(unlist(nouns)) 
wordcount
# 데이터 프레임으로
df_word <- as.data.frame(wordcount, stringsAsFactors = F) 
library(dplyr)
df_word <- rename(df_word,
                  word = Var1,
                  freq = Freq)
# 자주 사용된 단어 빈도표 
# 두글자 이상 단어 
df_word <- filter(df_word, nchar(word) >= 2)
top_20 <- df_word %>% 
  arrange(desc(freq)) %>% 
  head(20)
top_20

#워드 클라우드 만들기 
install.packages("wordcloud")
library(wordcloud)
library(RColorBrewer)
# 단어 색상 목록 만들기
?brewer.pal
pal <- brewer.pal(8, "Dark2")
# 난수 고정 set.seed()
set.seed(1234)
# 워드 클라우드 만들기 
wordcloud(words = df_word$word, # 단어
          freq = df_word$freq,  # 빈도
          min.freq = 2,         # 최소 단어 빈도
          max.words = 200,      # 표현 단어 수
          random.order = F,     # 고빈도 단어 중앙 배치
          rot.per = .1,         # 회전 단어 비율
          scale = c(4,0.3),     # 단어 크기 범위
          colors = pal)         # 색상 목록
# 단어 색상 바꾸기 
pal <- brewer.pal(9,"Blues")[5:9]
set.seed(1234)
wordcloud(words = df_word$word, # 단어
          freq = df_word$freq,  # 빈도
          min.freq = 2,         # 최소 단어 빈도
          max.words = 200,      # 표현 단어 수
          random.order = F,     # 고빈도 단어 중앙 배치
          rot.per = .1,         # 회전 단어 비율
          scale = c(4,0.3),     # 단어 크기 범위
          colors = pal)         # 

# 국정원 트윗 텍스트 마이닝 
# 데이터 준비 
twitter <- read.csv("twitter.csv",
                    header = T,
                    stringsAsFactors = F,
                    fileEncoding = "UTF-8")
# 변수명 수정 & 특수문자 제거 
twitter <- rename(twitter,
                  no = 번호 ,
                  id = 계정이름 ,
                  date = 작성일 ,
                  tw = 내용)
twitter$tw <- str_replace_all(twitter$tw, "\\W", " ")
head(twitter$tw)

# 명사 추출 & 빈도표 
nouns <- extractNoun(twitter$tw)
wordcount <- table(unlist(nouns))  # 리스트 제거 , table
df_word <- as.data.frame(wordcount, stringsAsFactors = F)
df_word <- rename(df_word,
                  word = Var1,
                  freq = Freq)
# 두글자 이상 단어 만 추출 
df_word <- filter(df_word, nchar(word) >= 2)
top_20 <- df_word %>% 
  arrange(desc(freq)) %>% 
  head(20)
top_20
# 단어 빈도 막대 그래프 
library(ggplot2)
order <- arrange(top_20, freq)$word # 빈도 순서 변수 

ggplot(data = top_20, aes(x= word, y = freq)) +
  geom_col() +
  ylim(0,2500) +
  coord_flip() +
  scale_x_discrete(limit = order) + # x축 빈도순 정렬 
  geom_text(aes(label = freq), hjust = -0.3) # 라벨링
?geom_text # 라벨링 
# hjust : 수평자리 맞추기 vjust : 수직 자리 맞추기 0 = 왼쪽정렬 ,1 = 오른쪽
# 워드 클라우드 
pal <- brewer.pal(8, "Dark2")
set.seed(1234)
wordcloud(words = df_word$word, # 단어
          freq = df_word$freq,  # 빈도
          min.freq = 2,         # 최소 단어 빈도
          max.words = 200,      # 표현 단어 수
          random.order = F,     # 고빈도 단어 중앙 배치
          rot.per = .1,         # 회전 단어 비율
          scale = c(6,0.2),     # 단어 크기 범위
          colors = pal)         # 
