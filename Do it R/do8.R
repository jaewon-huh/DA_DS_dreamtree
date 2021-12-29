# 통계적 가설 검정 
# t검정 - 두 집단의 평균 비교 t.test()
# compact 자동차와 suv 자동차의 도시연비 cty t검정.
mpg <- as.data.frame(ggplot2 ::mpg)
head(mpg)
# class 와 cty만 남기고 추출 
library(dplyr) # 전처리 
mpg_diff <- mpg %>%
  select(class, cty) %>% 
  filter(class %in% c("compact", "suv"))
head(mpg_diff)  
table(mpg_diff$class)
# t 검정 
?t.test
t.test(data = mpg_diff, cty ~ class, var.equal = T)
# compact cty 평균 20 / suv cty 평균 13.5  & p-value : 유의

# 일반 휘발유와 고급휘발유의 도시연비 t 검정 
mpg_diff2 <- mpg %>% 
  select(fl, cty) %>% 
  filter(fl %in% c("r", "p")) # r : regular , p: premium
table(mpg_diff2$fl)
t.test(data = mpg_diff2, cty ~ fl , var.equal = T)
# p- value = 0.28 > 0.05 , 유의 x  우연히 발생했을 가능성 큼 

# 상관분석 - 두 변수의 관계성 분석  
# cor.test : 상관계수 0 ~ 1 , + 정비례, - 반비례
# 실업자 수와 개인 소비 지출의 상관관계 
economics <- as.data.frame(ggplot2 :: economics)
cor.test(economics$unemploy, economics$pce)
# 상관계수 0.61 : 정비례 관계 

# 여러변수의 관련성 -> 상관 행렬 cor()
head(mtcars)
car_cor <- cor(mtcars)
round(car_cor, 2)
# mpg & cyl -0.85  : 연비 높을수록 실린더 개수 적다.
# 상관행렬 히트맵
install.packages("corrplot")
library(corrplot)
corrplot(car_cor)
# 상관계수 클수록 원 크고 색 진함 / + : 파랑 , - : 빨강 
corrplot(car_cor, method = "number") # 수로 표현 파라미터 
# 다양한 파라미터 지정 
# colorRampPalette() : 입력한 색 보관 팔레트 
colorRampPalette(c("red", "blue"))(5) # 빨 ,파 사이를 5등분
col <- colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", 
                          "#77AADD", "#4477AA"))
corrplot(car_cor,
         method = "color",        # 색깔로 표현
         col = col(200),          # 색 200개 선정
         type = "lower",          # 왼쪽 아래 행렬만 표시
         order = "hclust",        # 유사한 상관계수끼리 군집화
         addCoef.col = "black",   # 상관계수 색깔
         tl.col = "black",        # 변수명 색깔
         tl.srt = 45,             # 변수명 45도 기울임
         diag = F)                # 대각 행렬 제외 



corrplot(car_cor,
         method = "color",        # 색깔로 표현
         addCoef.col = "black")   # 상관계수 색깔
