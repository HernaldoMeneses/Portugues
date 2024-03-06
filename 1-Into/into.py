title = '''O que é:
    Gramática Normativa
        Norma Culta
            Registro culto etc.?
'''

'''
Gramática Normativa
    Sistematização do registro culto da língua
        Fonológico (som)
        Mórfico (forma)
        Sintático (organização)
        Semântico (sentido)
        Léxico (vocabulário)
        Discursivo (uso prático)
        Estilístico (Criatividade)
Norma Culta, Registro Culto, Gramática Normativa
    Modelo de Utilização por Escritores do Romantismo para cá (Uma forma)
    *obs - Não necessariamente o melhor
Objetivos da Lingua
    Comunicação e Interação
Vantagens da Norma Culta
    Unidade Linguistica
    Ascenção Profissional
    Instrumento de Situações formais

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