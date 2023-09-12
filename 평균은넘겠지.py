def over_rate() : # 각 케이스에서 평균이 넘는 비율 구하기
    ls = list(map(int, input().split())) # 공백 기준으로 입력 받아서 정수형 리스트로 담음
    average = sum(ls[1:]) / len(ls[1:]) # 리스트에서 맨 앞의 요소는 인원수 이므로 제외
    cnt = 0 # 평균이 넘는 %를 구하기 위해서는 인원에 카운트가 필요
    for i in range(1, len(ls)) : # 맨앞의 요소는 인원수 이므로 제외 함
        if ls[i] > average : cnt += 1
    return cnt / (len(ls)-1) * 100 # 백분율 표기로 변경

n = int(input()) # 총 테스트 횟수
rst = [] # 각 케이스에 대한 결과값을 받기 위한 리스트
for i in range(n) : # 총 테스트 횟수만큼 반복 수행
    rst.append(over_rate())

for e in rst :
    print(f"{e:.3f}%")