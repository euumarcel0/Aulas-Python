# Definição da função para calcular operações matemáticas
def calcular_operacao(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        return num1 / num2
    else:
        return "Operador inválido"

# Entrada dos números e operador da operação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

# Cálculo da operação e exibição do resultado
resultado = calcular_operacao(num1, num2, operador)
print(f"O resultado da operação é: {resultado}")