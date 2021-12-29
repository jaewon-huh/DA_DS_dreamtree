# min(), max(), sum () : 매개변수로 리스트 
a = [273,103,52,32,54]
print(list(enumerate(a)))
for i, element in enumerate(a) :
    print("{}번째 요소는 {}입니다.".format(i,element)) 
b = {
    "키a":"값a",
    "키b":"값b",
    "키c":"값c", 
}
print(b.items()) 
for key,value in b.items():
    print("{}:{}".format(key,value))  
    
array = []
for i in range(0,20,2):
    array.append(i*i)
print(array)
#리스트 내포 사용 : 리스트 이름 = [표현식 for 반복자 in 반복할수 있는것 + if 조건문] 
array_1 = [i*i for i in range(0,20,2)]
print(array_1)
array_2 = [i for i in range(10) if i % 2 == 0 ]
print(array_2)

#ex2 1~100 사이 숫자중(range) 2진수로 변환했을때 0이 하나만 포함된 숫자(조건문)를 찾고, 그 숫자들의 합을 구하여라 
output = [i for i in range(1,101) if "{:b}".format(i).count("0")==1] 
for i in output:
    print("{} : {}".format(i,"{:b}".format(i)))
print("합계:",sum(output))