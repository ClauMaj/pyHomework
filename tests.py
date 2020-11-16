
lista = ['a' , 'b' , 'c' , 'd' , 'e', 'f']
for item in lista:
    lista.append(item)
    del lista[0]

print(lista)