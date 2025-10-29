usuarios =["ana", "", "", "marcos", "julia123", "marcos@3", "gabrielly"]

for usuario in usuarios:
    if not usuario:
        continue
    for letra in usuario:
        if letra.isspace():
            print(f"Ignorando '{usuario}', (contém espaços vazios)")
            break
        if letra.isalpha():
            print(f"Ignorando '{usuario}', (contém espaços vazios)")
            break
else:
    print(f"Cadastrando usuário: {usuario}")