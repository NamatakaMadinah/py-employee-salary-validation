# student's biography
print("STUDENT'S BIOGRAPHY")
students_list =[]
n=int(input("Enter students name list:"))
print("\n")
for i in range(0,n):
    NAME = str(input("Enter student's name: "))
    students_list.append(NAME)
    REGISTRATION_NUMBER = str(input("REGISTRATION NUMBER: "))
    students_list.append(REGISTRATION_NUMBER)
    AGE = int(input("Age: "))
    students_list.append(AGE)
    NATIONALITY = str(input("Enter the student's Nationality: "))
    students_list.append(NATIONALITY)
    PHONE_NUMBER = int(input("Enter the student's phone number: "))
    students_list.append(PHONE_NUMBER)
    BATCH_YEAR = int(input("enter the students year of study: "))
    students_list.append(BATCH_YEAR)
    COURSE = str(input("Enter a students course of study: "))
    students_list.append(COURSE)
    PROGRAM = str(input("Enter students program admitted in: "))
    students_list.append(PROGRAM)
    GRADUATION_YEAR = int(input("enter the expected year of graduation: "))
    students_list.append(GRADUATION_YEAR)
    print(f"Student Name: {NAME}")
    print(f"Student RegistrationNumber: {REGISTRATION_NUMBER}")
    print(f"Student Age: {AGE}")
    print(f"Student Nationality: {NATIONALITY}")
    print(f"Student PhoneNumber: {PHONE_NUMBER}")
    print(f"Student Currentyearofstudy: {BATCH_YEAR}")
    print(f"Student Course: {COURSE}")
    print(f"Student AdmittedCourse: {PROGRAM}")
    print(f"Student GraduationYear: {GRADUATION_YEAR}")










