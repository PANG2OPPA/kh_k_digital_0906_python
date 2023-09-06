# 3. 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기


from datetime import datetime

jumin = input("주민등록번호 입력 : ")
year = jumin[:2]
month = jumin[2:4]
day = jumin[4:6]
gender = jumin[7]


if gender == "1" or gender == "2" :
    age = curr_year - 1900 - year
else:
    age = curr_year - 2000 - year

if gender == 1 or gender == 3:
    gender_str = "남성"
else:
    gender_str = "여성"

    print(f"생년월일 : {year:02}년 {month:02}월 {day:02}일")
    print(f"성별 : {gender_str}")
    print(f"나이 : {age}")


