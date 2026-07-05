# Search In a List: Stores and then search item in a list.

students_list = []

def search_student(student):
    if student in students_list:
        return True
    return False


while True:
    student = input("Add student to the list (q to quit): ")
    if student.lower() == 'q':
        break

    students_list.append(student.lower())


user_search = input("Hey, search student in a list: ")
if search_student(user_search.lower()):
    print("Student found.")
else: print("Sorry, student doesn't exist in the list.")