

inventario = ["elmo", "chapeu", "espada", "botas"]
busca = input("Digite um item: ")
for item in inventario:
    if item == busca:
        print(f"Item {busca.capitalize()} foi encontrada !")
        break
else:
    print("Item não foi encontrado")