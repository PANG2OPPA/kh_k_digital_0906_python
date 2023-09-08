# # 내장함수 : 파이썬이 기본적으로 제공, import가 필요없음
# # 외장함수 : 파이썬이 기본적으로 제공, import가 필요함
#
# # 큰값 작은값 찾기
# print(max(1,2,3,4,5,6,45,56,7,777,88,99,700,100))
# print(min(1,2,3,4,5,6,45,56,7,777,88,99,700,100))
#
# # 총 합 구하기
# print(sum([1,2,3,4,5,6,45,56,7,777,88,99,700,100])) # 리스트의 총 합
# print(sum((1,2,3,4,5,6,45,56,7,777,88,99,700,100))) # 튜플의 총 합
# num = list(map(int, input("정수값 입력 : ").split()))
# print(f"입력받은 수의 총 합 : {sum(num)}")
# print(f"입력받은 수의 평균 : {sum(num)/len(num)}")
#
# # 몫과 나머지 구하기
# print(f"몫과 나머지 : {divmod(10, 4)}")

# 여러개의 값을 한번에 입력받아 리스트로 만들기
# 최대값, 최소값, 합계, 평균

# num = list(map(int, input("정수값 입력 : ").split()))
# print(f"""
# 최대값 : {max(num)}
# 최소값 : {min(num)}
# 합계 : {sum(num)}
# 평균 : {sum(num)/len(num)}
# 몫과 나머지 : {divmod(sum(num), 5)}""") # 몫과 나머지 출력하는 함수

# 오름차순 정렬
my_list = [1,2,3,4,5,45,6,46,8,46,5,46,465,654]
print(sorted(my_list))
# 내림차순 정렬
print(sorted(my_list, reverse=True))
