# LAB 3 - STUDENT RECORD DATA MANAGEMENT USING DATA STRUCTURES

def student_record_management():

    # Step 1: Input Collection
    students = []

    # Adding Student Records using List of Dictionaries
    students.append({
        "name": "Priya",
        "age": 20,
        "grades": [85, 90, 78]
    })

    students.append({
        "name": "Rahul",
        "age": 21,
        "grades": [72, 88, 91]
    })

    students.append({
        "name": "Anita",
        "age": 19,
        "grades": [95, 89, 92]
    })

    # Step 2: Record Management with Lists and Dictionaries
    print("=== STUDENT RECORDS ===\n")

    for student in students:

        print("Name:", student["name"])

        print("Age:", student["age"])

        print("Grades:", student["grades"])

        print("-----------------------")

    # Step 3: Event Participation Analysis using Sets
    event_A = {"Priya", "Rahul", "Anita", "Kiran"}

    event_B = {"Rahul", "Anita", "Sneha"}

    # Common Participants
    common_participants = event_A & event_B

    # All Participants
    all_participants = event_A | event_B

    # Only Event A Participants
    only_event_A = event_A - event_B

    # Step 4: Output Display
    print("\n=== EVENT PARTICIPATION ANALYSIS ===")

    print("Common Participants:", common_participants)

    print("All Participants:", all_participants)

    print("Only Event A Participants:", only_event_A)


