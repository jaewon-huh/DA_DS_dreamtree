# 브루트 포스법으로 문자열 검색

def bf_match(txt: str, pat: str) -> int :
    pt = 0              # txt pointer               ABABCDEF
    pp = 0              # pattern pointer           ABC

    while pt != len(txt) and pp !=len(pat) :        # 포인터가 끝에 위치 x 
        if txt[pt] == pat[pp] :                     # 포인터 인덱스 서로 =
            pt += 1                                            
            pp += 1
        else :                                      
            pt = pt - pp +1                         # ABABCDEF  123
            pp = 0                                  #  ABC      012

    return pt - pp if pp == len(pat) else -1        
    # 검색 성공하면 성공한 txt 인덱스 반환  


if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')  # 텍스트용 문자열
    s2 = input('패턴을 입력하세요.: ')    # 패턴용 문자열

    idx = bf_match(s1, s2)  # 문자열 s1~s2를 브루트 포스법으로 검색

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자에서 일치합니다.')
