rst = ""
for e in input() : # 입력받은 문자열 만큼 자동 순회
    if e.islower() :
        rst += e.upper()
    else :
        rst += e.lower()
print(rst)