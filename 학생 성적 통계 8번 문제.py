def avg_dict(scores):
    new_score = {}

    for i, (scores_name, scores_score) in enumerate(scores.items(), start = 1):

        add = sum(scores_score.values())
        avg = round(add / len(scores_score), 2)

        new_score[scores_name] = avg

    print(f"평균 점수: {new_score}")

    high_avg = -1
    top_student = ""

    for student, score in new_score.items():
        if score > high_avg:
            high_avg = score
            top_student = student

    print(f"평균 점수가 가장 높은 학생: {top_student} ({high_avg})")

def max_dict(scores):
    max_score = {}

    for student, subjects in scores.items():
        for subject, score in subjects.items():
            if subject not in max_score or score > max_score[subject][0]:
                max_score[subject] = (score, student)

    for subject, (student, score) in max_score.items():
        print(f"{subject}의 최고 점수: {student} ({score})")

def main():
    scores = {
        "Alice": {"Math": 90, "English": 85, "Science": 88},
        "Bob": {"Math": 78, "English": 81, "Science": 89},
        "Charlie": {"Math": 95, "English": 92, "Science": 90},
        "Diana": {"Math": 88, "English": 79, "Science": 85}
    }

    avg_dict(scores)
    max_dict(scores)

if __name__ == "__main__":
    main()