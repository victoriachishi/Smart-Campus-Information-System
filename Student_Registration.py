# LAB 1 - STUDENT REGISTRATION AND GRADE EVALUATION

def student_registration():

    # Step 1: Input Collection
    student_name = input("Enter student name: ")

    score = float(input("Enter exam score (0-100): "))

    # Step 2: Grade Evaluation
    if score >= 90 and score <= 100:

        grade = "A"
        remark = "Excellent"

    elif score >= 75:

        grade = "B"
        remark = "Very Good"

    elif score >= 60:

        grade = "C"
        remark = "Good"

    elif score >= 40:

        grade = "D"
        remark = "Average"

    else:

        grade = "F"
        remark = "Needs Improvement"

    # Step 3: Output Display
    print("\n--- STUDENT REPORT ---")

    print("Name:", student_name)

    print("Score:", score)

    print("Grade:", grade)

    print("Performance Remark:", remark)
