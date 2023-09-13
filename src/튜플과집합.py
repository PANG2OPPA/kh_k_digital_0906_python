# 튜플이란? 변경할 수 없는 시퀀스 자료형입니다. (나머지는 리스트와 동일)
# 튜플의 정의 () 괄호를 사용하거나 생량 할 수 있음

# 튜플 만들기
person = "김현빈", 24, "서울시 강남구 역삼동"
print(person)

# 튜플 요소 접근하기
print(person[0])
print(person[1])

# 튜플의 언패킹
이름, 나이, 주소 = person
print(이름)
print(나이)
print(주소)

# 튜플의 언패킹 기능을 이용한 함수 만들기
def get_person() :
    name = "가을"
    age = 23
    addr = "서울시 강남구 역삼동"
    return name, age, addr

result = get_person() # 언패킹되서 전달되는 반환값을 패킹해서 받음
print(result)

a, b, c = get_person()
print(a)
print(b)
print(c)

tp = 1,1,2,2,2,3,3,3,3
print(tp.count(3)) # 매개변수로 전달한 변수가 몇번 나오는지 확인하는 함수
print(tp.index(2)) # 매개변수로 전달한 변수의 시작 인덱스를 반환
print(len(tp))
# 튜플에서 안되는 것 (이뮤터블 특성이기 때문에 삭제할 수 없음)
del tp[0]


