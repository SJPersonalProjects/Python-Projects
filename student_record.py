# Student Record using dictionary.

student = {}

student["name"] = input("Enter student's name: ")
student["age"] = int(input("Enter student's age: "))
student["city"] = input("Enter student's city: ")

print("\n==== Student Record ====")
print(f"Name : {student['name']}")
print(f"Age : {student['age']}")
print(f"City : {student['city']}")