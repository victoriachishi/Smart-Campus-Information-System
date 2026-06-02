# LAB 2 - COURSE ENROLLMENT MANAGEMENT SYSTEM

def course_enrollment():

    # Step 1: Input Collection
    courses = []

    max_courses = 5

    print("=== COURSE ENROLLMENT SYSTEM ===")

    while True:

        if len(courses) >= max_courses:

            print("Maximum course limit reached!")
            break

        course_name = input("Enter course name (or 'done' to finish): ")

        if course_name.lower() == "done":
            break

        credits = input("Enter credit value: ")

        # Step 2: Validation using if-elif-else
        if not credits.isdigit():

            print("Invalid credit value! Skipping entry...\n")
            continue

        credits = int(credits)

        if credits <= 0:

            print("Credit must be positive! Skipping entry...\n")
            continue

        # Valid Entry
        courses.append((course_name, credits))

        print(f"Course '{course_name}' with {credits} credits added.\n")

    # Step 3: Output Display
    print("\n--- ENROLLMENT REPORT ---")

    for course, credit in courses:

        print(f"Course: {course}, Credits: {credit}")

    print("\nTotal courses enrolled:", len(courses))

