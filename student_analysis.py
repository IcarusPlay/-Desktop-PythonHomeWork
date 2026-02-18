
import json
import os
from datetime import datetime
from collections import Counter


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(BASE_DIR, "student_courses.json")
REPORT_FILE = os.path.join(BASE_DIR, "student_courses_report.json")


def load_students(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def average_age(students):
    total = 0

    for student in students:
        birth = datetime.strptime(student["birth_date"], "%d.%m.%Y")
        enroll = datetime.strptime(student["enrollment_date"], "%d.%m.%Y")

        age = enroll - birth
        total += age.days / 365.25

    return total / len(students)


def students_counter(students):
    courses = []

    for student in students:
        courses.extend(student["courses"])

    return Counter(courses)


def main():
    students = load_students(DATA_FILE)

    total_students = len(students)
    avg_age = average_age(students)
    courses = dict(students_counter(students))

    report = {
        "total_students": total_students,
        "average_enrollment_age": round(avg_age, 1),
        "students_per_course": courses
    }

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print("Report created:")
    print(REPORT_FILE)


if __name__ == "__main__":
    main()
