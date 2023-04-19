#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de 
# representação que cada estado teve dentro do valor total mensal da distribuidora.

fat_sp = 67836.43
fat_rj = 36678.66
fat_mg = 29229.88
fat_es = 27165.48
fat_outros = 19849.53

faturamento_total = fat_sp + fat_rj + fat_mg + fat_es + fat_outros

print("O percentual de representação do faturamento da distribuidora, por estado é:")
print(f"SP = {round((fat_sp/ faturamento_total)*100, 2)}%")
print(f"RJ = {round((fat_rj / faturamento_total)*100, 2)}%")
print(f"MG = {round((fat_mg / faturamento_total)*100, 2)}%")
print(f"ES = {round((fat_es / faturamento_total)*100, 2)}%")
print(f"Outros = {round((fat_outros / faturamento_total)*100, 2)}%")



