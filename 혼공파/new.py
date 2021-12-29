example_dictionary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C",
}
# 딕셔너리와 items()함수
print("items():", example_dictionary.items())
# dict_items([('키A', '값A'), ('키B', '값B'), ('키C', '값C')])
# for 반복문과 items() 함수
for key, element in example_dictionary.items() :
    print("dictionary[{}] = {}".format(key,element))