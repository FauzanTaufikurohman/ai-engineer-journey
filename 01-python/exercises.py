# SOAL 1
# name
# age
# height
# is_student

# SOAL 2
# x = 10
# y = 10.5
# z = "10"
# active = True
# print masing masing tipe data dari variabel di atas

# SOAL 3
# UPPERCASE
# Hilangkan whitespace di awal dan akhir string
# print masing masing tipe data dari variabel di atas

# SOAL 4
# a = 20
# b = 6
# TAMPILKAN
# Penjumlahan
# Pengurangan
# Perkalian
# Pembagian
# Sisa pembagian

# SOAL 5
# price = "15000"
# quantity = "3"
# HITUNG total harga dengan mengkonversi price dan quantity menjadi integer, lalu tampilkan total harga

# SOAL 6
# name = 20
# is_adult = True
# if umur >= 18 and is_adult:

# SOAL 7
# +
# -
# *
# /
# input USER

# SOAL 8
# celcius to farenheit

# SOAL 9
# BMI

print("1. Soal 1\n2. Soal 2\n3. Soal 3\n4. Soal 4\n5. Soal 5\n6. Soal 6\n7. Soal 7\n8. Soal 8\n9. Soal 9\n10. Soal 10\n11. Bonus Soal 1\n12. Bonus Soal 2\n13. Bonus Soal 3\n14. Bonus Soal 4\n15. Bonus Soal 5\n16. Bonus Soal 6\n17. Bonus Soal 7\n18. Bonus Soal 8\n19. Bonus Soal 9\n20. Bonus Soal 10")

choice = input("Pilih soal (1-20): ")

if choice == "1":
    name = "Fauzan"
    age = 20
    height = 1.75
    is_student = True
    print(f"Name: {name}\nAge: {age}\nHeight: {height}\nIs Student: {is_student}")
elif choice == "2":
    x = 10
    y = 10.5
    z = "10"
    active = True
    print(f"x: {x}, type: {type(x)}\ny: {y}, type: {type(y)}\nz: {z}, type: {type(z)}\nactive: {active}, type: {type(active)}")
elif choice == "3":
    name = "  Fauzan  "
    uppercase_name = name.upper().strip()
    stripped_name = name.strip()
    print(f"Uppercase: {uppercase_name}\nStripped: {stripped_name}")
elif choice == "4":
    a = 20
    b = 6
    print(f"Penjumlahan: {a + b}\nPengurangan: {a - b}\nPerkalian: {a * b}\nPembagian: {a / b}\nSisa Pembagian: {a % b}")
elif choice == "5":
    price = "15000"
    quantity = "3"
    total_price = int(price) * int(quantity)
    print(f"Total Harga: {total_price}")
elif choice == "6":
    age = 20
    is_adult = True
    if age >= 18 and is_adult:
        print("You are an adult.")
    else:
        print("You are not an adult.")
elif choice == "7":
    num1 = float(input("Masukkan angka pertama: "))
    operator = input("Masukkan operator (+, -, *, /): ")
    num2 = float(input("Masukkan angka kedua: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        result = None
        print("Operator tidak valid.")
    if result is not None:
        print(f"Hasil: {result}")
elif choice == "8":
    celsius = float(input("Masukkan suhu Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
elif choice == "9":
    weight = float(input("Masukkan berat badan (kg): "))
    height = float(input("Masukkan tinggi badan (m): "))
    bmi = weight / (height ** 2)
    print(f"BMI Anda: {bmi}")