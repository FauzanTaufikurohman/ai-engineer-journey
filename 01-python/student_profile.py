# BONUS CHALANGE
# Nama:
# Umur:
# Tinggi:
# Berat:

# ===== STUDENT PROFILE =====

# Nama       : Fauzan
# Umur       : 20
# Tinggi     : 170 cm
# Berat      : 65 kg
# BMI        : ...
# Status     : ...

input_name = input("Masukkan nama: ")
input_age = int(input("Masukkan umur: "))
input_height = float(input("Masukkan tinggi badan (cm): "))
input_weight = float(input("Masukkan berat badan (kg): "))

bmi = input_weight / ((input_height / 100) ** 2)
if bmi < 18.5:
    status = "Kekurangan berat badan"
elif 18.5 <= bmi < 25:
    status = "Normal"
elif 25 <= bmi < 30:
    status = "Kelebihan berat badan"
else:
    status = "Obesitas"

print("\n===== STUDENT PROFILE =====")
print(f"Nama       : {input_name}")
print(f"Umur       : {input_age}")
print(f"Tinggi     : {input_height} cm")
print(f"Berat      : {input_weight} kg")
print(f"BMI        : {bmi:.2f}")
print(f"Status     : {status}")