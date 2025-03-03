import matplotlib.pyplot as plt

class InputError(Exception):
    pass

def menu():
    print("== 학생 성적 통계 및 그래프 ==")
    print("1. 평균 성적")
    print("2. 과목별 최고 점수")
    print("3. 평균 점수가 가장 높은 학생")
    print("4. 그래프: 과목별 점수를 시각화한 막대그래프")
    print("5. 종료")
    print("==========================")
    print()

def get_int_valid_input(prompt, valid_input=None):
    while True:
        str_user_input = input(prompt).strip()

        if not str_user_input:
            print("오류: 공백은 입력할 수 없습니다.")
        elif valid_input and str_user_input not in valid_input:
            print(f"오류: {valid_input} 외에 입력될 수 없습니다.")
        else:
            if str_user_input.isdigit():
                return int(str_user_input)
            else:
                print("오류: 유효한 숫자를 입력해 주세요.")


def avg_score(scores):
    avg_name_score = {}

    for name, value in scores.items():
        add = sum(value.values())
        avg = round(add / len(value), 2)

        avg_name_score[name] = avg

    print(f"평균 점수: {avg_name_score}")
    print()

def subject_max_score(scores):
    max_score = {}

    for name, value in scores.items():
        for subject, score in value.items():
            if subject not in max_score or score > max_score[subject][0]:
                max_score[subject] = (score, name)

    for subject, (score, name) in max_score.items():
        print(f"{subject} 최고 점수: {name} - ({score})")
    print()

def avg_max_score(scores):
    avg_max_score_name = {}

    high_score = 0
    high_score_name = ""

    for name, value in scores.items():
        add = sum(value.values())
        avg = round(add / len(value), 2)

        avg_max_score_name[name] = avg

    for student, score in avg_max_score_name.items():
        if score >= high_score:
            high_score = score
            high_score_name = student

    print(f"평균 점수가 가장 높은 학생: {high_score_name} - ({high_score})")
    print()

def scatterplot(scores):
    avg_score = {}

    for name, value in scores.items():
        add = sum(value.values())
        avg = round(add / len(value), 2)

        avg_score[name] = avg

    student = list(avg_score.keys())
    avg_plot_score = list(avg_score.values())

    plt.plot(student, avg_plot_score, marker='o', color='blue')
    plt.title("Average Scores of Students")
    plt.xlabel("Student")
    plt.ylabel("Average Score")
    plt.grid()
    plt.show()

def user_choice(scores):
    while True:
        try:
            int_modifying = get_int_valid_input("원하는 작업을 입력해주세요: ", ['1', '2', '3', '4', '5'])

            if int_modifying == 1:
                avg_score(scores)
            elif int_modifying == 2:
                subject_max_score(scores)
            elif int_modifying == 3:
                avg_max_score(scores)
            elif int_modifying == 4:
                scatterplot(scores)
            else:
                print("== 프로그램 종료 ==")
                print()

                break

        except ValueError as error:
            print(f"오류: {error}")

def main():
    scores = {
        "Alice": {"Math": 85, "English": 78, "Science": 92},
        "Bob": {"Math": 88, "English": 90, "Science": 85},
        "Charlie": {"Math": 95, "English": 85, "Science": 88},
        "Diana": {"Math": 70, "English": 88, "Science": 80},
        "Eve": {"Math": 92, "English": 75, "Science": 85}
    }

    menu()
    user_choice(scores)

if __name__ == "__main__":
    main()
