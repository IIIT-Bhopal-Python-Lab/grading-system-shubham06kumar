# Grading System
import sys

marks = input()

if marks.upper() == "EXIT":
    print("Exiting the program.")
    sys.exit()


if not marks.isdigit():
    print("Invalid input. Please enter a number between 0 and 100.")
    sys.exit()

marks = int(marks)

if marks < 0 or marks > 100:
    print("Invalid input. Marks should be between 0 and 100.")
elif marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")
