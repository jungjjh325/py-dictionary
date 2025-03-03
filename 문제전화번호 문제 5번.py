class InputError(Exception):
    pass

def phonebook_list():
    print("== 전화번호부 관리 시스템 ==")
    print("1. 전화번호 추가")
    print("2. 전화번호 수정")
    print("3. 전화번호 조회")
    print("4. 종료")

    return

def filter_phonenumbers(phonenumbers):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    add = ''.join([char for char in phonenumbers if char in numbers])

    if len(phonenumbers) not in [10, 11]:
        raise InputError("전화번호는 10자리 숫자여야 합니다.")

    if len(add) == 10:
        return f"{add[:3]}-{add[3:7]}-{add[7:]}"
    elif len(add) == 11:
        return f"{add[:3]}-{add[3:7]}-{add[7:]}"
    else:
        raise InputError("전화번호는 10자리 혹은 11자리여야 합니다.")

def get_valid_input(prompt, valid_inputs = None):
    while True:
        try:
            user_input = input(prompt).strip()

            if not user_input:
                raise InputError("공백이 입력되었습니다.")
            if valid_inputs and user_input not in valid_inputs:
                raise InputError(f"입력 값이 {valid_inputs} 중 하나가 아닙니다.")

            return user_input

        except IndexError as error:
            print(f"오류: {error}")

def get_valid_inputs(prompt, valid_inputs = None):
    while True:
        try:
            user_input = input(prompt).strip()

            if not user_input:
                raise InputError("공백이 입력되었습니다.")
            if valid_inputs and user_input not in valid_inputs:
                raise InputError(f"입력 값이 {valid_inputs} 중 하나가 아닙니다.")
            if user_input.isdigit():
                raise InputError("입력값은 숫자가 될 수 없습니다.")

            return user_input

        except IndexError as error:
            print(f"오류: {error}")

def phonebook_dict(phonebook):
    while True:
        try:
            phonebook_list()

            int_modifying = get_valid_input("원하는 작업을 선택해주세요: ", ['1', '2', '3', '4'])
            if int_modifying in '1':
                name = get_valid_inputs("이름을 입력해주세요: ").strip()

                phonenumbers = get_valid_input("전화번호를 입력해주세요 (10/11자리 숫자만 입력): ")

                phonenumbers = filter_phonenumbers(phonenumbers)
                phonebook[name] = phonenumbers

                if name.isdigit():
                    raise InputError(f"이름에는 {name}을(를) 입력할 수 없습니다.")

                print(f"{name}의 전화번호는 {phonebook[name]}입니다.")

                continue
            elif int_modifying in '2':
                name = get_valid_inputs("수정할 이름을 입력해주세요: ").strip()

                if name not in phonebook:
                    print(f"오류: {name}은 전화번호부에 존재하지 않습니다.")
                    continue

                print(f"{name}의 현재 전화번호는 {phonebook[name]}입니다.")

                modifying = get_valid_inputs("수정하시겠습니다? (y/n): ", ['y', 'Y', 'n', 'N'])

                if modifying in ['y', 'Y']:
                    phonenumbers = get_valid_input("새 전화번호를 입력해주세요 (10/11자리 숫자만 입력): ")

                    phonenumbers = filter_phonenumbers(phonenumbers)
                    phonebook[name] = phonenumbers

                    print(f"{name}의 전화번호가 {phonebook[name]}로 수정되었습니다.")
                    continue
                else:
                    print("== 프로그램 종료 ==")
                    break
            elif int_modifying in '3':
                print("전화번호부 전체를 조회 1번 ")
                print("이름을 입력해 조회 2번 ")

                modifying = get_valid_input("입력해주세요 (1/2): ", ['1', '2'])

                if modifying in '1':
                    print("전화번호부 전체를 조회를 선택하셨습니다.")
                    print(f"{phonebook}")
                    continue
                else:
                    name = get_valid_inputs("조회할 이름을 입력해주세요: ").strip()

                    if name not in phonebook:
                        print(f"오류: {name}은 전화번호부에 존재하지 않습니다.")
                        continue

                    print(f"{name}의 전화번호는 {phonebook[name]}입니다.")
                    continue
            else:
                print("== 프로그램 종료 ==")
                break

        except InputError as error:
            print(f"오류: {error}")

def main():
    phonebook = {
        "홍길동": "010-1234-5678",
        "김철수": "010-2345-6789",
        "박영희": "010-3456-7890"
    }

    phonebook_dict(phonebook)

if __name__ == "__main__":
    main()