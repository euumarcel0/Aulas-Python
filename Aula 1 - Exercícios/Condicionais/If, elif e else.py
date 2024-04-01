# Operadores Condicionais

# Exemplo 1 - Condicional if, elif, else
numero = 100
#Se o numero foi maior que 10
if numero > 10:
    print("O número é maior que 10")
#e se o numero foi maenorque 10
elif numero < 10:
    print("O número é menor que 10")
#Como não encontrou nenhuma condição anterior o numero é 10
else:
    print("O número é igual a 10")


# Exemplo 2 - Condicional if, else
idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")
