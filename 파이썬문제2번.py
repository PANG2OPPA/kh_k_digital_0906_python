# 2. 3개의 정수를 입력받아 최대값과 최소값 구하기
a, b, c = map(int, input("3개의 정수 입력 : ").split(","))
list_num = [a, b, c]
list_num.sort()
print(list_num[2], list_num[0])
