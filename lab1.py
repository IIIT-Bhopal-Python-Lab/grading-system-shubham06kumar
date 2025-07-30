# Grading System
while True:
    marks = input("Enter marks (0-100) or type 'Exit' to quit: ")

    if marks.upper() == "EXIT":
        print("Exiting the program.")
        break

    if not marks.isdigit():
        print("Invalid input. Please enter a number between 0 and 100.")
        continue

    mark = int(marks)

    if marks < 0 or marks > 100:
        print("Invalid input. Marks should be between 0 and 100.")
    elif marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 40:
        print("Grade D")
    else:
        print("Grade F")
