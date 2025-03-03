def dict_a():
    try:
        keys, value = input("키와 값을 입력 (ex: key2 40): ").split()

        # keys가 공백만 있으면 ValueError 발생
        if not keys.strip():
            raise ValueError("공백만 입력되었습니다.")

        Dict = {
            'key1': 10,
            'key2': 20,
            'key3': 30
        }

        # get()을 이용해 키가 존재하는지 확인
        if Dict.get(keys) is not None:
            Dict[keys] = int(value)  # 값은 정수로 변환
            print(Dict)
        else:
            print(f"키 '{keys}'는 딕셔너리에 존재하지 않습니다.")  # 키가 없을 때 실행되는 부분

    except ValueError as Error:
        print(f"Error: {Error}")
        print("딕셔너리 업데이트에 실패했습니다.")

dict_a()
