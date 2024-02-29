import json

# Transformando os dados faturamento mensal em formato de JSON
dist_state = '''[
  {
    "Estado": "SP",
    "Valor": 67836.43
  },
  {
    "Estado": "RJ",
    "Valor": 36678.66
  },
  {
    "Estado": "MG",
    "Valor": 29229.88
  },
  {
    "Estado": "ES",
    "Valor": 27165.48
  },
  {
    "Estado": "Outros",
    "Valor": 19849.53
  }
] '''

# Transformando string em um dicionário meio da variável 'infos'
infos = json.loads(dist_state)

# Calcula o faturamento total
faturamento_total = sum(item["Valor"] for item in infos)

# Calcula o percentual de representação de cada estado
for item in infos:
    percentual = (item["Valor"] / faturamento_total) * 100
    print(f"Porcentagem de {item['Estado']}: {percentual:.2f}%")

print("fim do programa")