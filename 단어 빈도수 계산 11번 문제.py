def get_str_valid_input(prompt, valid_input = None):
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("공백이 입력되었습니다.")
            print()
        elif valid_input and user_input not in valid_input:
            print(f"{valid_input} 외에 다른 것이 입력되었습니다.")
            print()
        elif user_input.isdigit():
            print("숫자가 입력되었습니다.")
            print()
        else:
            return user_input

# apple banana apple orange banana apple
def count_word(void_dict):
    user_input = get_str_valid_input("단어를 입력해주세요: ").split()

    for k in user_input:
        if k in void_dict:
            void_dict[k] += 1
        else:
            void_dict[k] = 1

    v = void_dict.values()
    max_val = max(v)
    key = max(void_dict, key=void_dict.get)

    print(key, max_val)

    sort = sorted(void_dict.items(), key=lambda x: x[1])

    print(sort)


def main():
    void_dict = {}

    count_word(void_dict)

if __name__ == "__main__":
    main()