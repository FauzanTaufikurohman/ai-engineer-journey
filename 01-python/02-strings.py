print("Pilih string yang ingin dicetak:")
choose = input("1. String concatenation\n2. String methods\n3. String indexing\n4. String slicing\nPilih (1-4): ")

if choose == "1":
    name = "Fauzan"
    city = "Jakarta"
    print("String concatenation:")
    print(name + " tinggal di " + city)
elif choose == "2":
    name = "Fauzan"
    print("String methods:")
    print(name.upper())
    print(name.lower())
    print(name.capitalize())
elif choose == "3":
    name = "Fauzan"
    print("String indexing:")
    print(name[0])  # F
    print(name[1])  # a
    print(name[2])  # u
elif choose == "4":
    name = "Fauzan"
    print("String slicing:")
    print(name[0:3])  # Fau
    print(name[3:])   # zan
    print(name[:3])   # Fau
