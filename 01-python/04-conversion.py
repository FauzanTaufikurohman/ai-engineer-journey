print(f"1. String → Integer\n2. String → Float\n3. Number → String")
choose = input("Choose a type:")

if choose == "1":
    age = int(input("Umur: "))
    print(type(age))
elif choose == "2":
    height = float(input("Tinggi: "))
    print(type(height))
    print(f"Tinggi: {height}")
elif choose == "3":
    age = 20
    message = "Umur saya " + str(age)
    print(message)