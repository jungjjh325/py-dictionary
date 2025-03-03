def department_avg_salary(employees):

    department_jobs = {}

    for user, info in employees.items():
        department = info["Department"]
        salary = info["Salary"]

        if department not in department_jobs:
            department_jobs[department] = []

        department_jobs[department].append(salary)

    for departmentm, salarys in department_jobs.items():
        avg = round(sum(salarys) / len(salarys), 2)
        print(f"{departmentm}의 평균 급여: {avg}")
    print()

    return

def high_salary(employees):
    price = 6000

    print(f"급여 {6000} 이상 직원: ")

    for name, info in employees.items():
        salary = info["Salary"]

        if salary >= price:
            print(f"{name} ({salary})")
    print()

    return

def very_high_salarys(employees):
    high_salary = 0

    for name, info in employees.items():
        salary = info["Salary"]

        if salary > high_salary:
            high_salary = salary
            high_salary_name = name

    print(f"급여가 가장 높은 직원: {high_salary_name} ({high_salary})")
    print()

    return

def department_sqot_salary(employees):
    department_name = {}

    for name, department in employees.items():
        department_name_value = department["Department"]
        salary = department["Salary"]

        if department_name_value not in department_name:
            department_name[department_name_value] = []
        department_name[department_name_value].append((name, salary))

    for departments, employees_list in department_name.items():
        print(f"{departments}:")
        for name, salary in employees_list:
            print(f"{name} - ({salary})")
        print()

    return

def main():
    employees = {
        "Alice": {"Department": "HR", "Salary": 5000},
        "Bob": {"Department": "Engineering", "Salary": 7000},
        "Charlie": {"Department": "HR", "Salary": 6000},
        "Diana": {"Department": "Engineering", "Salary": 8000},
        "Eve": {"Department": "Marketing", "Salary": 4500}
    }

    department_avg_salary(employees)
    high_salary(employees)
    very_high_salarys(employees)
    department_sqot_salary(employees)

if __name__ == "__main__":
    main()