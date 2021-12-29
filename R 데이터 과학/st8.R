# 반복문 : 프로그래밍 시뮬레이션 
# 기대값 : 일종의 가중치가 적용된 평균값 
die <- c(1,2,3,4,5,6)
score <- function(symbols) {
  # 조건 확인
  same <- symbols[1] == symbols[2] && symbols[2] == symbols[3]
  bars <- symbols %in% c("B", "BB", "BBB")
  # 상금 계산 
  if (same) {
    payouts <- c("DD" = 100, "7" = 80, "BBB" = 40, "BB" = 25, "B" = 10, 
                 "C" = 10, "0" = 0)
    prize <- unname(payouts[symbols[1]])
  } else if (all(bars)) {
    prize <- 5
  } else {
    cherries <- sum(symbols =="C")
    prize <- c(0,2,5)[cherries + 1]
  }
  # 다이아 개수를 센다 
  diamonds <- sum(symbols == "DD")
  # 다이아 개수만큼 상금을 두배로 한다 
  prize * 2^diamonds
}
score(symbols)
symbols
# expand.grid : n 벡터 원소들의 모든 조합을 구한다.
rolls <- expand.grid(die,die) # 주사위 2쌍 , 36가지 조합 1.
rolls$value <- rolls$Var1 + rolls$Var2 # 주사위의 합 2.
head(rolls,3)
# 각 조합의 일어날 확률 
prob <- c("1" = 1/8 , "2" = 1/8 , "3" = 1/8, "4" = 1/8 , "5" = 1/8 , "6" = 3/8 )
prob
prob[rolls$Var1]
rolls$prob1 <- prob[rolls$Var1]
head(rolls, 3)
rolls$prob2 <- prob[rolls$Var2]
head(rolls, 3)
# 조합의 확률 3.
rolls$prob <- rolls$prob1 * rolls$prob2
head(rolls , 3)
# 기대값 sum(2. * 3. : 결과값 * 그 확률)
sum(rolls$value * rolls$prob)

# 상금에 대한 기대값 
# 1.  슬롯머신의 모든 결과값 . 세 심벌의 모든 조합 
wheel <- c("DD", "7", "BBB", "BB", "B", "C", "0")
combos <- expand.grid(wheel, wheel, wheel, stringsAsFactors = F)
head(combos)
# 2. 각 조합이 나올 확률 
prob = c("DD" = 0.03, "7" = 0.03, "BBB" = 0.06, "BB" = 0.1, 
         "B" = 0.25, "C" = 0.01, "0" = 0.52)
combos$prob1 <- prob[combos$Var1]
combos$prob2 <- prob[combos$Var2]
combos$prob3 <- prob[combos$Var3] # 15
# 조합의 확률 
combos$prob <- combos$prob1 * combos$prob2 * combos$prob3
sum(combos$prob)
# 3. 각 상금 계산 score()
# for 문 : for(value in that) { this } 
# that 객체는 객체의 집합(숫자 or 문자열 벡터) , value는 인수 
for (value in c("My", "first", "for", "loop")) {
  print("one run")
}
for (value in c("My", "second", "for", "loop")) {
  print(value)
}  
# for문은 출력을 저장하지 않음. 출력을 따로 작성하도록 루프 작성 
chars <- vector(length = 4)

words <- c("My", "third", "for", "loop")
for (i in 1:4) {
  chars[i] = words[i]
}
chars # 결과를 벡터나 리스트에 저장하기 위해 for문 사용
# 상금을 계산하기 위한 for 문 
combos$prize <- NA
head(combos, 3)
# combos 객체의 343개 행에 score 함수를 실행.
# 매 루프는 combos i번째 행의 첫 3가지 원소를 이용해 score 함수 실행.
# score함수 결과는 combos$prize의 i번째 원소에 저장
for (i in 1:nrow(combos)) {
  symbols <-c(combos[i,1], combos[i,2], combos[i,3])
  combos$prize[i] <- score(symbols)
}
head(combos)

# 기대값 계산 
sum(combos$prob * combos$prize) # 슬롯머신의 배당률 

# 와일드카드 DD : DD는 치환가능 & 상금 두개  B DD B -> BBB $ DD = 20$
# 와일드 카드를 고려한 score 계산

score <-  function(symbols){
  
  diamonds <- sum(symbols == "DD")
  cherries <- sum(symbols == "C")

  # 조건에 따라 어떤 경우에 해당하는지 
  # 다이아몬드는 와일드 카드이므로 , 다이아가 아닌 것들만
  # 모양이 모두 같은 경우 or 모두 바 모양인 경우  
  slots <- symbols[symbols != "DD"]
  same <- length(unique(slots)) == 1 # 고유값이 하나 
  bars <- slots %in% c("B", "BB", "BBB")
  
  # 상금 할당 
  if (diamonds == 3){ # DD DD DDD
    prize <- 100
  } else if (same) {
    payouts <- c("7" = 80, "BBB" = 40, "BB" = 25,
                "B" = 10, "C" = 10, "0" = 0)
    prize <- unname(payouts[slots[1]]) # 상금만 표시 
  } else if (all(bars)) {
    prize <- 5
  } else if (cherries > 0) {
    # 체리가 하나 이상 있으면,
    # 다이아몬드를 체리로 계산한다.
    prize <- c(0,2,5)[cherries + diamonds + 1]
  } else {
    prize <- 0
  }
  # 다이아몬드의 두배를 한다 .
  prize * 2^diamonds
}  
# 새 combos$prize 수정 
for (i in 1:nrow(combos)) {
  symbols <-c(combos[i,1], combos[i,2], combos[i,3])
  combos$prize[i] <- score(symbols)
}
head(combos)
sum(combos$prob * combos$prize)

get_symbols <- function(){
  wheel <- c("DD", "7", "BBB", "BB", "B", "C", "0")
  sample(wheel, size = 3, replace = T,
         prob = c(0.03, 0.03, 0.06, 0.1, 0.25, 0.01, 0.52))
}
play <- function(){
  symbols <- get_symbols()
  structure(score(symbols), symbols  = symbols)
}
play()

# while 문 while (조건) { 코드 }
# 파산할 때까지 슬롯머신 
plays_till_broke <- function(start_with){
  cash <- start_with
  n <- 0
  while (cash > 0) {
    cash <- cash -1 + play()
    n <- n + 1
  }
  n
}
plays_till_broke(100)
# repeat문 : 명령으로 멈추지 않는 한 계속 반복 
plays_till_broke <- function(start_with){
  cash <- start_with
  n <- 0
  repeat {
    cash <- cash -1 + play()
    n <- n + 1
    if (cash <= 0) {
      break
    }  #cash가 -가 되도 계속하니까 
  }
  n
}
plays_till_broke(100)
