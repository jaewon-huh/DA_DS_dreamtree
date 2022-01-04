# 산점도 scatter : 두 변수 사이의 관계 (연속 값)


import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default') # 스타일 서식

df = pd.read_csv('예제/part4/auto-mpg.csv', header= None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# x축 weight / y축 mpg - scatter

df.plot(kind='scatter', x = 'weight', y = 'mpg',
        c='blue', s=10, figsize= (10,5))
# c - color , s - size
plt.title('Scatter plot - mpg vs weight')
plt.show()


# 버블차트 : 점의 크기의 변화를 줌 
# cylinders 개수의 상대적 비율 비율을 계산해 시리즈 생성
cylinders_size = df.cylinders / df.cylinders.max() * 300  
# 왜 300을 곱하지 : 0~ 1 size 너무 작아서 안보임 따라서 size를 키움 
print(cylinders_size)

# 3개의 변수로 산점도 - cylinders_size를  s옵션엥 지정 
df.plot(kind ='scatter', x= 'weight', y ='mpg',
        c= 'red', figsize =(10,5),
        s = cylinders_size, alpha =0.3)
plt.title('Scatter plot : mpg - weight - cylinders')
plt.show()

# 그림파일로 저장 : plt.savefig('경로/파일이름.png')