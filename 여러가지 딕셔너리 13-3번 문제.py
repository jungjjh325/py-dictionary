def get_dict(a):
    user_input = int(input("값: "))

    key = [k for k, v in a.items() if v == user_input]

    if key:
        print(f"값 {user_input}을 가진 키는: {key[0]}")
        print()
    else:
        print("키가 존재하지 않습니다")
        print()

def ket_ext_list(b):
    user_input = input("입력: ")

    key = [k for k in b.keys() if k == user_input]

    if key:
        print(f'키 "{key[0]}"는 딕셔너리에 존재합니다. ')
        print()
    else:
        print(f'키 "{key}"는 딕셔너리에 존재하지 않습니다. ')
        print()

def del_value(c):
    user_input = int(input("값: "))

    for key in [key for key, value in c.items() if value == user_input]:
        c.pop(key)
    print(c)        # 딕셔너리에서의 pop은 키를 제거 값으로 제거 x
                    # 그렇기에 값을 찾아서 제거하려면 리스트컴프리헨션 이용 혹은
                    # 딕셔너리를 리스트화해서 인덱스 번호로 지우거나 해야함

def com_dict(d, e):
    print(d == e)

def avg_dict(g):
    value = sum(g.values())
    print("평균 값:",value / len(g))

def add_key(h):
    user_input = input("키: ")
    int_user_input = int(input("값: "))

    h[user_input] = int_user_input

    print(h)

def over_dict(f):
    hi_user_input = input("최상위 키: ")

    if hi_user_input in f:
        print(f"'{hi_user_input}' 안의 키들은 {f[hi_user_input]}입니다.")

        low_user_input = input("하위 키: ")
        int_user_input = int(input("값: "))

        if low_user_input in f[hi_user_input]:
            f[hi_user_input][low_user_input] = int_user_input
        else:
            print("하위키에 존재하지 않습니다.")
    else:
        print("상위키에 존재하지 않습니다.")
    print(f)
    print()

def min_dict(i):
    key = [k for k, v in i.items() if v == min(i.values())]
    print(f"최솟값을 가진 키: {key[0]}")

def comparison_dict(j):
    keys = {key: j[key] for key, value in j.items() if value >= 10}
    print(keys)

def sort_dict(k):
    print(dict(sorted(k.items(), key=lambda x: x[0])))

def main():
    a = {"a": 10, "b": 20, "c": 30}
    b = {"apple": 5, "banana": 10, "cherry": 15}
    c = {"x": 1, "y": 2, "z": 3}
    d = {"a": 1, "b": 2}
    e = {"a": 1, "b": 2}
    h = {"name": "Alice", "age": 25, "city": "Seoul"}
    g = {"a": 10, "b": 20, "c": 30, "d": 40}
    f = {"person": {"name": "John", "age": 25, "city": "Busan"}}
    i = {"x": 15, "y": 5, "z": 10}
    j = {"apple": 5, "banana": 10, "cherry": 15}
    k = {"y": 15, "x": 5, "z": 10}

    #get_dict(a)
    #ket_ext_list(b)
    #del_value(c)
    #com_dict(d, e)
    #add_key(h)
    #avg_dict(g)
    #over_dict(f)
    #min_dict(i)
    #comparison_dict(j)
    sort_dict(k)

if __name__ == "__main__":
    main()