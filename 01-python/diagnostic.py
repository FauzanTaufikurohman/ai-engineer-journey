
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def clarify_scores(scores):
    if(scores>= 90):
        return "Excellent"
    elif(scores>= 80):
        return "Good"
    elif(scores>= 70):
        return "Average"
    else:
        return "Poor"
def get_passed_students(students):
    passed_students = []
    for student in students:
        if student["score"] >= 80:
            passed_students.append(student)
    return passed_students

def processing_numbers(numbers, even=True):
    if even:
        return [num for num in numbers if num % 2 == 0]
    else:
        return [num for num in numbers if num % 2 != 0]
    
choice = input("Please enter your choice: ")

if choice == "1":
    #Soal Pertama
    print("You selected option 1.")
    name = "Fauzan"
    experience = 1
    learning_ai = True
    
    print(f"Name : {name}")
    print(f"Experience : {experience}")
    print(f"Learning AI : {learning_ai}")
elif choice == "2":
    #Soal Kedua
    print("You selected option 2.")
    scores = [85, 90, 78, 92, 88]
        
    print(f"Banyak Scores:{len(scores)}")
    print(f"Nilai Tertinggi Scores:{max(scores)}")
    print(f"Nilai Terendah Scores:{min(scores)}")
    print(f"Rata-rata Scores:{sum(scores)/len(scores)}")
elif choice == "3":
    #Soal Ketiga
    print("You selected option 3.")
    numbers = [10, 20, 30, 40, 50]
    average = calculate_average(numbers)
    print(f"Average of the numbers: {average}")
elif choice == "4":
    #Soal Keempat
    print("You selected option 4.")
    student = {
        "name": "Fauzan",
        "age": 25,
        "skills": ["Python", "Laravel", "Flutter"]
    }
    print(f"Student Name: {student['name']}")
    print(f"Student Age: {student['age']}")
    print(f"Student Skills: {student['skills'][0]}")
elif choice == "5":
    #Soal Kelima Sum tanpa menggunakan fungsi sum()
    print("You selected option 5.")
    numbers = [10, 20, 30, 40, 50]
    total = 0
    for number in numbers:
        total += number
    print(f"Sum Value: {total}")
elif choice == "6":
    #Soal Keenam
    print("You selected option 6.")
    scores = [85, 90, 78, 92, 20]
    for score in scores:
        result = clarify_scores(score)
        print(f"Score: {score}, Result: {result}")
elif choice == "7":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    genap = processing_numbers(numbers, even=True)
    ganjil = processing_numbers(numbers, even=False)
    
    print(f"Even Numbers: {genap}")
    print(f"Odd Numbers: {ganjil}")
elif choice == "8":
    #Soal Kedelapan
    students = [
        {"name": "Andi", "score": 80},
        {"name": "Budi", "score": 65},
        {"name": "Citra", "score": 90},
    ]
    get_passed_students(students)
elif choice == "9":
    #Bonus Test
    students = [
        {"name": "Andi", "score": 80},
        {"name": "Budi", "score": 55},
        {"name": "Citra", "score": 90},
        {"name": "Deni", "score": 45},
    ]
    result = get_passed_students(students)
    print(result)
    
else:
    print("Invalid choice. Please select either 1, 2, 3, or 4.")
    
    