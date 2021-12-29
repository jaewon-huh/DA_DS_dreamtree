# deck 생김 , 카드섞기 , 한 장씩 분배 -> 개별 값 
# deck[ 행, 열] R의 인덱싱은 1부터 시작 
deck <- read.csv("card.csv", header = T)
deck[1,1]
deck[1,]
deck[,2] # 2열을 벡터로 리턴 
deck[,2, drop = F] # 데이터 프레임으로 받기 
deck[-1,]
deck[-(2:52), ]
# 논리형 인덱싱 : 벡터의 길이가 추출하기 원하는 인덱스의 길이와 같아야 함 
deck[1, c(T,T,F)]
# 이름
deck[1, c("face","suit", "value")]
deck[, "value"]
# 첫행을 돌려주는 코드
deal <- function(cards){
  cards[1,]
}
deal(deck) # 계속 맨 윗장 카드만 줌, 복원
# 카드 섞기 : deck의 행들의 순서 재배치 
deck2 <- deck[1:52,]
head(deck2)
deck3 <- deck[c(2,1,3:52),] # 1행과 2행 순서 바꾸기 
head(deck3)
# 1: 52 를 랜덤하게 정렬후 , 인덱스의 행으로 
random <- sample(1:52,52)
random
deck4 <-deck[random, ]
head(deck4)
# shuffle 함수
shuffle <- function(cards){
  random <- sample(1:52,52)
  cards[random,]
}

shuffle(deck)
deal(deck)
deck2 <- shuffle(deck) #섞고서
deal(deck2) # 윗장주기

# 달러 $와 이중괄호 
deck$value # value열 벡터로 리턴 
mean(deck$value)
median(deck$value)
# 리스트에 $표기 
lst <- list(numbers = c(1,2) , logical= T , strings = c("a", "b", "c"))
lst
lst[1] # 리스트를 리턴,원소는 벡터지만
sum(lst[1])
lst$numbers #list$원소 -> 원자 리턴
sum(lst$numbers) # 바로 함수 활용 ㄱㄴ
lst[[1]] # 이중괄호 : 부분 리스트 안의 원소 값 리턴
lst["numbers"]
lst[["numbers"]]

