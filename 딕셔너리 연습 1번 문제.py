def word_count():
    try:
        # 문자열 입력
        text = input("문자열 입력: ")

        # 입력 검증 (공백만 입력하는 경우 예외 처리)
        if not text.strip():
            raise ValueError("공백만 입력되었습니다. 유효한 단어를 입력하세요.")

        # 단어를 공백 기준으로 분리
        words = text.split()

        # 단어 빈도수를 저장할 딕셔너리
        word_dict = {}

        # 단어 빈도수 계산
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

        # 결과 출력
        print(word_dict)

    except ValueError as e:
        print(f"입력 오류: {e}")

# 함수 실행
word_count()
