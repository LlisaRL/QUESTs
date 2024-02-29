import json
# Colocando os dados do arquivo dados.json como uma string no python
infos_json = '''[
  {
    "dia": 1,
    "valor": 22174.1664
  },
  {
    "dia": 2,
    "valor": 24537.6698
  },
  {
    "dia": 3,
    "valor": 26139.6134
  },
  {
    "dia": 4,
    "valor": 0
  },
  {
    "dia": 5,
    "valor": 0
  },
  {
    "dia": 6,
    "valor": 26742.6612
  },
  {
    "dia": 7,
    "valor": 0
  },
  {
    "dia": 8,
    "valor": 42889.2258
  },
  {
    "dia": 9,
    "valor": 46251.174
  },
  {
    "dia": 10,
    "valor": 11191.4722
  },
  {
    "dia": 11,
    "valor": 0
  },
  {
    "dia": 12,
    "valor": 0
  },
  {
    "dia": 13,
    "valor": 3847.4823
  },
  {
    "dia": 14,
    "valor": 373.7838
  },
  {
    "dia": 15,
    "valor": 2659.7563
  },
  {
    "dia": 16,
    "valor": 48924.2448
  },
  {
    "dia": 17,
    "valor": 18419.2614
  },
  {
    "dia": 18,
    "valor": 0
  },
  {
    "dia": 19,
    "valor": 0
  },
  {
    "dia": 20,
    "valor": 35240.1826
  },
  {
    "dia": 21,
    "valor": 43829.1667
  },
  {
    "dia": 22,
    "valor": 18235.6852
  },
  {
    "dia": 23,
    "valor": 4355.0662
  },
  {
    "dia": 24,
    "valor": 13327.1025
  },
  {
    "dia": 25,
    "valor": 0
  },
  {
    "dia": 26,
    "valor": 0
  },
  {
    "dia": 27,
    "valor": 25681.8318
  },
  {
    "dia": 28,
    "valor": 1718.1221
  },
  {
    "dia": 29,
    "valor": 13220.495
  },
  {
    "dia": 30,
    "valor": 8414.61
  }
]'''

# Transformando string em um dicionário meio da variável 'dados'
dados = json.loads(infos_json)

# Sendo
for item in dados:
    dia = item["dia"]
    valores = item["valor"]

# Contabiliza quantos dias tiveram algum faturamento
def dias_faturados():
    dias_faturados = 0
    for item in dados:
        if item["valor"] > 0:
            dias_faturados += 1
    return dias_faturados

dias_totais = dias_faturados()

# Faz o cálculo da média, analiza e contabiliza quantos dias do mês o faturamento
# foi maior que a média mensal
def calcular_media():
    total_valores = 0
    total_dias = 0
    for item in dados:
        valor = item["valor"]
        if valor > 0:
            total_valores += valor
            total_dias += 1
    media_mensal = total_valores / total_dias
    return media_mensal

def contar_dias_acima_da_media(media):
    dias_acima_media = 0
    for item in dados:
        valor = item["valor"]
        if valor > media:
            dias_acima_media += 1
    return dias_acima_media

media_mensal = calcular_media()
dias_acima_media = contar_dias_acima_da_media(media_mensal)

print(f"Dias acima da média: {dias_acima_media}")

# Abaixo conseguimos usar min e max para descobrir quais foram os valores
# maiores e menores do faturamento
valores_faturamento = [item["valor"] for item in dados]
menor_valor = min(valores_faturamento)
maior_valor = max(valores_faturamento)

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")

print("fim do programa")