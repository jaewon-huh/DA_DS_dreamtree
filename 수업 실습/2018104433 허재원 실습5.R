library(pdftools)
library(stringr)
library(wordcloud)
library(tm)

trade_text <- pdf_text(file.choose())
class(trade_text)

# 전처리 
# 하나의 문장으로 연결
trade_string <- str_c(trade_text, collapse = " ")
# 참고문헌 삭제 3번째 references
str_locate_all(tolower(trade_string), "references")
str_sub(trade_string, 65771)
trade_trunc <- str_trunc(trade_string, 65771, side = "right")
trade_trunc
# 공백 통일 
trade_nospace <- str_replace_all(trade_trunc, "[[:space:]]{1,}", " ")
trade_nospace
# 영문 아닌 문자 삭제 
trade_eng <- str_replace_all(trade_nospace, "[^[:ascii:]]{1,}", " ")
# [545] 등 괄호 수치 삭제 
trade_eng <- tolower(trade_eng) # 소문자로 변경 
trade_eng
trade_notice <- str_replace_all(trade_eng, "\\[[[:digit:]]+]\\ | \\([[:digit:]]+\\)", "")
trade_notice
# 기호 삭제 
trade_nopunct <- str_replace_all(trade_notice, "[[:punct:]^]+", "")
trade_nopunct
# 숫자 삭제 (단어만 남기려고 숫자는 지웠습니다!)
trade_nonum <- str_replace_all(trade_nopunct, "[[:digit:]]+", "")
trade_nonum
# 스페이스 삭제 
trade_nospace <- str_replace_all(trade_nonum, "[[:space:]]{1,}", " ")
# 불용어 제거 
stopwords("en")
trade_stopwords <- removeWords(trade_nospace, stopwords("en"))
trade_stopwords

# 집계 
# 단어별로 쪼개기 
trade_word <- unlist(str_split(trade_stopwords, " "))
trade_word
# 빈도표 
trade_freq <- sort(table(trade_word), decreasing = T)
trade_freq
# 데이터 프레임화 
trade_df <- data.frame(trade_freq)[-1,]
head(trade_df)
# 변수 이름 수정 
library(dplyr)
trade_df <- rename(trade_df,
                  word = trade_word)
head(trade_df)

# 워드 클라우드 
windows(width = 15, height = 10)
# 난수 고정 
set.seed(1234)
wordcloud(words = trade_df$word,  # 단어
          freq = trade_df$Freq,   # 빈도
          min.freq = 1,           # 최소 단어 빈도
          max.words = 200,        # 표현 단어 수
          random.order = F,       # 고빈도 단어 중앙 배치
          rot.per = .35,          # 회전 단어 비율
          scale = c(10,1),        # 단어 크기 범위
          colors = brewer.pal(8, "Dark2"))         # 색상 목록
