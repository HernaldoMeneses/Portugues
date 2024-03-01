title = '''O que é:
    Gramática Normativa
        Norma Culta
            Registro culto etc.?
'''
print("\n")
print(title)
print("\n")


file_path = 'into.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

for ln in lines:
    print(ln.strip())

print("\n")