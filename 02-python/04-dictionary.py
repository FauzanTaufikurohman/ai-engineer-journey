student = {
    "name": "Fauzan",
    "age": 25,
    "role": "AI Engineer"
}

print(student["name"])

student["age"] = 26
student["city"] = "Jakarta"
print(student)
del student["city"]
print(student)

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