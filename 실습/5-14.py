# 시계열 데이터 만들기 
# Timestamp 배열 : date_range() 함수
# 파이썬 range() 로 숫자배열 만드는 것 유사 
import pandas as pd 
# 배열 생성 
# 월 초 
ts_ms = pd.date_range(start = '2019-01-01', # 날짜 시작일
                      end= None,            # 범위 끝
                      periods= 6,           # timestamp 개수
                      freq= 'MS',           # 시간 간격 (월초)
                      tz= 'Asia/Seoul')     # 시간대 
print(ts_ms)
print('\n')
# 월 마지막
ts_me = pd.date_range(start = '2019-01-01', # 날짜 시작일
                      end= None,            # 범위 끝
                      periods= 6,           # timestamp 개수
                      freq= 'M',            # 시간 간격 (월말)
                      tz= 'Asia/Seoul')     # 시간대 
print(ts_me)
print('\n')
# 분기 (3개월) 간격 , 월 말 
ts_3m = pd.date_range(start = '2019-01-01', # 날짜 시작일
                      end= None,            # 범위 끝
                      periods= 6,           # timestamp 개수
                      freq= '3M',            # 시간 간격 (3개월 말)
                      tz= 'Asia/Seoul')     # 시간대 
print(ts_3m)