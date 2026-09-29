
students = [
    {"name": "Andi", "score": 85},
    {"name": "Budi", "score": 70},
    {"name": "Citra", "score": 95},
]
filtered_students = []

for student in students:
    if student["score"] >= 80:
        filtered_students.append(student)

print(filtered_students)

filtered_students = [
    student
    for student in students
    if student["score"] >= 80
]
print(filtered_students)