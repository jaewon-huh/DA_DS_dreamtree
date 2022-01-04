# 시계열 데이터 만들기 
# Period 배열 : pd.period_range() 함수
import pandas as pd 
# period 배열 - 1개월 
pr_m = pd.period_range(start='2019-01-01',
                       end = None,
                       periods= 3,
                       freq= 'M')
print(pr_m) # 전체 기간을 나타냄  1월  / 2월 
print('\n')
# 한시간 길이 
pr_h = pd.period_range(start='2019-01-01',
                       end = None,
                       periods= 3,
                       freq= 'H')
print(pr_h)  
print('\n')
# 두 시간 길이 
pr_2h = pd.period_range(start='2019-01-01',
                       end = None,
                       periods= 3,
                       freq= '2H')
print(pr_2h)  