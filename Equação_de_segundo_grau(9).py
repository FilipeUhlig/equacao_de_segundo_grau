"""
Programa: Equação de segundo grau
Descrição: Este programa resolve uma equação de segundo grau do tipo ax² = b
Autor: Filipe
Data: 04/06/2023
Versão: 0.0.1
"""
#Atribuição de variáveis

#Entrada de dados
a = int(input("Qual é o valor de a, dado ax² = b? "))
b = int(input("Qual é o valor de b, dado ax² = b? "))


#Processamento de dados
x = ((b/a)**(1/2))

#Saida de dados
print(f"O valor de x é {x}.")