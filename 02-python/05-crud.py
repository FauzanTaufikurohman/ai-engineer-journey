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
    }
]
new_student = {
    "id": 3,
    "name": "Citra",
    "score": 95
}

students.append(new_student)

for student in students:
    print(student)
    
for student in students:
    print(
        f"{student['id']} - "
        f"{student['name']} - "
        f"{student['score']}"
    )

for student in students:
    if student["id"] == 2:
        student["score"] = 80

for student in students:
    if student["id"] == 2:
        students.remove(student)
        break