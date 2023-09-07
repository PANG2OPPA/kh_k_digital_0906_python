# 반복문 : 조건이 참인 동안 계속 수행되는 구문
# n = int(input("정수를 입력 하세요 : "))
# sum = 0
# while n : # 파이썬 정수값이 0이 아니면 참으로 간주함
#     sum += n
#     n -= 1 # 파이썬은 증감 연산자가 없음
# print(sum)

# while True :
#     age = int(input("나이를 입력 하세요 : "))
#     if 0 < age < 200 : break
#     print("나이 입력 범위가 벗어났습니다.")

# for 요소 in 시퀀스 : 시퀀스의 각 요소를 순회하는데 사용 (자바의 향상된 for문과 동일)
# fruits = ["apple", "banana", "cherry", ["seoul", "korea"]]
# print(fruits[3][1][0])
# for e in fruits:
#     print(e[0])
#
# str1 = "경기도 광명시 철산동"
# for e in str1:
#     print(e, end="/")

# for 변수 in range(시작값, 종료값, 증감값):
# n = int(input("정수를 입력하세요 : "))
# sum = 0
# for i in range(1, n+1) : # 1부터 n+1 미만
#     sum += i
# print(sum)
#
# # for문을 역순으로 반복하기
# for i in range(10, -1, -1) : # 10 ~ 0 까지 출력
#     print(i)

# 이중 for문
# n = int(input("정수를 입력하세요 : "))
# for i in range(0, n) :
#     for j in range(0, n) :
#         print("*", end=' ')
#     print()

# 구구단 찍기
# for i in range(2, 10) : # 2단 ~ 9단
#     for j in range(2, 10) :
#         print(f"{i} x {j} = {i*j}")
#         print()

# 홀수 / 짝수 나누어 찍기
# n = int(input("정수 입력 : "))
# for i in range(0, n) :
#     for j in range(0, n) :
#         if j % 2 == 0 : print("$", end=' ')
#         else:print("*", end=' ')
#     print()

# 사각형 찍기
# 정수값 n을 입력받아 n * n 크기의 행렬을 출력하는 프로그램 작성
# n = int(input("정수 입력 : "))
# for i in range(1, n * n + 1) :
#     print(f"{i:>3}", end=' ')
#     if i % n ==0 : print()

# 삼각형
# n = int(input("별 갯수 입력 : "))
# for i in range(n) :
#     for j in range(i+1) :
#         print("*", end=" ")
#     print()

# 역삼각형
# n = int(input("정수 입력 : "))
# for i in range(n) :
#     for j in range(n-i):
#         print("*", end=" ")
#     print()

# 역 피라미드
# n = int(input("정수 입력 : "))
# for i in range(n):
#     for j in range(n-i):
#         if j % n == 0 :
#             print(" " * i, end=" ")
#         print("*", end=" ")
#     print()

# 역 피라미드 답
# n = int(input("정수 입력 : "))
# for i in range(n, 0, -1):
#     for s in range(n - i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()


# 문자와 ASCII 코드
# chr : 유니코드 값을 입력받아 그 코드에 해당하는 문자를 출력
# ord : 문자를 유니코드값으로 변환
for i in range(ord("A"),ord("Z")+1):
    print(chr(i), end=" ") # chr 문자 출력
print()

for i in range(65,91):#A:65 Z:90
	print(chr(i), end=" ")
print()


# 반대 역삼각형
# n = int(input("정수 입력 : "))
# for i in range(n) :
#       for s in range(i):
#           print(" ", end=" ")
#       for j in range(n-i):
#           print("*", end=" ")
#       print()



