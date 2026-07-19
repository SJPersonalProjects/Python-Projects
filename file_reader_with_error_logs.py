# File Reader with Error Logs.

import traceback

# Ask teh user for the filename.
filename = input("Enter the text file name: ")

try:

    # Ope and read the file.
    file = open(filename, "r")

    print("\nFile Contents: ")
    print("-" * 30)

    print(file.read())

    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except Exception:
    print("An unexpected error occurred.")
    print("Saving error information...")

    errorFile = open("Errorlog.txt", "a")

    errorFile.write(traceback.format_exc())
    errorFile.write("\n" + "-" * 50 + "\n")

    errorFile.close()

    print("Error saved to ErrorLog.txt.")
