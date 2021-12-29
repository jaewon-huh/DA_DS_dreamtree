# 5장 
# deck에 점수 시스템 설정 
deck <- read.csv("card.csv", header = T)
deck2 <- deck
# 제자리에서 값 변경
vec <- c(0,0,0,0,0,0)
vec
vec[1] <-1000
vec
vec[c(1,3,5)] <- c(1,1,1)
vec
vec[7] <- 0
vec
deck2$new <- 1:52
deck2
deck2$new <- NULL # 열 삭제 
head(deck2)
#ace의 값을 14로 수정 
deck2[c(13,26,39,52),] # ace 호출 
deck2$value[c(13,26,39,52)] <- 14
deck2$value[c(13,26,39,52)]

#논리 서브세팅 : 논리 연산자 > == !=
1 > c(0,1,2) 
1 %in% c(2,3,4) # A %in% B : A 가 B에 들어 있는가 
c(1,2,3,4) %in% c(3,4,5,6) # A가 벡터라면 독립적으로 테스트 
# deck2의 face 열 추출 , 각 값들이 ace와 같은지 
deck2$face == "ace"
sum(deck2$face =="ace")
# 섞인 카드뭉치에서 ace 확인 
shuffle <- function(cards){
  random <- sample(1:52,52)
  cards[random,]
}
deck3 <-shuffle(deck)

deck3$value[deck3$face == "ace"] # ace 카드들의 value 값들 
deck3$value[deck3$face == "ace"] <- 14
head(deck3)
# 하트 게임 (하트& 스페이드 제외 모든 카드 0의값)
deck4 <-deck
deck4$value <- 0
head(deck4,13)
# 하트는 1의 값
deck4$value[deck4$suit =="hearts"] <- 1
deck4
#스페이드 퀸은 13점 
queenOfSpades <- deck4$suit == "spades" & deck4$face == "queen"
deck4$value[queenOfSpades] <- 13
deck4[queenOfSpades,]
#참고 행 추출 deck %>% filter(suit == "hearts" & face == "queen")
# 불린 연산자 boolean : (&,|, xor, !, any, all)
w <- c(-1,0,1)
x <- c(5,15)
y <- "February"
z <- c("Monday", "Tuesday", "Friday")
w > 0
x > 10 & x < 20 # 10 < x & x < 20
y == "February"
all(z %in%  c("Monday", "Tuesday", "Wednesday", "Thursday" ,"Friday",
                "Saturday", "Sunday")) 
# 블랙잭 ( 카드의 숫자 = 카드의 점수, KQJ =10 ,에이스는 11 or 1)
deck5 <- deck
head(deck5)
facecard <- deck5$face %in% c("king", "queen", "jack")
deck5[facecard,] #face card 인 행들 출력
deck5$value[facecard] <- 10 
head(deck5, 13) # ace 빼고 완료 , ace는 특정 조건에 따라 값 !=
# ace에 결측값 NA (값을 모른다. 현재는 지정 x)
mean(c(NA, 1: 50))
mean(c(NA, 1: 50), na.rm = T) # na.rm = NA remove 무시 
vec <- c(1,2,3, NA)
is.na(vec) # 어떤 값이 NA인지 확인 
deck5$value[deck5$face == "ace"] <- NA 
head(deck5,13)
