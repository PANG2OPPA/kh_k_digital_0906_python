# 계좌 개설
def open_account(name) :
    print(f"{name}님의 계좌가 개설되었습니다.")
    return name # 반환값으로 이름을 전달

# 입금 함수
def deposit(input) : # 잔고와 입금액을 매개변수로 전달받음
    balance[0] += input
    print(f"{input}이 입금 되었습니다. 잔액은 {balance[0]}입니다.")

def withdraw(output) :
    if balance[0] >= output :
        balance[0] -= output
        print(f"{output}이 출금되었습니다. 잔액은 {balance[0]}입니다.")
    else :
        print(f"출금이 실패했습니다. 잔액은 {balance[0]}입니다.")

balance = [0] # 외부에서 선언했지만 매개변수로 전달하여 결과를 리턴 받음
name = open_account("김현빈")
deposit(1500)
withdraw(500)
print(f"{name}의 잔액은 {balance[0]}입니다.")