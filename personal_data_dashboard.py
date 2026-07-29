# Personal Data Dashboard.

import csv
import json

# Load students from CSV
def load_students(filename):
    students = []

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            student = {
                "id": row[0],
                "name": row[1],
                "marks": int(row[2])
            }
            students.append(student)

    return students


# Load courses from JSON.
def load_courses(filename):
    with open(filename, "r") as file:
        return json.load(file)


# Generate report.
def generate_report(students, courses):

    report = []

    total_marks = 0

    for student in students:

        course = courses.get(student['id'], "Not Assigned")

        report.append({
            "Name": student["name"],
            "Course": course,
            "Marks": student["marks"]
        })

        total_marks += student["marks"]

    average = total_marks / len(students)

    return report, average

# Save report as CSV.
def save_report(report):
    with open("final_report.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Name", "Course", "Marks"])

        for student in report:
            writer.writerow([
                student["Name"],
                student["Course"],
                student["Marks"]
            ])


# Main Program.
students = load_students("school_students.csv")
courses = load_courses("school_courses.json")

report, average = generate_report(students, courses)

save_report(report)

print("Student Summary")
print("-" * 30)

for student in report:
    print(student)

print("\nAverage Marks: ", average)
print("\nReport saved as final_report.csv")
