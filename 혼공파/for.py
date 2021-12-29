a = [1,2,3,4,5]

for element in a:
    print(element) 
numbers = [273,103,5,32,65,9,72,800,]
#holzzak = ["짝수","홀수"]
#for number in numbers :
     #print("{}는 {}".format(number,holzzak[number%2]))
for number in numbers :
    if number >= 100 :
         print("- 100 이상의수 : " ,number)
for number in numbers :
     if number %2 == 0 :
         print("짝수입니다 : " ,number)
     else:
         print("홀수입니다 :", number)
for number in numbers :
     if len(str(number)) == 3 :
         print("세자릿수 : " ,number)
     elif len(str(number)) == 2 :
         print("두 자릿수 : " ,number)
     else:
         print("한 자리수 : ", number)
for number in numbers :
    if len(str(number)) ==3 : 
        print("{} 자리수 {}".format(len(str(number)), number))
    elif len(str(number)) == 2 :
        print("{} 자리수 {}".format(len(str(number)), number))
    else:
        print("{} 자리수 {}".format(len(str(number)), number))
list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]   
for a in list_of_list :
    # [1,2,3]>>[4,5,6,7]>>[8,9]
    for b in a:
    # 1,2,3 // 4,5,6,7 // 8,9   
        print(b)
