
# a, b, c, d, e = map(int, input("세개 버거값과 두개 음료값 입력 : ").split(" "))
a = int(input("상덕 : "))
b = int(input("중덕 : "))
c = int(input("하덕 : "))
d = int(input("콜라 : "))
e = int(input("사이다 : "))

list_num1 = [a, b, c]
list_num1.sort()
list_num2 = [d, e]
list_num2.sort()
print(list_num1[0] + list_num2[0] - 50)


