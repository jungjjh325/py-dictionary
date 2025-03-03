class InputError(Exception):
    pass

def Dict_A1():
    try:
        Name = input("학생 이름을 입력해주세요: ")
        Score = int(input("점수를 입력해주세요: "))

        if not Name.strip():
            raise InputError("공백이 입력되었습니다")

        Dict = {
            '홍길동': 85,
            '김철수': 92,
            '박영희': 78
        }

        if Dict.get(Name) is not None:
            Dict[Name] = Score
            print(f"{Name}의 점수는 {Score}입니다.")

            user_input = ['Y', 'y', 'N', 'n']
            Modifying = input("점수를 수정하시겠습니까? (y/n): ")

            if not Modifying.strip():
                raise InputError("공백이 입력되었습니다.")

            if Modifying not in user_input:
                raise InputError(f"입력된 값: {user_input}이 아닙니다.")

            if Modifying == "Y" or Modifying == 'y':
                Modifying_Score = int(input("수정할 점수를 입력하세요: "))
                Dict[Name] = Modifying_Score
                print(f"{Name}의 점수가 {Modifying_Score}로 수정되었습니다.")
            else:
                print(f"{Name}의 점수가 {Score}로 동일합니다.")

        else:
            print(f"{Name}의 이름이 존재하지 않습니다.")

    except InputError as Error:
        print(f"입력이 잘못되었습니다. {Error}")
    except ValueError as Errors:
        print(f"입력이 잘못되었습니다. {Errors}")

Dict_A1()