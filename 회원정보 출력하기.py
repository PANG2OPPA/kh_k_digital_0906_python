name = input("이름을 입력 하세요 : ")
while True:
    age = input("나이를 입력하세요 : ")
    if age.isdigit():  # 문자열이 '숫자'로만 이루어져있는지 확인하는 함수
        age = int(age)
        if 0 < age < 200: break
    print("나이를 잘못 입력 하셨습니다. 다시 입력 하세요.")

while True:
    gender = input("성별을 입력 하세요 : ")
    if gender == 'M' or gender == 'm':
        break
    elif gender == 'F' or gender == 'f':
        break
    else:
        print("성별이 틀렸습니다. 다시 입력 해 주세요.")

while True:
    jobs = input("직업을 입력 하세요 : ")
    if jobs.isdigit():
        jobs = int(jobs)
        if 0 < jobs < 5: break
    print("직업이 잘못 입력되었습니다. 다시 입력해주세요.")

if gender == 'M' or gender == 'm':
    gen_name = "남성"
else:
    gen_name = "여성"

jobs_name = ("", "학생", "회사원", "주부", "무직")  # 튜플 사용

print("=" * 3, "회원정보", "=" * 3)
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gen_name}")
print(f"직업 : {jobs_name[jobs]}")
