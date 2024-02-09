# 1 #
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: ")
maior_numero = max(numero1, numero2)
print(f"O maior número é: {maior_numero}")

# 2 #
turno = input("Em qual turno você estuda? (M-matutino, V-vespertino, N-noturno): ")
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")

# 3 #
while True:
    nota = float(input("Digite a nota entre 0 a 10: "))
    if 0 <= nota <= 10:
        break
    else:
        print("Nota inválida. Digite novamente.")

print(f"Nota: {nota}")

# 4 #
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")

# 5 #
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 == lado2 == lado3:
    print("Triângulo Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")

# 6 #
login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == "admin" and senha == "admin123":
    print("Acesso permitido!")
else:
    print("Erro.")

# 7 #
idade = int(input("Digite a idade: "))
if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 50:
    print("Adulto")
else:
    print("Idoso")

# 8 #
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    maior_numero = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior_numero = numero2
else:
    maior_numero = numero3
print(f"O maior número é: {maior_numero}")

# 9 #
pares = 0
impares = 0

while True:
    try:
        numero = int(input("Digite um número (ou 0 para encerrar): "))
        if numero < 0:
            print("Por favor, digite apenas números positivos.")
            continue
        if numero == 0:
            break
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")

# 10 #
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))
    
numeros_ordenados = sorted([numero1, numero2, numero3])

print(f"Números em ordem crescente: {numeros_ordenados}")

