seat = list(map(int, input("좌석 번호 입력 : ").split()))
pc = [0] * 100
cnt = 0
for e in seat : # 향상된 for문이므로 e값을 고객이 앉고싶어 하는 좌석번호
    if pc[e - 1] != 0 : cnt += 1
    else: pc[e - 1] =1
print(cnt)