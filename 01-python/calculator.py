num1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+ - * /): ")
num2 = float(input("Masukkan angka kedua: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "%":
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2
elif operator == "//":
    result = num1 // num2
else:
    result = None
    print("Operator tidak valid.")

if result is not None:
    print(f"Hasil: {result}")