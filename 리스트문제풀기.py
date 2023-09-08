# num = list(map(int, input("입력 : ").split()))
# ls1 = []
# ls2 = []
# for i in num :
#     if i % 2 == 0 :
#         ls1.append(i)
#     else:
#         ls2.append(i)
# print(ls1)
# print(ls2)

# map : 전달 받은 갯수를 함수 내부에서 가공 (입력 개수와 반환 개수가 동일)
# filter : 전달 받은 값을 함수 내부에서 조건이 일치하는 것만 골라서 반환

# 람다식 방법
num = list(map(int, input("입력 : ").split()))
odd = list(filter(lambda e:e % 2 == 1, num))
even = list(filter(lambda e:e % 2 == 0, num))
print(odd)
print(even)




