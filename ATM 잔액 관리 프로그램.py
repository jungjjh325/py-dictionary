'''
문제 요구 사항:

은행의 ATM 시스템을 시뮬레이션하는 프로그램을 작성하세요.
사용자에게 다음과 같은 메뉴를 제공합니다:
1: 잔액 조회
2: 입금
3: 출금
4: 종료
각 동작에 대해 적절한 입력을 받고 결과를 처리합니다.
잔액 조회: 현재 잔액을 출력합니다.
입금: 입금할 금액을 입력받아 잔액을 증가시킵니다.
출금: 출금할 금액을 입력받아 잔액을 감소시킵니다. 단, 잔액이 부족하면 "잔액이 부족합니다."를 출력합니다.
종료: 프로그램을 종료하며 "프로그램을 종료합니다."를 출력합니다.
잘못된 입력을 받으면 "잘못된 입력입니다. 다시 선택하세요."를 출력하고 메뉴를 다시 보여줍니다.
추가 조건:

초깃값 잔액은 0원입니다.
입력값이 유효하지 않은 경우 (숫자가 아닌 입력 등) 오류를 처리합니다.
'''

class atm_sys:
    def __init__(self):
        self.cash = 0
        self.main_menu()

    def main_menu(self):
        print("== 1. 잔액 조회 ==")
        print("== 2. 입금 ==")
        print("== 3. 출금 ==")
        print("== 4. 종료 ==")

        self.int_user_input = self.get_int_user_input("숫자 입력: ", ['1', '2', '3', '4'])

        if self.int_user_input == '1':
            self.cash_balance()
        elif self.int_user_input == '2':
            self.cash_deposit()
        elif self.int_user_input == '3':
            self.cash_withdraw()
        else:
            self.exit()

    def cash_balance(self):
        print(f"현재 잔액: {self.cash}원")

    def cash_deposit(self):
        print("입금 페이지에 접속 하셨습니다.")
        money = self.get_int_user_input("금액 입력: ")

        if money.isdigit():
            print("입금 페이지 입니다.")

            self.cash += int(money)

            print(f"{money}원 만큼 입금되었습니다, 현재 잔액: {self.cash}")
            print()
        else:
            print("금액이 잘못 되었습니다.")
            print()

    def cash_withdraw(self):
        print("출금 페이지에 접속 하셨습니다.")
        print(f"현재 잔액: {self.cash}")
        money = self.get_int_user_input("금액 입력: ")

        if money.isdigit():
            money = int(money)

            if self.cash < money:
                print("잔액 부족 입니다.")
                print()
            else:
                self.cash -= money

                print(f"출금이 {money}원 만큼 완료 되었습니다, 현재 잔액: {self.cash}")
                print()

        else:
            print("금액을 잘못 입력하셨습니다.")
            print()

    def exit(self):
        print("종료 페이지입니다.")
        print()

    @staticmethod
    def get_int_user_input(prompt, valid_input=None):
        while True:
            user_input = input(prompt).strip()

            if not user_input:
                print("공백이 입력되었습니다.")
                print()
            elif valid_input and user_input not in valid_input:
                print(f"오류: {valid_input}외에 다른 것은 입력될 수 없습니다.")
                print()
            elif user_input.isdigit():
                return user_input
            else:
                print("유효하지 않은 입력입니다.")

if __name__ == "__main__":
    atm_sys()