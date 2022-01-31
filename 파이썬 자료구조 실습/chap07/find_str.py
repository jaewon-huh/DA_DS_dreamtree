# 파이썬 연산자와 표준 라이브러리로 문자열 검색 

# 문자열에 포함되어 있는 문자열을 검색(find 계열 함수）

# str.find(문자) : str안에서 문자가 포함되있으면 그 중 가장 작은 인덱스 반환 
# str.rfind(문자) : 뒤에서 찾음 



txt = input('문자열 txt: ')  # 문자열 나열
ptn = input('문자열 ptn: ')  # 검색할 문자

c = txt.count(ptn)

if c == 0:                                                  # 포함된 문자가 없음
    print('ptn은 txt에 포함되어 있지 않습니다.')
elif c == 1:                                                # 포함된 문자가 １개만 있는 경우
    print('ptn이 txt에 포함되어 있는 인덱스: ', txt.find(ptn))
else:                                                       # 포함된 문자가 2개 이상 있는 경우
    print('ptn이 txt에 포함되어 있는 맨 앞 인덱스: ', txt.find(ptn))
    print('ptn이 txt에 포함되어 있는 맨 끝 인덱스: ', txt.rfind(ptn))

# 문자열에 포함되어 있는 문자열을 검색(index 계열 함수)

txt = input('문자열 txt: ')
ptn = input('문자열 ptn: ')

c = txt.count(ptn)

if c == 0:                                                  # 포함된 문자가 없음
    print('ptn은 txt에 포함되어 있지 않습니다.')
elif c == 1:                                                # 포함된 문자가 １개만 있는 경우
    print('ptn이 txt에 포함되어 있는 인덱스: ', txt.index(ptn))
else:                                                       # 포함된 문자가 2개 이상 있는 경우
    print('ptn이 txt에 포함되어 있는 맨 앞 인덱스: ', txt.index(ptn))
    print('ptn이 txt에 포함되어 있는 맨 끝 인덱스: ', txt.rindex(ptn))    

# str.startswith(문자) : 문자로 시작 ? T/ F , .endswith(문자)