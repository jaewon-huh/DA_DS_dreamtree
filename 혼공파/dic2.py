pets = [
    {"name" : "구름", "age" :  5},
    {"name" : "초코", "age" :  3},
    {"name" : "아지", "age" :  1},
    {"name" : "뭉이", "age" :  1}
]
print("#우리동네 애완동물들 ")
for pet in pets :   
    print("{} {}살".format(pet["name"],pet["age"]))
numbers = [1,2,6,8,4,3,2,2,1,3,3,7,4,5,1,3,2,3,1,5,6]
counter = {}
for number in numbers :
    if number in counter:
        counter[number] += 1
    else :
        counter[number] = 1
print(counter)
    #{1:1}
    #{2:1}
    #{6:1} ... {2: 2}
character = {
    "name" : "기사",
    "level" : 12,   
    "items" : {
        "sword" :"불꽃검",
        "armor" :"풀플레이트",
         },
    "skill" : ["베기","세게 베기","아주 세게 베기 "]
        }
# 반복문 사용 
for key in character : 
    if type(character[key] ) is dict : # "key" : {}
        for item in character[key] :   # 그 안의 {}속의 key -item 반복문
            print("{} :{}".format(item,character[key][item]))  #
    elif type(character[key] ) is list :
        for s in character[key] :    # s = [] 안의 element  
            print("{} : {}".format(key,s))
    else :
        print("{} : {}".format(key,character[key]))