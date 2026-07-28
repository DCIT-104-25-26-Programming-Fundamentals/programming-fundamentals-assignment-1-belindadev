# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


students = []


def calculate_average(scores):
    """Calculates and returns the average of a list of scores rounded to 2 decimal places."""
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def add_student():
    """Prompts the user to enter student details and adds them to the records."""
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()

    # Get valid number of scores
    while True:
        try:
            num_scores = int(input("How many scores? "))
            if num_scores > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Collect individual scores
    scores = []
    for i in range(1, num_scores + 1):
        while True:
            try:
                score = float(input(f"Enter score {i}: "))
                scores.append(score)
                break
            except ValueError:
                print("Invalid score. Please enter a numerical value.")

    # Create dictionary and append to list
    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_all_students():
    """Displays all student records in a formatted table."""
    if not students:
        print("\nNo students have been added yet.")
        return

    print("\n" + "-" * 65)
    print(f"{'Name':<20} {'ID':<12} {'Scores':<18} {'Average':<10}")
    print("-" * 65)

    for student in students:
        scores_str = ", ".join(str(int(s) if s.is_integer() else s) for s in student["scores"])
        avg = calculate_average(student["scores"])
        print(f"{student['name']:<20} {student['id']:<12} {scores_str:<18} {avg:<10.2f}")

    print("-" * 65)


def calculate_student_average():
    """Finds a student by ID and displays their average score."""
    if not students:
        print("\nNo students found in the database.")
        return

    search_id = input("Enter student ID: ").strip()
    
    for student in students:
        if student["id"] == search_id:
            avg = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {avg:.2f}")
            return

    print(f"Error: Student with ID '{search_id}' not found.")


def main():
    """Main menu loop to handle user interaction."""
    while True:
        print("\n==================================================")
        print("          STUDENT RECORD SYSTEM MENU              ")
        print("==================================================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            calculate_student_average()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 4.")


if __name__ == "__main__":
    main()