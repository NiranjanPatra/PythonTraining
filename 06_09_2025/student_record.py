import os

def create_student_database(file):
    with open(file, "w") as f:
        while True:
            name = input("Enter name: ")
            if name == "exit":
                break
            roll_number = int(input("enter roll number: "))
            marks = int(input("Ener marks"))

            data = {
                "name" : name,
                "roll_number": roll_number,
                "marks": marks
            }
            f.write(str(data))
            f.write("\n")

def read_student_database(file):
    with open(file, "r") as f:
        datas = f.readlines()
        for data in datas:
            student = eval(data)
            print(student)

def rename_student_database(fileOriginal, fileNew):
    try:
        os.rename(fileOriginal, fileNew)
    except Exception as e:
        print("Exception :", e)
    print(f"File renamed '{fileOriginal}' to '{fileNew}' ")

def move_student_database(file, dir):
    if os.path.exists(dir):
        print("The directory already exists")
    else:
        os.makedirs(dir)
    
    new_path = os.path.join(dir, os.path.basename(file))
    try:
        os.rename(file, new_path)
    except Exception as e:
        print("File already exists")

    print("\n")
    print("List all files in the directory '{dir}' ")
    items = os.listdir(dir)
    print("All files: ", items)

def delete_db_and_dir(file, dir):
    new_file_path = os.path.join(dir, os.path.basename(file))
    os.remove(new_file_path)
    os.rmdir(dir)

create_student_database("students.txt")
print("Student database created\n")

print("Student database display:")
print("*" * 50)
read_student_database("students.txt")
print("*" * 50)

print("\n")
rename_student_database("students.txt", "student_records.txt")

print("\n")
move_student_database("student_records.txt", "SchoolData")

delete_db_and_dir("student_records.txt", "SchoolData")
