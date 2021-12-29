딕셔너리 = {
  "키A": "값A", # 키에는 문자열,숫자,불 (리스트,딕셔너리 X )
  # "문자열" 을 키로 사용 할때는 따옴표" 를 붙여주세요.
  273: [1,2,3,4],
  True: False,
 }
print(딕셔너리[True])
딕셔너리["키A"] = "값값"  
# 딕셔너리에 새로운 값 추가(변경)
print(딕셔너리["키A"])
#del 딕셔너리[키]  : 딕셔너리 요소 제거 
del 딕셔너리[True]
print(딕셔너리)
#print(딕셔너리["키"]) KeyError : 딕셔너리에 존재x 키에 접근 

print()
dictionary = {
    "name" : "7d 건조 망고 ",
    "type" : "당절임",
    "ingredient" : ["망고", " 설탕", "색소", "메타황산나트륨"],
    "origin" : "필리핀"
}
# 딕셔너리 내부에 키가 있는지 확인하기 
key = input(">접근하고자 하는 키 : ")
if key in dictionary :
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있슴")

print()
#get() 이용해서 존재하지 않는 키에 접근하는 지 확인. 
value = dictionary.get("존재하지 않는 키 ")
print("값:" ,value)
if value ==  None :
    print("존재하지 않는 키에 접근했습니다 .")

print()   
#for 반복문 사용하기 
for key in dictionary :
    print("{}:{}".format(key,dictionary[key]))

