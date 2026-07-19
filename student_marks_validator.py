# Student Marks Validator.

import traceback

resultsFile = open("StudentResults.txt", "w")

totalMarks = 0
studentCount = 0

while True:

    try:
        name = input("Enter student name (or 'done' to finish): ")

        if name.lower() == 'done':
            break

        marks = int(input("Enter marks (0 - 100): "))

        # Internal assumption.
        assert studentCount >= 0

        # Validate user input
        if name == "":
            raise ValueError("Student name cannot be empty.")

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")


        resultsFile.write(name + " : " + str(marks) + "\n")

        totalMarks += marks
        studentCount += 1

    except ValueError as error:
        print("Error", error)

    except AssertionError:
        print("Assertion failed.")
    
    except Exception:
        print("Unexpected error occurred.")

        errorFile = open("Errorlog.txt", "a")
        errorFile.write(traceback.format_exc())
        errorFile.write("\n" + "-" * 50 + "\n")
        errorFile.close()

if studentCount > 0:

    average = totalMarks / studentCount
    resultsFile.write("\n")
    resultsFile.write("Average Marks: " + str(round(average, 2)))

resultsFile.close()

print("Results saved to StudentResults.txt")