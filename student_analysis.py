import json
from datetime import datetime


def load_students(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def calculate_average_age(students):
    total_age = 0

    for student in students:
        birth = datetime.strptime(student["birth_date"], "%d.%m.%Y")
        enroll = datetime.strptime(student["enrollment_date"], "%d.%m.%Y")
        age = (enroll - birth).days / 365.25
        total_age += age

    if len(students) == 0:
        return 0

    return total_age / len(students)


def count_courses(students):
    courses = {}

    for student in students:
        for course in student.get("courses", []):
            if course in courses:
                courses[course] += 1
            else:
                courses[course] = 1

    return courses


students = load_students("student_courses.json")

print("Всего студентов:", len(students))

avg_age = calculate_average_age(students)
print("Средний возраст при зачислении:", round(avg_age, 1))

courses_count = count_courses(students)
print("Количество студентов по курсам:", courses_count)

report = {
    "Общее количество студентов": len(students),
    "Средний возраст при зачислении": round(avg_age, 1),
    "Количество студентов по курсам": courses_count
}

with open("student_courses_report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4, ensure_ascii=False)

print("Отчет сохранен")