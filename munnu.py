# HERE IS A PYTHON PROGRAM TO BUILD A GRADE-BOOK TO TRACK STUDENT GRADES

# STUDENT PROGRESS TRACKING SYSTEM!!

students = {}

#Add_student function adds a new student

def add_student():
    name = input("Enter student's name: ")
    grades = {}                                 # Concatination means obtaining a new string that contains both of the original strings(+operator)
    for subject in ["Maths", "Physics", "English", "Chemistry","Sanskrit"]:
        grade = input("Enter grade for " + subject + ":")                    # By using concatenation
        grades[subject] = grade
        students[name] = grades

    print("Student "+name+" added.")


#  "Remove_student function removes an existing student.."

def remove_student():
    name = input("Enter student's name: ")
    if name in students:
        del students[name]
        print("Student "+name+" removed.")
    else:
        print("Student "+name+" not found.")


#  "Update_grade function updates a students grade for a specific subject ."

def update_grade():
    name = input("Enter student's name: ")
    if name in students:
        subject = input("Enter subject: ")
        grade = input("Enter new grade: ")
        students[name][subject] = grade
        print("Student's "+name+" grade for "+subject+" updated to "+grade+".")
    else:
        print("Student "+name+" not found.")


#   "Delete_subject deletes a subject for a student."

def delete_subject():
    name = input("Enter student's name: ")
    if name in students:
        subject = input("Enter subject to delete: ")
        if subject in students[name]:
            del students[name][subject]
            print("Subject "+subject+" deleted for student "+name+".")
        else:
            print("Subject "+subject+" not found for student "+name+".")
    else:
        print("Student "+name+" not found.")


# "Calculating percentage for a student ."

def calculate_percentage(grades):
    total = 0
    for grade in grades.values():
        total += float(grade)                  #" total = total + float(grade)"
    percentage = total / len(grades)
    return (percentage)                        # "percentage = (obtained grades/total grade * 100)"


#" Calculating average for a student ."

def calculate_average(grades):
    total = 0
    for grade in grades.values():
        total += float(grade)              #" total = total + float(grade)"
    average = total / len(grades)
    return (average)                       # "Average = (Sum of grades / Number of grades )"


# "Report displays student with their Grade , Percentage and Average....."

def report():
    name = input("Enter your name:")
    if name in students:

        for name, grades in students.items():

            print("Student: "+name+"")

            for subject, grade in grades.items():
                print(subject+" "+"grade"+" = "+grade)
            percentage = calculate_percentage(grades)
            average = calculate_average(grades)
            print("Percentage:",percentage,"%")
            print("Average:",average)
            if percentage >= 95:
                print(' Grade A')
                print("EXCELLENT!!")
            elif percentage < 95 and percentage >80 :
                print('Grade B')
                print("GOOD!!")
            else:
                print('Grade C')
                print("YOUR REPORT SHOULD BE IMPROVED!!")
    else:
        print("student not found!!")


# "This program runs in a loop until the user chooses to EXIT" .


while True:
    print("\n1. Add Student\n2. Remove Student\n3. Update Grade\n4. Delete Subject\n5. Report\n6. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        update_grade()
    elif choice == "4":
        delete_subject()
    elif choice == "5":
        report()
    elif choice == "6":
        break
    else:
        print("Invalid option. Please choose a valid option.")
 # "NOTE THAT THIS PROGRAM ASSUMES THAT THE GRADES ARE NUMERIC VALUES....."



# HERE IS A PYTHON PROGRAM TO BUILD A GRADE-BOOK TO TRACK STUDENT GRADES

# STUDENT PROGRESS TRACKING SYSTEM!!

students = {}

#Add_student function adds a new student

def add_student():
    name = input("Enter student's name: ")
    grades = {}                                 # Concatination means obtaining a new string that contains both of the original strings(+operator)
    for subject in ["Maths", "Physics", "English", "Chemistry","Sanskrit"]:
        grade = input("Enter grade for " + subject + ":")                    # By using concatenation
        grades[subject] = grade
        students[name] = grades

    print("Student "+name+" added.")


#  "Remove_student function removes an existing student.."

def remove_student():
    name = input("Enter student's name: ")
    if name in students:
        del students[name]
        print("Student "+name+" removed.")
    else:
        print("Student "+name+" not found.")


#  "Update_grade function updates a students grade for a specific subject ."

def update_grade():
    name = input("Enter student's name: ")
    if name in students:
        subject = input("Enter subject: ")
        grade = input("Enter new grade: ")
        students[name][subject] = grade
        print("Student's "+name+" grade for "+subject+" updated to "+grade+".")
    else:
        print("Student "+name+" not found.")


#   "Delete_subject deletes a subject for a student."

def delete_subject():
    name = input("Enter student's name: ")
    if name in students:
        subject = input("Enter subject to delete: ")
        if subject in students[name]:
            del students[name][subject]
            print("Subject "+subject+" deleted for student "+name+".")
        else:
            print("Subject "+subject+" not found for student "+name+".")
    else:
        print("Student "+name+" not found.")


# "Calculating percentage for a student ."

def calculate_percentage(grades):
    total = 0
    for grade in grades.values():
        total += float(grade)                  #" total = total + float(grade)"
    percentage = total / len(grades)
    return (percentage)                        # "percentage = (obtained grades/total grade * 100)"


#" Calculating average for a student ."

def calculate_average(grades):
    total = 0
    for grade in grades.values():
        total += float(grade)              #" total = total + float(grade)"
    average = total / len(grades)
    return (average)                       # "Average = (Sum of grades / Number of grades )"


# "Report displays student with their Grade , Percentage and Average....."

def report():
    name = input("Enter your name:")
    if name in students:

        for name, grades in students.items():

            print("Student: "+name+"")

            for subject, grade in grades.items():
                print(subject+grade)
            percentage = calculate_percentage(grades)
            average = calculate_average(grades)
            print("Percentage:",percentage,"%")
            print("Average:",average)
            if percentage >= 95:
                print(' Grade A')
                print("EXCELLENT!!")
            elif percentage < 95 and percentage >80 :
                print('Grade B')
                print("GOOD!!")
            else:
                print('Grade C')
                print("YOUR REPORT SHOULD BE IMPROVED!!")
    else:
        print("student not found!!")


# "This program runs in a loop until the user chooses to EXIT" .


while True:
    print("\n1. Add Student\n2. Remove Student\n3. Update Grade\n4. Delete Subject\n5. Report\n6. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        update_grade()
    elif choice == "4":
        delete_subject()
    elif choice == "5":
        report()
    elif choice == "6":
        break
    else:
        print("Invalid option. Please choose a valid option.")

 # "NOTE THAT THIS PROGRAM ASSUMES THAT THE GRADES ARE NUMERIC VALUES....."