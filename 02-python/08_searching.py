keyword = "Citra"

for student in students:
    if student["name"].lower() == keyword.lower():
        print(student)
        
keyword = "cit"

for student in students:
    if keyword.lower() in student["name"].lower():
        print(student)