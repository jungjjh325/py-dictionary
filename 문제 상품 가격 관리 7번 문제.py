class InputError(Exception):
    pass

def fruit_program():
    print("== 상품 가격 관리 프로그램 ==")
    print("1. 상품 추가")
    print("2. 상품 수정")
    print("3. 상품 삭제")
    print("4. 상품 목록 출력")
    print("5. 할인율 적용")
    print("6. 종료")
    print()

    return

def get_int_valid_input(prompt, valid_input = None):
    while True:
        try:
            user_input = input(prompt).strip()

            if not user_input:
                raise InputError("공백이 입력되었습니다.")

            if valid_input and user_input not in valid_input:
                raise InputError(f"{valid_input}외에 다른 것은 입력할 수 없습니다.")

            return int(user_input)

        except ValueError as error:
            print("== 프로그램 종료 ==")
            print(f"오류: {error}")

def get_int_discount(prompt, min_value = 1, max_value = 100):
    while True:
        try:
            user_input = input(prompt).strip()

            if not user_input:
                raise InputError("공백이 입력되었습니다.")

            int_value = int(user_input) # 입력값을 정수형으로 변환

            if int_value < min_value or int_value > max_value:
                print(f"입력값은 {min_value} - {max_value} 사이여야 합니다.")
                continue

            return int(user_input)

        except InputError as error:
            print("== 프로그램 종료 ==")
            print(f"오류: {error}")
        except ValueError:
            print("유효한 정수를 입력해주세요")

def get_str_valid_input(prompt, valid_input = None):
    while True:
        try:
            user_input = input(prompt).strip()

            if not user_input:
                raise InputError("공백이 입력되었습니다.")

            if valid_input and user_input not in valid_input:
                raise InputError(f"{valid_input}외에 다른 것은 입력할 수 없습니다.")

            if user_input.isdigit():
                raise  InputError(f"숫자를 입력할 수 없습니다.")

            return user_input

        except ValueError as error:
            print("== 프로그램 종료 ==")
            print(f"오류: {error}")

def add_fruit(fruit):
    fruit_name = get_str_valid_input("상품 이름을 입력하세요: ")

    if fruit.get(fruit_name): # 딕셔너리에 있을 경우
        print(f"{fruit_name}이 이미 존재합니다.")

        revise_fruit_name = get_str_valid_input("상품의 이름을 수정하시겠습니까? (y/n): ", ['y', 'Y', 'n', 'N'])

        if revise_fruit_name in ['y', 'Y']:
            revice_fruit(fruit)

        else:
            print("== 선택창으로 넘어갑니다. ==")
            print()
            return

    else:
        fruit_price = get_int_valid_input("상품 가격을 입력해주세요: ")
        fruit_menu = fruit[fruit_name] = fruit_price

        print(f"{fruit_name}의 가격을 {fruit_price}으(로) 설정하였습니다.")
        print()

        return

def revice_fruit(fruit):
    fruit_name = get_str_valid_input("수정할 상품 이름을 입력해주세요: ")

    if fruit_name not in fruit:
        print(f"{fruit_name}은 존재하지 않는 상품입니다.")
        return

    fruit_price = get_int_valid_input("상품 가격을 입력해주세요: ")
    fruit[fruit_name] = fruit_price

    print(f"{fruit_name}의 가격을 {fruit_price}으(로) 설정하였습니다.")
    print()

    return

def display_fruit_list(fruit):  # 딕셔너리에 어떤 과일이 있는지 값이 얼마인지 보여주는 함수
    print("== 현재 과일 목록 ==")
    for i, (fruit_name, fruit_price) in enumerate(fruit.items(), start = 1):    # cnumerate에 items로 키와 값을 쌍으로 받는다.
        print(f"{i}. {fruit_name} - {fruit_price}")     # items로 키와 값을 쌍으로 받은 후 i로 과일이 몇번인지 알려준다
    print()

    return

def select_fruit(fruit):    # 딕셔너리에 있는 과일을 실사용하는 함수
    display_fruit_list(fruit)   # 위에 있는 함수이다

    total_fruit = len(fruit)    # total_fruit가 fruit 딕셔너리의 길이를 잰다. ex) 사과 파인애플 두리안 - 3개
    choice = get_int_valid_input(f"1부터 {total_fruit} 사이의 번호를 입력해주세요: ", [str(i) for i in range(1, total_fruit + 1)])
    # choice는 말 그대로 fruit 딕셔너리에 있는 과일이 순서대로 있으면 번호를 선택하는 것을 의미

    selected_fruit = list(fruit.keys())[choice - 1]     # fruit 딕셔너리를 리스트화 시킨다, 후에 choice - 1로 입력한 숫자에 -1을 한 후 인덱스 번호에 있는 과일을 선택한다.

    del_fruit = get_str_valid_input(f"선택된 과일: {selected_fruit} - {fruit[selected_fruit]}원 입니다. 삭제하시겠습니까? (y/n): " ,['y', 'Y', 'n', 'N'])

    if del_fruit in ['y', 'Y']:
        del fruit[selected_fruit]
        print(f"요청하신 {selected_fruit}는 삭제되었습니다.")

    print()

    return

def product_list_output(fruit):
    print("== 전체 상품 목록 출력 ==")
    for i, (fruit_name, fruit_price) in enumerate(fruit.items(), start = 1):
        print(f"{i}. {fruit_name} - {fruit_price}")
    print()

    return

def discount_fruit(fruit):
    discount = get_int_discount("할인율(%)를 입력하세요: ", min_value = 1, max_value = 100)

    for fruit_name, fruit_price in fruit.items():
        discount_price = fruit_price - (fruit_price * discount / 100)

        fruit[fruit_name] = discount_price

        print(f"{fruit_name}의 할인된 가격: {discount_price:.2f}원")

    return

def end_program():
    print("== 프로그램 종료 ==")
    print()

    return

def main():
    fruit = {}

    while True:
        try:
            fruit_program()

            int_modifying = get_int_valid_input("원하는 작업을 입력하세요: ", ['1', '2', '3', '4', '5', '6'])

            if int_modifying == 1:
                add_fruit(fruit)
            elif int_modifying == 2:
                revice_fruit(fruit)
            elif int_modifying == 3:
                select_fruit(fruit)
            elif int_modifying == 4:
                product_list_output(fruit)
            elif int_modifying == 5:
                discount_fruit(fruit)
            else:
                end_program()

        except ValueError as error:
            print(f"오류: {error}")


if __name__ == "__main__":
    main()