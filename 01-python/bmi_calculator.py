#formula  BMI = weight / (height ** 2)
# BMI < 18.5
# 18.5 – 24.9
# 25 – 29.9
# >= 30


weight = float(input("Masukkan berat badan (kg): "))
height = float(input("Masukkan tinggi badan (m): "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"BMI Anda: {bmi:.2f} (Kekurangan berat badan)")
elif 18.5 <= bmi < 25:
    print(f"BMI Anda: {bmi:.2f} (Normal)")
elif 25 <= bmi < 30:
    print(f"BMI Anda: {bmi:.2f} (Kelebihan berat badan)")
else:
    print(f"BMI Anda: {bmi:.2f} (Obesitas)")