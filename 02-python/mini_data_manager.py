# ========================
#      DATA MANAGER
# ========================

# 1. Lihat Data
# 2. Tambah Data
# 3. Update Data
# 4. Hapus Data
# 5. Cari Data
# 6. Filter Data
# 7. Urutkan Data
# 8. Keluar


def show_students(students):
    for student in students:
        print(student)

def add_student(students):
    new_student = {
        "id" : 3,
        "nama" : "Jofan",
        "score" : 93
    }
    
    students.append(new_student)
    print(students)

def update_student(students):
    for student in students:
        if student['id'] == 2:
            student["score"] = 10
    
    print(students)


def delete_student(students):
    for student in students:
        if student["id"] == 2:
            students.remove(student)
    print(students)

def search_student(students):
    keyword = "Citra"
    
    for student in students:
        if student["name"].lower() == keyword.lower():
            print(student)
    
    keyword = "cit"
    for student in students:
        if keyword.lower() in student["name"].lower():
            print(student)


def filter_students(students):
    filter_students = []
    
    for student in students:
        if student["score"] >= 80:
            filter_students.append(student)
    
    print(filter_students)


def sort_students(students):
    sorted_students = (sorted(
        students, key=lambda student: student["score"]
    ))
    print(sorted_students)
    
    sorted_students = sorted(
        students,
        key = lambda student: student["score"],
        reverse = True
    )
    
    print(sorted_students)
    
students = [
    {
        "id": 1,
        "name": "Andi",
        "score": 85
    },
    {
        "id": 2,
        "name": "Budi",
        "score": 70
    },
    {
        "id": 3,
        "name": "Citra",
        "score": 95
    }
]

while True:
    print("\n=== DATA MANAGER ===")
    print("1. Lihat Data")
    print("2. Tambah Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Filter Data")
    print("7. Urutkan Data")
    print("8. Keluar")

    choice = input("Pilih menu: ")

    if choice == "1":
        show_students(students)

    elif choice == "2":
        add_student(students)

    elif choice == "3":
        update_student(students)

    elif choice == "4":
        delete_student(students)

    elif choice == "5":
        search_student(students)

    elif choice == "6":
        filter_students(students)

    elif choice == "7":
        sort_students(students)

    elif choice == "8":
        break

    else:
        print("Menu tidak tersedia.")