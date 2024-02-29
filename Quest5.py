def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    resultado = ""

    # Percorre a string de trás para frente e adiciona cada caractere ao resultado
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]

    return resultado

# Exemplo
minha_string = "Papiro"
string_invertida = inverter_string(minha_string)
print(f"String original: {minha_string}")
print(f"String invertida: {string_invertida}")

print("fim do programa")