# math = __import__("math")
import math
# 수학 = __import__("math")
import math as 수학
print(math.pi)
print(수학.pi)

#from import 구문 : 모듈에 있는걸 그냥 사용
from math import pi, sin
print(pi ,sin(10))
#from import * 구문 : 모듈이 가지고 있는 모든 기능 가져옴
from math import *
print(pi ,sin(10))