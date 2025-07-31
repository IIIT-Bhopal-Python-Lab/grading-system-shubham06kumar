# Grading System

def grading_sys():

    marks = input()

    # Exit Condition
    if marks.upper() == "EXIT":
        return "Exiting the program."
    
    # Validate input is numeric
    if not marks.isdigit():
        return "Invalid input. Please enter a number between 0 and 100."
    
    # Convert input String into Integer
    marks = int(marks)

    # Check if marks are in valid range
    if marks < 0 or marks > 100:
        print("Invalid input. Marks should be between 0 and 100.")

    # Grading Logic 
    elif marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 40:
        return 'D'
    else:
        return 'F'
    
    
if __name__ == "__main__":
    grade=grading_sys()
    print(grade)
    
