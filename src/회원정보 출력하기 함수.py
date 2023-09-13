def print_info(name, age, gender, jobs) :
    jobs_str = "", "학생", "회사원", "주부", "무직"
    print("="*3, "회원정보", "=" * 3)
    print(f"이름 : {name}\n : {age}\n성별 : {gender}\n직업 : {jobs_str[jobs]}")

member_info = "member.txt"
fd = open(member_info, "wt", encoding="utf-8")
while True :
    name = input("이름을 입력하세요 (종료하려면 quit) : ")
    if name == 'quit' : break
    age = input_age()
    gender = input_gender()
    jobs = input_jobs()
    print_info(name, age, gender, jobs)