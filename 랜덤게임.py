'''
숫자 맞히기 게임
문제 요구 사항:

컴퓨터는 1부터 100 사이의 랜덤 숫자를 선택합니다.
사용자는 숫자를 입력하여 컴퓨터가 선택한 숫자를 맞히려고 시도합니다.
사용자가 입력한 숫자가 정답보다 크면 "더 낮은 숫자입니다"를 출력하고, 작으면 "더 높은 숫자입니다"를 출력합니다.
정답을 맞히면 "축하합니다! {시도 횟수}번 만에 맞혔습니다."를 출력합니다.
추가 조건:

random 모듈을 사용하세요.
사용자가 유효한 숫자를 입력하지 않으면 "잘못된 입력입니다. 1부터 100 사이의 숫자를 입력하세요."를 출력하세요.
'''
import random

class rand_game:
    def __init__(self):
        self.rand_number = random.randrange(1, 101)

    def game_play(self):
        attempt = 0

        while True:
            guest = self.get_int_user_input("숫자 입력 (1~100): ")
            attempt += 1

            if guest < self.rand_number:
                print("더 높은 숫자입니다.")
                print()
            elif guest > self.rand_number:
                print("더 낮은 숫자입니다.")
                print()
            else:
                print(f"축하합니다! {attempt}번 만에 맞췄습니다.")
                print()
                break

    @staticmethod
    def get_int_user_input(prompt, min_val = 1, max_val = 100):
        while True:
            try:
                user_input = int(input(prompt).strip())

                if not user_input:
                    print("공백이 입력되었습니다.")
                elif min_val <= user_input <= max_val:
                    return user_input
                else:
                    print(f"오류: .{min_val} - {max_val} 외의 다를 숫자는 입력될 수 없습니다.")
            except ValueError as Error:
                print(f"오류: {Error}")
                print("다시 시도해주세요")

if __name__ == "__main__":
    game = rand_game()
    game.game_play()


