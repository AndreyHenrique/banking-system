import os
import sys
saldo = float(0)
contagem_de_saques = 0
extrato_lista = []
global usuarios, contas
usuarios = [{"nome": "Andrey Henrique", "data de nascimento": "14/01/2005", "cpf": "00000000001", "endereço":"Fortaleza"}]
contas = []


def apaga_terminal():
  if sys.platform.startswith("win"):
    os.system("cls")
  else: 
    os.system("clear")

def is_simple_number(value):
    if not value.strip().replace('-', '').replace('+', '').replace('.', '').isdigit():
        return False
    try:
         float(value)
    except ValueError:
         return False
    return True

def verifica_cpf(cpf_formatado, lista):
  for usuario in lista:
    if usuario["cpf"] == cpf_formatado:
      return True 
  return False

def deposito(saldo, contagem_de_saques, extrato_lista, /):
  apaga_terminal()
  while True:
    valor = ( input("digite o valor que você deseja depositar, ou digite (v) para voltar ao menu: "))
    if valor =="v":
      print()
      break
    else:
      if is_simple_number(valor):
        valor = float(valor)
        if valor <= 0:
          print()
          print("A entrada de dados é irreconhecida. Por favor, tente novamente ou digite (v) para voltar ao menu.")
          print()
        elif valor > 0:
          extrato_lista.append(f"Depósito: R${valor}")
          saldo = saldo + valor
          print(f"Seu saldo agora é de R${saldo}.")
          print()
          print("Pressione enter para voltar ao menu.")
          input()
          break
      else:
        print("A entrada de dados é irreconhecida. Por favor, tente novamente.")
  menu(saldo, contagem_de_saques, extrato_lista)

def saque(*, saldo, contagem_de_saques, extrato_lista):
  apaga_terminal()
  if contagem_de_saques >= 3:
    print("Você atingiu o limite de saques diário, tente novamente mais tarde.")
  else:
    print(f"Seu saldo é de: R${saldo}.")
    while True:
      print()
      valor = input("Digite o valor que deseja sacar, ou digite (v) para voltar ao menu: ")
      if valor == "v":
        print()
        break
      else:
        valor = float(valor)
        if valor <= 0:
          print("O valor é invalído.")
        elif valor > saldo:
          print("O valor que você deseja sacar é maior que o saldo que você tem em conta. Por favor tente novamente.")
        elif valor > 500:
          print("O valor que você deseja sacar é maior que o limite por saque. por favor tente novamente.")
        else:
          extrato_lista.append(f"Saque: R${valor}")
          saldo = saldo - valor
          print()
          print(f"Seu saque foi realizado com sucesso, seu saldo agora é de: R${saldo}.")
          contagem_de_saques += 1
          print()
          print("presione enter  para voltar ao menu.")
          input()
          break
  menu(saldo, contagem_de_saques, extrato_lista)

def extrato(saldo, /, *, extrato_lista, contagem_de_saques):
  apaga_terminal()
  print("="*14, "EXTRATO", "="*13)
  print()
  if not extrato_lista:
    print("Não houveram movimentações financeiras na sua conta.")
  else:
    for elemento in extrato_lista:
      print(f"{elemento}")
  print()
  print(f"Seu saldo é de R$: {saldo}.")
  print()
  print("="*18 + "="*18)
  print("\n Pressione enter para voltar ao menu.\n")
  input()
  menu(saldo, contagem_de_saques, extrato_lista)

# Cliente do Banco
def criar_usuario(saldo, contagem_de_saques, extrato_lista):
  apaga_terminal()
  while True:
    cpf = input("Digite seu CPF, ou aperte (v) para retornar: ")
    if cpf == "v":
      menu(saldo, contagem_de_saques, extrato_lista)
    else:
      cpf_formatado = ""
      for char in cpf:
        if char.isdigit():
          cpf_formatado += char

      if verifica_cpf(cpf_formatado, usuarios):
        print("Esse CPF já está cadastrado no sistema.")
        input("\nAperte enter para voltar ao menu.")
        menu(saldo, contagem_de_saques, extrato_lista) 
      elif len(cpf_formatado) < 11 or len(cpf_formatado) > 11:
          print("\nO CPF que você digitou é invalído.")
          print()
      else:
        nome = input("Digite seu nome completo: ")
        data_nascimento = input("Digite sua data de nascimento (dd/mm/yyyy): ")
        endereço = input("Digite seu endereço (logradouro - n - bairro - cidade/Sigla estado): ")
        usuarios.append({"nome": nome, "data de nascimento": data_nascimento,"cpf": cpf_formatado, "endereço": endereço})
        print("\nUsuário cadastrado com sucesso.")
        input("\nAperte enter para voltar ao menu.")
        menu(saldo, contagem_de_saques, extrato_lista) 

# Vincular com o Usuario
def criar_conta_corrente(saldo, contagem_de_saques, extrato_lista):
  apaga_terminal()

  if len(usuarios) == 0:
    print("Não existem usuários cadastrados no sistema.")
    input("\nAperte enter para voltar ao menu.")
    menu(saldo, contagem_de_saques, extrato_lista)

  else:
    while True:
      usuario_cpf = input("Digite o CPF do usuário que deseja conectar a esta conta corrente ou aperte (v) para voltar ao menu: ")
      if usuario_cpf == "v":
        menu(saldo, contagem_de_saques, extrato_lista)
      else:
        usuario_cpf_formatado = ""
        for char in usuario_cpf:
          if char.isdigit():
            usuario_cpf_formatado += char

        if not verifica_cpf(usuario_cpf_formatado, usuarios):
          print("Não foi encontrado nenhum CPF correspondente, por favor tente novamente.")
        else:
          agencia = "0001"
          n_conta = (len(contas) + 1)
          contas.append({"Agência": agencia, "Número da conta": n_conta, "Usuário": usuario_cpf_formatado})
          print("\nSua conta foi criada com sucesso.")
          input("\nAperte enter para voltar ao menu.")
          menu(saldo, contagem_de_saques, extrato_lista)

def listar_contas():  
  print()

def menu(saldo, contagem_de_saques, extrato_lista):
  apaga_terminal()
  print("="*15, "MENU", "="*15)
  print("""
      d - Depositar
      s - Sacar
      e - Extrato
      u - Criar novo usuário
      c - Criar nova conta corrente
      v - Sair
       """)
  print("="*18 + "="*18)

  while True:
    caminho = input("=> ")
    if caminho == "d":
      deposito(saldo, contagem_de_saques, extrato_lista)
    elif caminho == "s":
      saque(saldo=saldo, contagem_de_saques=contagem_de_saques, extrato_lista=extrato_lista)
    elif caminho == "e":
      extrato(saldo, contagem_de_saques=contagem_de_saques, extrato_lista=extrato_lista)
    elif caminho == "u":
      criar_usuario(saldo, contagem_de_saques, extrato_lista)
    elif caminho == "c":
      criar_conta_corrente(saldo, contagem_de_saques, extrato_lista)
    elif caminho == "v":
      apaga_terminal()
      print()
      print("Obrigado por utilizar nossos sistemas, volte sempre!")
      print()
      sys.exit()
      break
    else:
      print()
      print("A entrada de dados é irreconhecida. Por favor, tente novamente.")
      print()



menu(saldo, contagem_de_saques, extrato_lista)
