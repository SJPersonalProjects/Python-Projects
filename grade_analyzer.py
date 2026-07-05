# Grade Analyzer.

student_marks = []

while True:
    marks = input("Enter students marks (q to quit): ")

    if marks.lower() == 'q':
        break

    student_marks.append(float(marks))


if len(student_marks) == 0:
    print("No marks were entered.")

else:
    total = 0
    
    for mark in student_marks:
        total += mark

    average = total / len(student_marks)

    print(f"\nAverage marks: {average}")

    if average >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")