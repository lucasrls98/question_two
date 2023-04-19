#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json


with open('faturamento.json', 'r') as file:
    dados = json.load(file)


faturamento_diario = [dia['faturamento'] for dia in dados['dias']]


menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)


dias_com_faturamento = [dia['faturamento'] for dia in dados['dias'] if dia['faturamento'] > 0]
media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)


dias_acima_da_media = sum(1 for dia in dias_com_faturamento if dia > media_faturamento)


print(f"Menor faturamento diário: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento diário: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento diário acima da média: {dias_acima_da_media}")
