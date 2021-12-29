# 6장 R 환경 시스템 
deck <- read.csv("card.csv", header = T)
deal <- function(cards){
  cards[1,]
}
deal(deck) 
# deal 함수가 같은 카드(맨 윗장)만 나눠줌
shuffle <- function(cards){
  random <- sample(1:52,52)
  cards[random,]
}

shuffle(deck)
# 실제로 섞는것 x , 섞인 deck의 복사본 리턴 

# R 환경 시스템 (부모환경, 계층구조) parenvs(all = TRUE)
as.environment("package:stats") 
globalenv() #전역환경
baseenv() # 기본환경
emptyenv() # 빈 환경 
parent.env(globalenv()) # parent.env() 부모환경 확인 
ls(globalenv()) # ls() : 객체 이름 리턴 , ls.str() 각 객체의 구조
# $ 사용해 객체 불러오기 
head(globalenv()$deck, 3)
# 환경에 객체 저장 assign("객체이름", 새 객체 값, envir = 저장할 환경)
# assign 은 <-와 비슷하게 작동 , 바로 덮어씀 
assign('new', "Hello Global", envir = globalenv())
globalenv()$new

# 동작 환경 : 일반적 전역환경 (작업공간)
environment() #현재 동작환경
# 스코핑 규칙 : R이 객체를 찾는 특별한 규칙 (전역환경 -> 부모환경)
# 할당 : 객체에 값 할당 -> 그 값을 동작 환경 내 객체 이름에 저장 
new
new <- "Hello active" # 이전 객체 덮어쓰기 
# 실행 : R은 함수를 실행할 때마다 새로운 환경을 만들고, 복귀 (런타임 환경)
show_env <- function(){
  a <- 1
  b <- 2
  c <- 3
  list(ran.in = environment(),
       parent = parent.env(environment()),
       objects = ls.str(environment()))
}
show_env()
deal <-function(){
  deck[1,]
}
deal() # 스코핑 규칙으로 deck 찾음
environment(deal) # deal의 근원환경은 전역환경
# 맨 위카드 삭제 
DECK <- deck
deck <- deck[-1,]
head(deck)
deal <- function(){
  card <- deck[1,]
  deck <- deck[-1,]
  card
}
deal() # deck <-dekc[-1.] 시행 할때 런타임 환경 (전역 환경이 아닌 런타임 환경에 deck<- deck[-1,] 저장)
# deck[-1,]을 전역환경의 객체에 할당 
deal <- function(){
  card <- deck[1,]
  assign("deck", deck[-1,], envir = globalenv())
  card
}
deal()
environment(deal)
# 셔플 
shuffle <- function(cards){
  random <- sample(1:52,52)
  cards[random,]
}
head(deck,3) # deck의 복사본, 나눠준 카드는 없음
# 전역 환경에 살아있는 deck 을 원본 DECK의 섞인 버전으로 대체 
shuffle <-function(){
  random <- sample(1:52,52)
  assign("deck", DECK[random,], envir = globalenv())
}
shuffle()
deal()
# 클로저 
# deck이 바뀌거나 지워지지 않게 안전한 곳에 저장(복사본)
setup <- function(deck){
  DECK <- deck
  
  DEAL <- function(){
    card <- deck[1,]
    assign("deck", deck[-1,], envir = globalenv())
    card
  }
  SHUFFLE <-function(){
    random <- sample(1:52, 52)
    assign("deck", DECK[random,], envir = globalenv())
  }
  
  list(deal = DEAL, shuffle = SHUFFLE)
}

# deal 과 shuffle 함수의 근원환경이 전역환경이 아닌 setup 런타임 환경 
environment(deal)
environment(shuffle)
environment(setup)
# deal과 shuffle 여전히 전역환경에서 deck 업데이트 
setup <- function(deck){
  DECK <- deck
  
  DEAL <- function(){
    card <- deck[1,]
    assign("deck", deck[-1,], envir = parent.env(environment()))
    card
  }
  SHUFFLE <-function(){
    random <- sample(1:52, 52)
    assign("deck", DECK[random,], envir = parent.env(environment()))
  }
  
  list(deal = DEAL, shuffle = SHUFFLE)
}
# 부모 환경을 참조하도록 바꿈

cards <- setup(deck)
deal <- cards$deal
shuffle <- cards$shuffle

rm(deck)
shuffle()
deal()

