# 1 #
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

# 2 #

AnoNascimento = float(input("Ano de nascimento: "))
AnoAtual = float(input("Ano atual: "))

idade = AnoAtual - AnoNascimento

print("{idade}")

# 3 #

quilometros = float(input("Digite em quilômetros: "))
metros = quilometros * 1000
centimetros = quilometros * 100000
milimetros = quilometros * 1000000

print(f"{quilometros} quilômetros é igual a:")
print(f"{metros} metros")
print(f"{centimetros} centímetros")
print(f"{milimetros} milímetros")

# 4 #
litros_consumidos = float(input("Digite a quantidade de litros de combustível consumidos: "))

distancia_percorrida = float(input("Digite a distância percorrida em quilômetros: "))

consumo = distancia_percorrida / litros_consumidos

print(f"O consumo é de {consumo:.2f} km/l.")

# 5 #
salario_bruto = float(input("Digite salário bruto: "))
percentual_desconto_ir = float(input("Digite percentual de desconto do Imposto de Renda: "))

if salario_bruto <= 1903.98:
    desconto_ir = 0
elif 1903.99 <= salario_bruto <= 2826.65:
    desconto_ir = salario_bruto * 0.075
elif 2826.66 <= salario_bruto <= 3751.05:
    desconto_ir = salario_bruto * 0.15
elif 3751.06 <= salario_bruto <= 4664.68:
    desconto_ir = salario_bruto * 0.225
else:
    desconto_ir = salario_bruto * 0.275

salario_liquido = salario_bruto - desconto_ir

print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Desconto do Imposto de Renda: R${desconto_ir:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")

# 6 #

distancia_viagem = float(input("Digite a distância da viagem em km: "))

velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

tempo_aviao = distancia_viagem / velocidade_aviao
tempo_carro = distancia_viagem / velocidade_carro
tempo_onibus = distancia_viagem / velocidade_onibus

print(f"Tempo de viagem de avião: {tempo_aviao:.2f} horas")
print(f"Tempo de viagem de carro: {tempo_carro:.2f} horas")
print(f"Tempo de viagem de ônibus: {tempo_onibus:.2f} horas")

# 7 #
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

# 8 #

valor_por_hora = float(input("Digite o valor ganho por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))

salario_total = valor_por_hora * horas_trabalhadas

print(f"O salário total no mês é: R${salario_total:.2f}")

# 9 #

horas_por_semana = float(input("Digite o número de horas de exercício físico por semana: "))

minutos_por_semana = horas_por_semana * 60

calorias_por_minuto = 5
calorias_totais = minutos_por_semana * 4 * calorias_por_minuto  # 4 semanas em um mês
print(f"Total de calorias queimadas em um mês: {calorias_totais} calorias")

# 10 #
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
lugar = input("Digite o lugar onde você mora: ")
profissao = input("Digite sua profissão: ")

mensagem = f"Olá {nome}, que legal te conhecer. Eu também tenho {idade} anos, mas moro em Campo Grande e não trabalho como {profissao}."
print(mensagem)

