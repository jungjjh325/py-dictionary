class InputError(Exception):
    pass

def Valid_Input(prompt, valid_inputs=None):
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise InputError("공백이 입력되었습니다.")
            if valid_inputs and user_input not in valid_inputs:
                raise InputError(f"입력 값이 {valid_inputs} 중 하나가 아닙니다.")
            return user_input
        except InputError as error:
            print(f"오류: {error}")

def Correction_Score(students, name):
    while True:
        correction_of_score = Valid_Input("점수를 수정하시겠습니까? (y/n): ", ['y', 'Y', 'n', 'N'])
        if correction_of_score in ['y', 'Y']:
            while True:
                try:
                    correction_score = int(Valid_Input("새 점수를 입력해 주세요 (0-100): "))
                    if 0 <= correction_score <= 100:
                        students[name] = correction_score
                        print(f"{name}의 점수가 {students[name]}점으로 수정되었습니다.")
                        return
                    else:
                        print("점수는 0에서 100 사이여야 합니다.")
                except ValueError:
                    print("숫자를 입력해주세요.")
        else:
            print("점수 수정이 취소되었습니다.")
            return

def Dict(students):
    while True:
        try:
            name = Valid_Input("학생 이름을 입력해주세요: ")
            if name.isdigit():
                print("오류: 숫자로 시작하는 이름은 허용되지 않습니다.")
                continue
            if name in students:
                print(f"{name}의 점수는 {students[name]}입니다.")
                Correction_Score(students, name)
            else:
                while True:
                    try:
                        score = int(Valid_Input(f"{name}의 이름이 없습니다. 점수를 입력해주세요 (0-100): "))
                        if 0 <= score <= 100:
                            students[name] = score
                            print(f"{name}의 점수가 {score}로 추가되었습니다.")
                            break
                        else:
                            print("점수는 0에서 100 사이여야 합니다.")
                    except ValueError:
                        print("숫자를 입력해주세요.")
        except InputError as error:
            print(f"오류: {error}")

        # 프로그램 반복 여부 확인
        continue_prompt = Valid_Input("계속 실행하시겠습니까? (y/n): ", ['y', 'Y', 'n', 'N'])
        if continue_prompt in ['n', 'N']:
            print("== 프로그램 종료 ==")
            break

def Main():
    students = {
        '홍길동': 85,
        '김철수': 92,
        '박영희': 78
    }
    Dict(students)

Main()