def dict_add(dict1, dict2):
    dict1_copy = dict1.copy()       # update로 인해 dict1 값이 게속 변경, dict1_copy로 딕셔너리를 복사해 사용

    dict1.update(dict2)             # dict1 에 dict2 를 병합
    # dict1 |= dict2    |= 으로 update 사용한 것

    dict3 = dict(dict1_copy, **dict2)    # dict3 에 dict1, dict2를 병합 update를 사용하지 않음 (update 연산자 |=)
    dict4 = {**dict1_copy, **dict2}      # dict4 에 dict1, dict2를 언팩킹시켜서 dict4에 병합 (kargs 연산자 **)

    dict5 = dict1_copy | dict2           # dict5 에 dict1, dict2를 병합 (merge 연산자 |)
    for key in dict1_copy.keys() & dict2.keys():    # 두 딕셔너리에서 공통으로 존재하는 키만 반복 (&는 교집합 *앰퍼샌드)
        dict5[key] = max(dict1_copy[key], dict2[key])   # dict5의 키에 dict1, dict2 키 중 큰 값만 dict5 키에 반환

    print(dict1_copy)   # a=3, b=7, c=1, d=4 로 뜨는 이유는 병합하는 과정에서
    print(dict2)        # 키가 중복될 경우 마지막 딕셔너리의 값이 해당 키에 대한 값으로 들어감
    print(dict3)
    print(dict4)
    print(dict5)

def main():
    dict1 = {
        'a' : 3,
        'b' : 5,
        'c' : 2
    }

    dict2 = {
        'b' : 7,
        'c' : 1,
        'd' : 4
    }

    dict_add(dict1, dict2)

if __name__ == "__main__":
    main()