print(f"1. String\n2. Integer\n3. Float\n4. Boolean")
choose = input("Choose a type:")

if choose == "1":
    name = "Fauzan"
    print(type(name))
elif choose == "2":
    age = 20
    print(type(age))
elif choose == "3":
    pi = 3.14
    print(type(pi))
elif choose == "4":
    is_learning_ai = True
    print(type(is_learning_ai))