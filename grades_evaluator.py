# Grades evaluator.

student_marks = float(input("Enter your marks: "))

if student_marks >= 0 and student_marks <= 35:
    print(f"F Grade. {student_marks} marks. Too low.")
elif student_marks > 35 and student_marks <= 45:
    print(f"D Grade. {student_marks} marks. Barely passed.")
elif student_marks > 45 and student_marks <= 55:
    print(f"C Grade. {student_marks} marks. Need to work harder.")
elif student_marks > 55 and student_marks <= 75:
    print(f"B Grade. {student_marks} marks. Good. work on strategies.")
elif student_marks > 75 and student_marks <= 92:
    print(f"A Grade. {student_marks} marks. Wow, you're flourishing.")
elif student_marks > 92 and student_marks <= 100:
    print(f"A+ Grade. {student_marks} marks. You just nailed it.")
else :
    print(f"Please enter correct marks.")