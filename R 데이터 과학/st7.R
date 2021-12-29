play()
one_play <-play()
one_play # 객체에 저장하고 나면 심벌 출력 x 
# S3 시스템 : R에서 사용하는 클래스 시스템 
num <- 1000000000
print(num)
class(num) <-c("POSIXct", "POSIXt") # 시간
print(num)
# 속성 
deck <- read.csv("card.csv", header = T)
attributes(deck) # attribute() : 객체의 속성 보기 
# 속성 값 수정 or 새로 부여 o 
row.names(deck) <- 101: 152
levels(deck) <- c("level 1", "level 2", "level 3")
attributes(deck)
# 객체에 속성 추가 or 속성값 보기 attr
attributes(one_play)
attr(one_play, "symbols") <- c("B", 0, "B")
attributes(one_play)
attr(one_play, "symbols")
one_play
one_play +1 # 객체의 속성은 일반적으로 무시 

# symbols에 심벌 정보가 저장된 상금을 돌려주도록 
play <- function(){
  symbols <- get_symbols()
  prize <- score(symbols) # one_play 와 동일
  attr(prize,"symbols") <- symbols # 18줄
  prize
}
play()
two_play <- play()
two_play

# structure() : 한번에 ,입력한 속성을 갖는 객체를 생성 ,  1. 객체, 2. 객체에 추가할 속성의 이름
?structure
play <- function(){
  symbols <- get_symbols()
  structure(score(symbols), symbols  = symbols)
}
three_play <- play()
three_play

# 속성을 검색하고 사용할 함수를 작성 
slot_display <- function(prize){
  
  # symbols 속성을 추출
  symbols <- attr(prize, "symbols") # "B" "0" "C"
  
  # symbols 벡터를 하나의 문자열로 합친다.
  symbols <- paste(symbols, collapse = " ") # "B 0 C"

  # symbols 을 정규 표현식으로 prize와 결합한다.
  #\n 은 줄바꿈을 의미하는 정규 표현식
  string <- paste(symbols,prize, sep = "\n$")
  
  # 콘솔에서 결과를 따옴표 없이 표시한다
  cat(string)
}

paste(c("a","b","c"),c("A","B","C"),sep="+",collapse="@")

paste("B", "0" , "C", collapse = " ") # 50 
paste("B 0 C", 0, sep = "\n$") # 55
cat("B 0 C\n$0") #결과

slot_display(one_play)
slot_display(play())

# 제네릭 함수 : 경우에 따라 다른 일을 할수 있음. -> if?
# print() : 콘솔 창에서 객체를 표시할때 , 제네릭함수 
# print()가 slot_display() 처럼 표시하도록 , 다른 객체일때는 원래 print()
print
#UseMethod  : 첫번째 인수에 제공한 입력의 클래스 검사 , 이 클래스를 다루기 위해 지정된 새함수에 인수를 넘겨줌 
# 메서드 : 서로 다른 클래스에서 서로다른 작업을 하도록 print를 관리 

# 슬롯머신 출력 형식 바꾸기 : 출력에 맞는 클래스 , 해당 클래스를 위한 print 메서드 

class(one_play) <- "slots" # one_play 객체에 클래스 지정 
#slots 클래스를 위한 S3 메서드 작성 (print.slots)
print.slots <- function(x, ...){
  cat("print.slots 메서드를 사용하고 있습니다.")
}
print(one_play)
rm(print.slots)
# slots 클래스를 위한 print 메서드 작성 
print.slots <- function(x, ...){
  slot_display(x)
}
one_play
# 결과가 slots 클래스 속성을 갖도록 play() 수정
play <- function(){
  symbols <- get_symbols()
  structure(score(symbols), symbols  = symbols, class = "slots")
}
class(play())
play()
attributes(play)
# R은 벡터안에 객체를 넣기 위해 , 객체를 추출할때 속성을 버린다.
play1 <-play()
c(play()) 
play1[1]

