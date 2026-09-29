skills = {"python", "java", "c++"}

print(skills)

# Sangat berguna untuk menghapus duplikat dari sebuah list

# OPERASI SET

skills.add("javascript")  # Menambahkan elemen baru
skills.remove("java")  # Menghapus elemen

print("Python" in skills)  # Output: True

a = {"Python", "Laravel", "Docker"}
b = {"Python", "Flutter", "Docker"}

# Intersection
print(a & b)

# Union
print(a | b)

