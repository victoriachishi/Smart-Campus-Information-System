
def file_handling():
    with open("students_Record.txt", "w") as file:
        file.write("ID, Name, Marks\n")
        file.write("101, Arjun, 85\n")
        file.write("102, Meera, 92\n")
        file.write("103, Ravi, 76\n")
        file.write("104, Anita, 89\n")

    print("Student Record written to file Successfully!!")

    print("Reading stored data:")
        
    with open("students_Record.txt", "r") as file:
        records = file.readlines()
        for record in records:
            print(record.strip())

    print("Generating Report!")

    total_students = 0
    total_marks = 0
    highest_marks = -1
    top_student = ""

    for record in records[1:]:
        parts = record.strip().split(",")
        student_id = parts[0]
        name = parts[1]
        marks = int(parts[2])

        total_students = total_students + 1
        total_marks = total_marks + marks

        if marks > highest_marks:
            highest_marks = marks
            top_student = name

    avg_marks = total_marks / total_students

    print("Total Students: ", total_students)
    print("Average Marks: ", avg_marks)
    print("Top student: ", top_student, "with", highest_marks, "marks.")




