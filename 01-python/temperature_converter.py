print("1. Konversi Suhu: Celsius ke Fahrenheit\n2. Konversi Suhu: Fahrenheit ke Celsius")

choice = input("Pilih konversi (1 atau 2): ")

if choice == "1":
    celsius = float(input("Masukkan suhu Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
elif choice == "2":
    fahrenheit = float(input("Masukkan suhu Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
else:
    print("Pilihan tidak valid.")
    exit()
print(f"{celsius}°C = {fahrenheit}°F")