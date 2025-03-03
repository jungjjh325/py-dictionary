def merge_dict(a):  # 중첩된 딕셔너리 값 수정
    high_dict = input("상위: ")

    if high_dict in a:
        low_dict = input("하위: ")
        int_value = int(input("값: "))

        if low_dict in a[high_dict]:
            a[high_dict][low_dict] = int_value

            print(f"상위 '{high_dict}'의 하위 '{low_dict}'의 값을 '{int_value}'로 수정하였습니다.")
            print(a)

        else:
            print("하위 키가 존재하지 않음")
            print()
    else:
        print("상위 키가 존재하지 않음")
        print()

def add_dict_key(b, c):     # ** 두 딕셔너리 병합, 중첩된 키는 값 더해주기 ** (중요)
    for key, value in c.items():    # c 딕셔너리의 키랑 값을 나눔
        if key in b:                # b 딕셔너리의 안에 c의 키가 있는지 확인
            b[key] += value         # 있을시 b의 키에 c의 값을 더해줌
        else:
            b[key] = value          # 없을시 b의 키에 c의 값을 추가해줌
    print(b)                        # 키에대한 값의 추가를 b 딕셔너리에 했기에 b 딕셔너리 출력
    print()

def find_key(d):    # ** 주어진 value(값)으로 딕셔너리 키 찾기 **
    int_user_input = int(input("값: "))

    key = {key: d[key] for key, value in d.items() if value == int_user_input}
    print(key)
    print()

def revers_sort_dict(e):    # 정렬된 딕셔너리 오름차순
    print(dict(sorted(e.items(), key=lambda x: x[1], reverse=False)))
    print()

def count_dict(f):  # ** 알파벳 카운팅 **
    dict_a = {}

    for word in f:  # f 딕셔너리에 있는 문자열이 word에 있는지 확인, 문자열이 1개이기에 한번만 돈다
        for char in word:   # 문자열 word의 각 문자를 하나씩 반복하여 char에 대입, 첫 번째 반복 h, 두 번째 반복 e ,,,
            if char.isalpha():  # char가 알파벳인지 확인, 띄어쓰기 제거, 숫자 제거
                char = char.lower() # 모든 문자열을 소문자로 변경
                dict_a[char] = dict_a.get(char, 0) + 1  # 비어있는 딕셔너리에 char변수 추가 {'h': 1},
    print(dict_a)                                       # dict.a안에 char 변수가 있으면 + 1씩 증가, 기본값 0
    print()

def binary_search(g, target):   # ** 이진 탐색 **
    low = 0
    high = len(g) - 1   # len의 길이가 10이고 파이썬은 0부터 시작이기에 -1

    while low <= high:  # 간단히 0 > 9 틀리고, 0 < 9가 맞음
        mid = (low + high) // 2 # 중간부분은 low + high를 2로 나눈 몫임

        if g[mid] == target:    # 중간부분이 타겟과 같으면
            print(f"값 {target}의 인덱스는 {mid}번 입니다.")
            print()
            break
        elif g[mid] > target:   # 중간 부분이 타겟보다 클 경우 g[4] > target = 인덱스 4번은 9 > 7
            high = mid - 1      # high를 mid - 1로 해서 처음 4 - 1 = 3으로 인덱스 번호 3 오른쪽은 다 버림
        else:                   # 중간 부분이 타겟보다 작을 경우 g[1] < target = 인덱스 1번은 3 < 7
            low = mid + 1       # low를 mid + 1로 해서 처음 1 + 1 = 2로 인덱스 번호 1 왼쪽은 다 버림

# 0 + 9 // 2 = 4, 9 > 7, high = g[mid] X, 그냥 mid, 4 - 1 = 3, 0 + 3 // 2 = 1, 3 < 7, 1 + 1 = 2, 2 + 3 // 2 = 2, 5 < 7, 2 + 1 = 3, 3 + 3 // 2 = 3, 7 == 7 인덱스는 3번?

def set_key_dict(h):    # ** 중복된 문자 제거 **
    result = "" # 빈 문자열

    for char in str(h): # 딕셔너리 h를 str로 변환 후 char에 대입
        if char != '{' and char != "}" and char != ',' and char != "'": # {'apple'}이 나오기에 {} , '' 를 제거 해줌
            if char not in result:  # result 문자열에 char(apple)가 없으면 추가 첫 번째 p는 result에 없기에 추가, 두 번째는 있기에 추가 X
                result += char      # 문자열을 이어붙이는 코드, char의 apple을 하나씩 대입 a, p, l, e

    print(result)
    print()

def word_count(i):  # ** 단어 빈도 수 체크 **
    word = i.split()    # 하나의 문자열을 띄어쓰기를 기준으로 단어로 쪼갬
    count_dict = {}     # 빈 딕셔너리 생성

    for word in word:   # 각 단어가 word에 존재하는지 확인
        if word in count_dict:  # count_dict에 word가 있는지 확인
            count_dict[word] += 1   # 참일 경우 단어 ex) count_dict[apple]이 있으면 증가
        else:   # 거짓일 경우
            count_dict[word] = 1    # count_dict에 1로 추가

    print(count_dict)  # dict.a안에 char 변수가 있으면 + 1씩 증가, 기본값 0
    print()

def dict_add(k, l):
    print(list(set(k) & set(l)))
    print(list(set(k) | set(l)))
    print(list(set(k) - set(l)))
    print(list(set(l) - set(k)))
    print()

def dict_union(m, n):
    print(m & n)
    print(m | n)
    print(m - n)
    print(n - m)
    print()

def main():
    a = {"person": {"name": "John", "age": 30}}
    b = {"a": 1, "b": 2}
    c = {"b": 3, "c": 4}
    d = {"apple": 5, "banana": 10, "cherry": 5}
    e = {"a": 3, "b": 2, "c": 1}
    f = {"hello world"}
    g = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    h = {"apple"}
    i = "apple orange apple banana apple"

    k = [1, 2, 3]
    l = [2, 3, 4]
    m = {1, 2, 3}
    n = {2, 3, 4}

    #merge_dict(a)
    #add_dict_key(b, c)
    #find_key(d)
    #revers_sort_dict(e)
    #count_dict(f)
    #binary_search(g, target)
    #set_key_dict(h)
    word_count(i)
    #9
    #dict_add(k, l)
    #dict_union(m, n)

if __name__ == "__main__":
    main()