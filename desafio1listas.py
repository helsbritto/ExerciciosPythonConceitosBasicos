# 1 #
respostas = []

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

for pergunta in perguntas:
    resposta = input(f"{pergunta} (S para sim, N para não): ")
    respostas.append(resposta.upper())

positivas = respostas.count("S")

if positivas == 2:
    print("Suspeita")
elif 3 <= positivas <= 4:
    print("Cúmplice")
elif positivas == 5:
    print("Assassino")
else:
    print("Inocente")

# 2 #
medias_alunos = []
for i in range(5):
    notas = [float(input(f"Digite a nota {j + 1} do aluno {i + 1}: ")) for j in range(4)]
    media = sum(notas) / len(notas)
    medias_alunos.append(media)

alunos_aprovados = sum(1 for media in medias_alunos if media >= 7.0)
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")

# 3 #
carrinho_compras = {}
def adicionar_produto(carrinho, produto, quantidade, preco_unitario):
    if produto in carrinho:
        carrinho[produto]['quantidade'] += quantidade
    else:
        carrinho[produto] = {'quantidade': quantidade, 'preco_unitario': preco_unitario}

adicionar_produto(carrinho_compras, 'Sal', 3, 2.5)
adicionar_produto(carrinho_compras, 'Mel', 2, 1.0)
adicionar_produto(carrinho_compras, 'Leite', 1, 3.0)

def calcular_total(carrinho):
    total = sum(item['quantidade'] * item['preco_unitario'] for item in carrinho.values())
    return total

total_carrinho = calcular_total(carrinho_compras)
print(f"Total do carrinho de compras: R${total_carrinho:.2f}")

# 4 #
contatos = {
    'Heloísa': '7777777',
    'Angelina': '7654321',
    'Filipe': '1234567'
}

def procurar_contato(nome, lista_contatos):
    return lista_contatos.get(nome, "Contato não encontrado")
nome_procurado = input("Digite o nome do contato que deseja procurar: ")

resultado_procura = procurar_contato(nome_procurado, contatos)
print(resultado_procura)


# 5 #
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
nova_tupla = tupla1 + tupla2
print("Nova Tupla:", nova_tupla)

# 6 #
nome_usuario = input("Digite seu nome: ")
nome_invertido = nome_usuario[::-1].upper()
print("Nome invertido em maiúsculas:", nome_invertido)

