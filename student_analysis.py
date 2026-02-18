import json
from datetime import datetime
from collections import Counter
from pathlib import Path


def load_students(file_path):
    """Загрузка данных студентов из JSON-файла."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл {file_path} не найден")
    return json.loads(path.read_text(encoding="utf-8"))


def calculate_average_age(students):
    """Средний возраст при поступлении."""
    ages = []
    for s in students:
        birth = datetime.strptime(s["birth_date"], "%d.%m.%Y")
        enrollment = datetime.strptime(s["enrollment_date"], "%d.%m.%Y")
        age_years = (enrollment - birth).days / 365.25
        ages.append(age_years)
    return sum(ages) / len(ages) if ages else 0


def count_courses(students):
    """Количество студентов на каждом курсе."""
    courses_list = [course for s in students for course in s.get("courses", [])]
    return dict(Counter(courses_list))


def save_report(report_data, filename):
    """Сохранение отчета в JSON."""
    Path(filename).write_text(json.dumps(report_data, indent=4, ensure_ascii=False), encoding="utf-8")


def main():
    students = load_students("student_courses.json")
    print(f"Total students: {len(students)}")

    avg_age = calculate_average_age(students)
    print(f"Average age at enrollment: {avg_age:.1f} years")

    courses_count = count_courses(students)
    print(f"Students per course: {courses_count}")

    report = {
        "total_students": len(students),
        "average_enrollment_age": avg_age,
        "students_per_course": courses_count
    }

    save_report(report, "student_courses_report.json")
    print("Report saved to 'student_courses_report.json'")


print("Запуск программы."); main()
