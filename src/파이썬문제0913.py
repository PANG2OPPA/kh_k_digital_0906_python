# A = int(input("입력 : "))
# B = list(map(int, input("입력 : ").split()))
# for i in B :
#     if i % A == 0 :
#         print(f"{i}is a multiple of {A}")
#     else :
#         print(f"{i}is NOT a multiple of {A}")

n = int(input())
ls = []
while True :
    x = (int(input()))
    if x == 0 : break
    ls.append(x)

for i in range(len(ls)):
    if ls[i] % n == 0 : print(f"{ls[i]} is a multiple of {n}.")
    else : print(f"{ls[i]} is NOT a multiple of {n}.")