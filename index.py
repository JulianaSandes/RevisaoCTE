"""
Exercício 1
"""

numero = int(input("Digite um número inteiro:"))

print("O número inteiro é", numero)

"""
Exercício 2
"""

numero = float (input("Digita o número real:"))

print("O número é %.2f." %numero)

"""
Exercício 3
"""

numero1 = int(input("Digite o primeiro número inteiro")) 
numero2 = int(input("Digite o segundo número inteiro")) 
numero3 = int(input("Digite o terceiro número inteiro"))

resultado = numero1 + numero2 + numero3

print("O resultado é", resultado)

"""
Exercício 4
"""

numero1 = float(input("Digite o número para colocar ao quadrado:"))

resultado = numero1 **2

print("O resultado é igual á: %.2f.", numero1)

"""
Exercício 5
"""

numero1 = float(input("Digite o número para colocar ao quadrado:"))

resultado = numero1 /5

print("O resultado é igual á: %.5f.", numero1)

"""
Exercício 6
"""

C = int(input("Digite o valor da temperatura em Celsius:"))

resultado = F = C * (9.0/5.0) + 32

print("C = ", C, "F = ", F)

"""
Exercício 7
"""

F = int(input("Digite o valor da temperatura em  Fahrenheit:"))

resultado = C = 5.0 * (F - 32.0)/9.0

print("C = ", C, "F = ", F)

"""
Exercício 8
"""

C = int(input("Digite o valor da temperatura em Celsius:"))

resultado = K = C + 273.15

print("C = ", C, "K = ", K)

"""
Exercício 9
"""

K = int(input("Digite o valor da temperatura em Kevin:"))

resultado = C = K - 273.15

print("C = ", C, "K = ", K)

"""
Exercício 10
"""

K = int(input("Digite a velocidade em km/h:"))

resultado = M = K/3.6

print("m/s = ", M)

"""
Exercício 11
"""

M = int(input("Digite a velocidade em m/s:"))

resultado = K = M * 3.6

print("km/h = ", K)

"""
Exercício 28
"""

n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))

resultado = (n1 ** 2) + (n2 ** 2) + (n3 ** 2)

print("A soma é igual á", resultado)

"""
Exercício 29
"""

nota1 = int(input("Digite o primeiro nota:"))
nota2 = int(input("Digite o segundo nota:"))
nota3 = int(input("Digite o terceira nota:"))

resultado = (nota1 + nota2 + nota3)/3

print("A média aritmética é igual á", resultado)

"""
Exercício 30
"""

real = float(input("Digite o valor em real:"))

resultado = real * 5.04

print("O valor da cotação é de:", resultado)

"""
Exercício 31
"""

n = int(input("Digite o número inteiro"))

resultado1 = n - 1
resultado2 = n + 1

print("Número inteiro = ", n, "Antecessor = ", resultado1, "Sucessor", resultado2)

"""
Exercício 49
"""

total = 780.000

pg = total * 0.46
sg = total * 0.32
tg = total - pg - sg

print("O primeiro vai receber R$", pg)
print("O segundo vai receber R$", sg)
print("O terceiro vai receber R$", tg)