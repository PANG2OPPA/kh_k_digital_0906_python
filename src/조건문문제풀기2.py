# 2번 문제 : 주/야간 근무시간을 입력받아 아르바이트 급여 계산하기
# 주간근무 : 9620원
# 야간근무 : 주간 시급 * 1.5
# 주간근무 [1], 야간근무[2]를 입력하세요 :
# 근무 시간을 입력해 주세요 :
# 입력한 시간 동안 근무한 주간 또는 야간 급여는 ___원 입니다.

time = int(input("주간근무 [1] 야간근무 [2]"))
t = int(input("근무 시간 입력 : "))
if time == 1:
    c = t * 9620
else:
    c = t * 9620 *1.5

t2 = time == 1 and "주간" or "야간"
print(f"{t}시간 동안 근무한 {t2} 급여는 {c}원 입니다.")