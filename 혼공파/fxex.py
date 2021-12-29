# example = [[1,2,3],[4,[5,6]],7,[8,9]]
# -> [1,2,3,4,5,6,7,8,9]
def flatten(data):
    output =[]
    for item in data:
        if type(item) == list :
            output += flatten(item) #[1,2,3] 리스트가옴 (재귀)
        else: 
            #output.append(item)
            output +=[item] #리스트 연결 연산자
    return output
example = [[1,2,3],[4,[5,6]],7,[8,9]]
print(flatten(example))

#전체 탐색문제 (모든경우 탐색)
#1. 재귀함수 or 반복문 ?
#2. 시작조건과 종료조건
#1) 시작조건
최소사람수 =2
최대사람수 =10
전체사람수 = 100
memo={} #메모화

# 트리 : 노드에 적은값 / 엣지에 적은값
#2) 함수
def 문제(남은사람수,앉힌사람수):
    key =str([남은사람수,앉힌사람수])
    #종료조건
    if key in memo :
        return memo[key]
    if 남은사람수 < 0 :
        return 0 
    if 남은사람수 == 0 :
        return 1

    #재귀처리
    count = 0
    for i in range(앉힌사람수,최대사람수 +1):
        count += 문제(남은사람수 -i, i)
    #메모화 처리
    memo[key] = count
    return count
print(문제(전체사람수,최소사람수))