A, B, C = map(int, input("입력 : ").split())
# cnt = 0
# while True:
#     # if A + (B * cnt) < C * cnt : break
#     if cnt > A // (C - B):break
#     cnt += 1
#
# print(cnt)
#
# if B > C:
#     print(-1)
if C <= B: print(-1)
else: print(A//(C-B) + 1)