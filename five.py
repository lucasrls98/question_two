#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência 
# ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

string = input("Digite sua string aqui: ")


lista_chars = list(string)


inicio = 0
fim = len(lista_chars) - 1


while fim > inicio:
    
    aux = lista_chars[inicio]
    lista_chars[inicio] = lista_chars[fim]
    lista_chars[fim] = aux
    
    
    inicio += 1
    fim -= 1


string_invertida = "".join(lista_chars)


print("String original:", string)
print("String invertida:", string_invertida)
