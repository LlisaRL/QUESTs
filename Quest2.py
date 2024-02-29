# Função que faz a vereificação em si se o número escrito pelo user fas parte da seuquência Fibonacci

def Fibs(A):
    Term1 = 0
    Term2 = 1
    while Term2 < A:
        Term1, Term2 = Term2, Term1 + Term2
    return Term2 == A

#Verifica se o número inserido é parte da sequência Fibonacci

TermN = int(input("Insira um valor a ser verificado:"))
if Fibs(TermN):
    print("Pertence à sequência Fibonacci.")
else:
    print("Não pertence à sequência Fibonacci.")