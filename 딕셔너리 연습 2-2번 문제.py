from itertools import count

class InputError(Exception):
    pass

def Dict():
    Dict_A = {
        '홍길동' : 85,
        '김철수' : 92,
        '박영희' : 78
    }
    while True:
        try:
            Name = input("학생 이름을 입력하세요: ").strip()

            if not Name or Name.isdigit():
                raise InputError("공백과 숫자가 입력되었습니다.")

            if Dict_A.get(Name) is not None:
                print(f"{Name}의 점수는 {Dict_A[Name]}입니다.")

                User_Input = ['Y', 'y', 'N', 'n']
                Modifying = input("계속 실행하시겠습니까? (y/n):").strip()

                if not Modifying:
                    raise InputError("공백이 추가되었습니다.")

                if Modifying not in User_Input:
                    raise InputError(f"입력이 {User_Input}이 아닙니다.")

                if Modifying in ['Y', 'y']:
                    continue
                else:
                    print("== 프로그램 종료 ==")
                    break

            else:
                try:
                    Score = int(input(f"{Name}의 이름이 없습니다. 점수를 입력해주세요: ").strip())
                    if 0 <= Score <= 100:
                        Dict_A[Name] = Score
                        print(f"{Name}의 점수가 추가 되었습니다.")

                        User_Input = ['Y', 'y', 'N', 'n']
                        Modifying = input("계속 실행하시겠습니까? (y/n):").strip()

                        if not Modifying:
                            raise InputError("공백이 추가되었습니다.")

                        if Modifying not in User_Input:
                            raise InputError(f"입력이 {User_Input}이 아닙니다.")

                        if Modifying in ['Y', 'y']:
                            Sum = sum(Dict_A.values())
                            Avg = Sum / len(Dict_A)
                            print(f"학생들의 평균 점수는 {Avg}입니다.")

                            Modifying = input("계속 실행하시겠습니까? (y/n):").strip()

                            if not Modifying:
                                raise InputError("공백이 추가되었습니다.")

                            if Modifying not in User_Input:
                                raise InputError(f"입력이 {User_Input}이 아닙니다.")

                            if Modifying in ['Y', 'y']:
                                continue
                            else:
                                print("== 프로그램 종료 ==")
                                break

                        else:
                            print("== 프로그램 종료 ==")
                            break
                    else:
                        print("값 오류: 점수는 0 ~ 100 사이여야 합니다.")

                        User_Input = ['Y', 'y', 'N', 'n']
                        Modifying = input("계속 실행하시겠습니까? (y/n):").strip()

                        if not Modifying:
                            raise InputError("공백이 추가되었습니다.")

                        if Modifying not in User_Input:
                            raise InputError(f"입력이 {User_Input}이 아닙니다.")

                        if Modifying in ['Y', 'y']:
                            continue
                        else:
                            print("== 프로그램 종료 ==")
                            break

                except ValueError:
                    print("점수는 숫자여야 합니다.")

        except InputError as Error:
            print(f"오류: {Error}")

            User_Input = ['Y', 'y', 'N', 'n']
            Modifying = input("계속 실행하시겠습니까? (y/n):").strip()

            if not Modifying:
                raise InputError("공백이 추가되었습니다.")

            if Modifying not in User_Input:
                raise InputError(f"입력이 {User_Input}이 아닙니다.")

            if Modifying in ['Y', 'y']:
                continue
            else:
                print("== 프로그램 종료 ==")
                break

Dict()