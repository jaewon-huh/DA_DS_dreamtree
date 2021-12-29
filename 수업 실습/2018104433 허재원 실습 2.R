# 수출통계 
export <- read.csv("kor_export_top5.csv", header = T, stringsAsFactors = F)
# 수입통계
import <- read.csv("kor_import_top5.csv", header = T, stringsAsFactors = F)
library(dplyr)
# 1-1
names(export) # 12번째
names(import) # 12번째
# 1-2 
# 수출, 수입액 따로 평균에 따라 구하는 것으로 문제를 이해했습니다. 
summary(export$Export.Value)
export$mean_value_e <- ifelse(export$Export.Value > 6.301e+10 , 1, 0)
summary(import$Import.Value)
import$mean_value_i <- ifelse(import$Import.Value > 4.348e+10 , 1, 0)

# 1-3
trade <- left_join(export, import, by= "No") %>%
         select(-ends_with(".y"))
trade
# 1-4
trade <- rename(trade,
                "no" = "No",
                "classification" = "Classification.x",
                "year" = "Year.x",  
                "reporter_code" = "Reporter.Code.x",
                "reporter" = "Reporter.x",
                "reporter_iso" = "Reporter.ISO.x",
                "partner_code" = "Partner.Code.x",
                "partner" = "Partner.x", 
                "partner_iso" = "Partner.ISO.x" ,
                "commodity_code" = "Commodity.Code.x",
                "commodity" = "Commodity.x",
                "export" = "Export.Value",
                "import" = "Import.Value")
# 1-5
trade <- transform(trade,
                   trade_value1 = (export + import))
# 1-6
trade <- trade %>% 
  mutate(trade_value2 = export + import)
# 1-7
trade_chn <- trade %>% filter(partner == "China") %>%
                       select(partner, trade_value1)
#중국과의 교역량만 보여주기 위해 select() 함수를 사용하였습니다.         
summary(trade_chn) 
# 1-8
trade_chn$trade_level <- cut(trade_chn$trade_value1,
                   breaks = c(-Inf, 2.274e+11, 2.400e+11, 2.434e+11, Inf ),
                   labels = c("A", "B", "C", "D"))
trade_chn$trade_level
# 1-9
trade %>% 
  group_by(partner) %>% 
  summarise(mean_value = mean(trade_value1))
# 1-10
trade %>% 
  group_by(year) %>% 
  summarise(mean_value = mean(trade_value1),
            mean_export = mean(export),
            mean_import = mean(import))

# 2-1 
mpg <- read.csv("mpg.csv", header= T, stringsAsFactors = F)
# 2-2
mpg %>%
  filter(displ <= 4) %>% 
  summarise(mean_hwy = mean(hwy)) 
mpg %>%
  filter(displ >= 5)  %>% 
  summarise(mean_hwy = mean(hwy))
# displ 4 이하인 자동차의 hwy 평균이 더 높음.
# 2-3
mpg %>%
  filter(manufacturer == "audi") %>% 
  summarise(mean_cty = mean(cty))
mpg %>%
  filter(manufacturer == "toyota") %>% 
  summarise(mean_cty = mean(cty))
# toyota 사의 평균 cty 가 더 높음 
# 2-4 
# 문제에서 추출한 3사의 데이터를 따로 새로운 데이터로 만들라는 언급이 없어서, 바로 3사 hwy 평균을 구했습니다.
mpg %>% 
  filter(manufacturer == "chevrolet" 
         | manufacturer == "ford" 
         | manufacturer == "honda") %>% 
  summarise(mean_hwy = mean(hwy))
# 2-5 
mpg_new = select(mpg, c(class,cty))
# 2-6
# 두 차종의 '평균 cty'를 비교하라 로 이해하였습니다.
mpg_new %>%
  filter(class == "suv") %>% 
  summarise(mean_cty = mean(cty))
mpg_new %>%
  filter(class == "compact") %>% 
  summarise(mean_cty = mean(cty))
# compact 차종의 평균 cty 가 20.12766으로 더 높습니다.
# 2-7
mpg %>% 
  filter(manufacturer == "audi") %>% 
  arrange(desc(hwy)) %>% 
  head(5)
# 2-8
# 원본 mpg에 total과 mean을 추가하라는 언급이 없어 %>% mutate 로 조건에 해당하는 데이터만 출력하였습니다.
mpg %>% 
  mutate(total = cty + hwy,
         mean = total / 2) %>% 
  arrange(desc(mean)) %>% 
  head(3)
# 만약 원본 mpg에 total과 mean 변수를 추가한 후 평균연비가 높은 3종의 데이터를 구한다면,
mpg <- mpg %>% 
  mutate(total = cty + hwy,
         mean = total / 2)
mpg %>% arrange(desc(mean)) %>% 
  head(3)
# 2-9
mpg %>% 
  group_by(class) %>% 
  summarise(mean_cty = mean(cty)) %>% 
  arrange(desc(mean_cty))
# 2-10
mpg %>% 
  group_by(manufacturer) %>% 
  filter(class == "compact") %>% 
  summarise(n= n()) %>% 
  arrange(desc(n))

