from Student_Registration import student_registration
from Course_Enrollment import course_enrollment
from Student_Records import student_record_management
from Search_and_Sort import sorting_searching_student_ids
from Fee_Calculation import fee_management
from File_handling import file_handling
from Exception_Handling import scan_directory
while True:

    print("\n========== SMART CAMPUS INFORMATION SYSTEM ==========")

    print("1. Student Registration")

    print("2. Course Enrollment")

    print("3. Student Records Management")

    print("4. Search and Sort Student IDs")

    print("5. Fee Calculation")

    print("6. File Handling")

    print("7. Directory Scanning")

    print("8. Performance Analytics")

    print("9. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        student_registration()
    elif choice == "2":
        course_enrollment()
    elif choice == "3":
        student_record_management()
    elif choice == "4":
        sorting_searching_student_ids()
    elif choice == "5":
        fee_management()
    elif choice == "6":
        file_handling()
    elif choice == "7":
        path = input("Enter directory path to scan: ")
        scan_directory(path)
    elif choice == "8":
        import Performance_Analytics
    elif choice == "9":
        print("Exiting Smart Campus System...")
        break
    else:
        print("Invalid Choice! Please try again.")
