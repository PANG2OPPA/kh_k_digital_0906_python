# 4. 갯수가 정해지지 않은 여러개의 정수를 입력받아 합계와 평균 구하기
score = list(map(int, input("정수 : ").split()))
print(f"총점 : {sum(score)}")
print(f"평균 : {sum(score)/len(score)}")