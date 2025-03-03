from matplotlib import pyplot as plt

class InputError(Exception):
    pass

def game_recode_sys_menu():
    print("== 게임 기록 관리 시스템 ==")
    print("1. 점수 추가")
    print("2. 점수 수정")
    print("3. 점수 조회")
    print("4. 전체 점수 목록 출력")
    print("5. 점수 분포 시각화")
    print("6. 최고 점수 플레이어 출력")
    print("7. 종료")

    return

def get_str_valid_input(prompt, valid_input = None):
    while True:
        try:
            user_input = input(prompt).strip()

            if not user_input:
                raise InputError("공백이 입력되었습니다.")
            if valid_input and user_input not in valid_input:
                raise InputError(f"입력이 {valid_input} 외에 다른 것은 입력할 수 없습니다.")
            if user_input.isdigit():
                raise InputError("숫자가 입력될 수 없습니다.")

            return user_input

        except ValueError as error:
            print(f"오류: {error}")

def get_int_valid_input(prompt, valid_input = None):
    while True:
        try:
            numbers = input(prompt).strip()

            if not numbers:
                raise InputError("공백이 입력되었습니다.")
            if valid_input and numbers not in valid_input:
                raise InputError(f"입력이 {valid_input} 외에 다른 것은 입력할 수 없습니다.")

            return numbers

        except ValueError as error:
            print(f"오류: {error}")

def game_recode_dict(game_recode_sys):
    while True:
        try:
            game_recode_sys_menu()

            int_modifying = get_int_valid_input("원하는 작업을 입력해주세요: ", ['1', '2', '3', '4', '5', '6', '7'])

            if int_modifying in '1':
                name = get_str_valid_input("플레이어 이름을 입력하세요: ").strip()

                if game_recode_sys.get(name): # 이름이 딕셔너리에 존재할 경우
                    print(f"{name}이 이미 존재합니다.")

                    str_modifying = get_str_valid_input("이름을 다시 입력하시겠습니까? (y/n): ", ['y', 'Y', 'n', 'N']).strip()

                    if str_modifying in ['y', 'Y']:
                        name = get_str_valid_input("플레이어 이름을 입력하세요: ").strip()
                        score = get_int_valid_input("점수를 입력하세요: ").strip()

                        game_recode_sys[name] = score

                        print(f"{name}의 점수가 {score}으(로) 추가 되었습니다.")
                        print("== 프로그램 재시작 ==")
                        continue

                    else:
                        print("== 프로그램 재시작 ==")
                        continue

                else:
                    score = get_int_valid_input("점수를 입력하세요: ").strip()

                    print(f"{name}의 점수가 {score}로 추가되었습니다.")
                    print("== 프로그램 재시작 ==")
                    continue

            elif int_modifying in '2':
                name = get_str_valid_input("플레이어 이름을 입력하세요: ").strip()

                if game_recode_sys.get(name): # 이름 딕셔너리에 있을 경우
                    str_modifying = get_str_valid_input("점수를 수정하시겠습니까? (y/n): ", ['y', 'Y', 'n', 'N']).strip()

                    if str_modifying in ['y', 'Y']:
                        score = get_int_valid_input("점수를 입력하세요: ").strip()

                        game_recode_sys[name] = score

                        print(f"{name}의 점수가 {score}으(로) 수정 되었습니다.")
                        print("== 프로그램 재시작 ==")
                        continue

                    else:
                        print("== 프로그램 재시작 ==")
                        continue

                else:
                    print(f"{name}이 존재하지 않습니다.")
                    print("== 프로그램 재시작 ==")
                    continue

            elif int_modifying in '3':
                print("플레이어 조회를 선택하셨습니다.")

                name = get_str_valid_input("플레이어 이름을 입력하세요: ").strip()

                if game_recode_sys.get(name):
                    print(f"{name}의 점수는 {game_recode_sys[name]}입니다.")
                    print("== 프로그램 재시작 ==")
                    continue

                else:
                    print("플레이어의 이름이 존재하지 않습니다.")
                    print("== 프로그램 재시작 ==")
                    continue

            elif int_modifying in '4':
                print("현재 점수 목록: ")

                if not game_recode_sys:
                    print("점수 목록이 비어있습니다.")

                else:
                    for name, score in game_recode_sys.items():
                        print(f"- {name} : {score}")

                print("== 프로그램 재시작 ==")
                continue

            elif int_modifying in '5':
                print("점수 분포를 표시합니다.")

                max_score = 100

                for name, score in game_recode_sys.items():
                    bar_length = (score * 10) // max_score  # 점수에 비례하는 bar 길이 계산
                    bar = '█' * bar_length  # '█' 문자를 이용한 막대그래프

                    print(f"{name} | {bar} ({score})")
                print("== 프로그램 재시작 ==")
                continue

            elif int_modifying in '6':
                max_score_user = max(game_recode_sys.keys())
                max_score_score = max(game_recode_sys.values())

                print(f"최고 점수 플레이어는 {max_score_user}입니다. ({max_score_score})점")
                print("== 프로그램 재시작 ==")
                continue

            else:
                print("프로그램을 종료합니다.")
                break

        except ValueError as error:
            print(f"오류: {error}")

def main():
    game_recode_sys = {
        '홍길동' : 95,
        '김철수' : 88,
        '박영희' : 73,
    }

    game_recode_dict(game_recode_sys)

if __name__ == "__main__":
    main()