students = [
    {"name": "Andi", "score": 85},
    {"name": "Budi", "score": 70},
    {"name": "Citra", "score": 95},
]

sorted_students = sorted(
    students,
    key=lambda student: student["score"]
)
print(sorted_students)

sorted_students = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)
print(sorted_students)