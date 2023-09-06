# 1. 정해진 형식으로 시간을 입력 받아서 출력하기
# 입력 형식 : 22:5:5 => 오후 10시 05분 05초
hour, min, sec = map(int, input("시간 입력 : ").split(":"))
if hour > 12:
    hour -= 12
    print(f"오후 {hour:02}시{min:02}분{sec:02}초")
else:
    print(f"오전 {hour:02}시{min:02}분{sec:02}초")