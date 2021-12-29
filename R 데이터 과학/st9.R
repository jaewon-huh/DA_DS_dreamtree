#  코드 벡터화 : 입력으로 벡터를 받고 벡터의 각 값을 동시에 다룸 
#  절대값 함수 ex1
abs_loop <- function(vec) {
  for (i in 1:length(vec)) {
    if (vec[i] < 0) {
      vec[i] = -vec[i]
    }
  }
  vec
}
abs_loop(c(-1,2,-3))
# ex2 
abs_set <- function(vec){
  negs <- vec < 0
  vec[negs] <- vec[negs] * -1 # 음수 값만 골라서 절대값
  vec
}

# 처리 속도 비교 
long <- rep(c(-1,1), 5000000)
system.time(abs_loop(long))
system.time(abs_set(long))
system.time(abs(long)) # 절대값 구하는 함수 abs()

# 벡터화 
change_vec <- function(vec) {
  vec[vec == "DD"] <- "joker"
  vec[vec == "C"] <- "ace"
  vec[vec == "7"] <- "kingr"
  vec[vec == "B"] <- "queen"
  vec[vec == "BB"] <- "jack"
  vec[vec == "BBB"] <- "ten"
  vec[vec == "0"] <- "nine"

  vec
}
vec <- c("DD", "C", "7", "B", "BB", "BBB", "0")
change_vec(vec)
many <- rep(vec,1000000)
system.time(change_vec(many))
# 검색테이블 사용 
change_vec2 <- function(vec) {
  tb <- c("DD" = "joker", "C" = "ace", "7" = "king", "B" = "queen",
          "BB" = "jack", "BBB" = "ten", "0" = "nine")
  unname(tb[vec])
}
change_vec2(vec)
system.time(change_vec2(many))

# for문의 속도를 개선하는법 
system.time({
  output <-rep(NA, 1000000) # 값을 저장하는 객체의 크기 백만
  for (i in 1:1000000) {
    output[i] <- i + 1
  }
})
system.time({
  output <-NA
  for (i in 1:1000000) {
    output[i] <- i + 1
  }
})

# 실전에서 코드 벡터화 
# 실제로 슬롯머신 시행을 통한 배당률 계산
play <- function(){
  symbols <- get_symbols()
  structure(score(symbols), symbols  = symbols)
}
play()

winnings <- vector(length = 1000000)
for (i in 1:1000000) {
  winnings[i] <- play()
}
mean(winnings)
# 벡터화
get_symbols <- function(){
  wheel <- c("DD", "7", "BBB", "BB", "B", "C", "0")
  sample(wheel, size = 3, replace = T,
         prob = c(0.03, 0.03, 0.06, 0.1, 0.25, 0.01, 0.52))
}
get_symbols()
# n개의 슬롯조합 , n * 3 행렬 형태로 작성률
get_many_symbols <- function(n) {
  wheel <- c("DD", "7", "BBB", "BB", "B", "C", "0")
  vec <- sample(wheel, size = 3* n, replace = T,
         prob = c(0.03, 0.03, 0.06, 0.1, 0.25, 0.01, 0.52))
  matrix(vec, ncol = 3)
}
get_many_symbols(4)
# play함수도
play_many <- function(n){
  symb_mat <- get_many_symbols(n = n)
  data.frame(w1 = symb_mat[,1], w2 = symb_mat[,2],
             w3 = symb_mat[,3], prize = score_many(symb_mat))
}
plays <- play_many(10000000)
mean(plays$prize) # 배당률

# score_many함수가 필요 : score 함수의 벡터화 버전 n*3 행렬에 n개에 상금 
# rowSums() : 헹의 합 계산 
# 아래 symbols로 score_many 함수 연구 
symbols <- matrix(
  c("DD", "DD", "DD",
    "C", "DD", "0",
    "B", "B", "B",
    "B", "BB", "BBB",
    "C", "C", "0",
    "7", "DD", "DD",
    "7", "DD", "7",
    "DD", "B", "BBB"), nrow = 8, byrow = T)
symbols
# symbols는 각 심벌을 열로저장한 행렬

score_many <- function(symbols){
  # 1단계 : 체리와 다이아를 가지고 기본상금 구하기 
  ## 열마다 체리와 다이아 개수 확인 
  cherries <- rowSums(symbols == "C") 
  diamonds <- rowSums(symbols == "DD")
  ### 와일드 카드로 사용된 다이아몬드를 체리로 취급
  prize <-c(0,2,5)[cherries + diamonds + 1]
  # but C & DD 가 둘다 있어야 됨 , C가 없으면 상금 취소 
  # (cherries 객체는 0일때 False로 강제 변환)
  prize[!cherries] <- 0

  # 2단계 : 심벌이 모두 같은 종류 일때, 상금을 조정 
  same <- symbols[,1] == symbols [,2] & 
    symbols [,2] == symbols[,3] 
  payoffs <- c("DD" = 100, "7" = 80, "BBB" = 40, "BB" = 25,
               "B" = 10, "C" = 10, "0" = 0)
  prize[same] <- payoffs[symbols[same,1]]
  
  # 3단계 : 심벌이 모두 바 모양 
  bars <- symbols == "B" | symbols == "BB" | symbols == "BBB" 
  all_bars <- bars[,1] & bars[,2] & bars[,3] & !same
  prize[all_bars] <- 5
  
  # 4단계 : 와일드카드 고려 
  ## 와일드 카드가 두개 ( * DD DD) -> same * & 곱 4
  two_wilds <- diamonds == 2
  
  ### 와일드 카드가 아닌 심벌을 확인
  one <- two_wilds & symbols[,1] != symbols[,2] &
    symbols[,2] == symbols[,3]
  two <- two_wilds & symbols[,1] != symbols[,2] &
    symbols[,1] == symbols[,3]
  three <- two_wilds & symbols[,1] == symbols[,2] &
    symbols[,2] != symbols[,3]
  ### 모두 같은 모양을 가진 것으로 취급.
  prize[one] <- payoffs[symbols[one,1]]
  prize[two] <- payoffs[symbols[two,2]]
  prize[three] <- payoffs[symbols[three,3]]
  
  ## 와일드 카드가 한개 (ex) 7 DD 0  -> 0 / 7 DD 7 -> 80 * 2 
  one_wild <- diamonds == 1
  
  ### 모두 바 모양인 것으로 취급 (경우에 따라 B DD BBB)
  wild_bars <- one_wild & (rowSums(bars) == 2)
  prize[wild_bars] <- 5 
  ### 모두 같은 모양으로 취급 (경우 따라 7 DD 7)
  one <- one_wild & symbols[,1] == symbols[,2] 
  two <- one_wild & symbols[,2] == symbols[,3]
  three <- one_wild & symbols[,3] == symbols[,1] 
  prize[one] <- payoffs[symbols[one,1]]
  prize[two] <- payoffs[symbols[two,2]]
  prize[three] <- payoffs[symbols[three,3]]
  
  # 5단계 다이아 몬드의 개수만큼 두배 
  unname(prize * 2^diamonds)
}
score_many(symbols)
# 1단계 
cherries <- rowSums(symbols == "C") 
cherries
diamonds <- rowSums(symbols == "DD")
diamonds

prize <- c(0,2,5)[cherries + diamonds + 1]
prize
prize[!cherries] <- 0
prize

# 2단계 : 심벌이 모두 같은 종류 일때, 상금을 조정 
same <- symbols[,1] == symbols [,2] & 
  symbols [,2] == symbols[,3] 
payoffs <- c("DD" = 100, "7" = 80, "BBB" = 40, "BB" = 25,
             "B" = 10, "C" = 10, "0" = 0)
prize[same] <- payoffs[symbols[same,1]]
# symbols[same인 열, 1째줄(원소)] payoffs["DD"] & payoffs["B"]
prize # same 조건이었던 상금들은 바뀜

# 3단계 
bars <- symbols == "B" | symbols == "BB" | symbols == "BBB" 
bars
all_bars <- bars[,1] & bars[,2] & bars[,3] & !same 
# 첫 줄 T (bars) & 두째 T & 셋째 T & 다 같진 않음 
all_bars
prize[all_bars] <- 5
prize

# 4단계 : 와일드카드 고려 

## 와일드 카드가 두개 
two_wilds <- diamonds == 2
### 와일드 카드가 아닌 심벌을 확인
one <- two_wilds & symbols[,1] != symbols[,2] &
  symbols[,2] == symbols[,3]
two <- two_wilds & symbols[,1] != symbols[,2] &
  symbols[,1] == symbols[,3]
three <- two_wilds & symbols[,1] == symbols[,2] &
  symbols[,2] != symbols[,3]
### 모두 같은 모양을 가진 것으로 취급.
prize[one] <- payoffs[symbols[one,1]]   # 심볼 중 * DD DD 인 행의 첫째줄 즉, * payoffs
prize[two] <- payoffs[symbols[two,2]]   # DD 7 DD
prize[three] <- payoffs[symbols[three,3]] # DD DD 7
prize # (7 DD 7 & DD B BBB) 는 0 인상황 & DD 곱하기 x 

## 와일드 카드가 한개 (ex) 7 DD 0  -> 0 / 7 DD 7 -> 80 * 2 
one_wild <- diamonds == 1

### 모두 바 모양인 것으로 취급 (경우에 따라 B DD BBB)
wild_bars <- one_wild & (rowSums(bars) == 2)
prize[wild_bars] <- 5 

### 모두 같은 모양으로 취급 (경우 따라 7 DD 7)
one <- one_wild & symbols[,1] == symbols[,2] 
two <- one_wild & symbols[,2] == symbols[,3]
three <- one_wild & symbols[,3] == symbols[,1] 
prize[one] <- payoffs[symbols[one,1]]
prize[two] <- payoffs[symbols[two,2]]
prize[three] <- payoffs[symbols[three,3]]

prize

unname(prize * 2^diamonds)
