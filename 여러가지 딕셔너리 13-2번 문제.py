def dict_value_add(a):  # 1. 딕셔너리 값 합계
    print("1. 합계: ", sum(a.values()))
    print()

def reverse_key_value(b):   # 2. 딕셔너리 키-값 뒤집기
    print("2.", dict(zip(b.values(), b.keys())))
    print()

def max_value(c):   # 3. 값의 최댓값 찾기
    # 1. value를 나누고 2. 나눈 value를 서로 비교 하고 3. 비교한 것 중에 제일 큰 값 출력
    print("3.", [k for k, v in c.items() if v == max(c.values())])
    print()

def del_value(d):
    v = list(set(d.values()))
    k = {}

    for key, value in d.items():
        if value in v:
            k[key] = value
            v.remove(value)

    print("4.", k)
    print()

def dict_merge(e, f): # 5. 딕셔너리 합치기
    from collections import Counter

    print("5.", dict(Counter(e) + Counter(f)))
    print()

def key_existence(g):   # 6. 키 존재 여부 확인
    user_input = input("입력: ")

    key = [v for k, v in g.items() if k == user_input]

    if key:
        print(f"6. 키 {user_input}의 값: {key}")
        print()
    else:
        print("존재하지 않는 키")
        print()

def sort_value(h):  # 7. 값으로 정렬하기
    print("7.", sorted(h.items(), key=lambda x:x[1]))
    print()

def key_list_print(i):  # 8. 키 목록 추출하기
    print("8.", [k for k in i.keys()])
    print()

def value_get(j):   # 9. 값의 개수 세기
    user_input = int(input("입력: "))

    count = list(j.values()).count(user_input)

    print("9.", count)
    print()

def over_dict(k):   # 10. 중첩 딕셔너리 접근
    print("10.", k)

def main():
    a = {"a": 10, "b": 20, "c": 30}
    b = {"x": 1, "y": 2, "z": 3}
    c = {"apple": 15, "banana": 25, "cherry": 10}
    d = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
    e = {"a": 1, "b": 2, "c": 3}
    f = {"b": 3, "c": 4, "d": 5}
    g = {"python": 3, "java": 8, "c++": 5}
    h = {"x": 15, "y": 5, "z": 10}
    i = {"name": "Alice", "age": 25, "city": "Seoul"}
    j = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 1}
    k = {"person": {"name": "John", "age": 30, "city": "Busan"}}

    dict_value_add(a)
    reverse_key_value(b)
    max_value(c)
    del_value(d)
    dict_merge(e, f)
    key_existence(g)
    sort_value(h)
    key_list_print(i)
    value_get(j)
    over_dict(k)

if __name__ == "__main__":
    main()