import os
import sys
saldo = float(0)
contagem_de_saques = 0
extrato_lista = []

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

def deposito(saldo, contagem_de_saques, extrato_lista):
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

def saque(saldo, contagem_de_saques, extrato_lista):
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

def extrato(saldo, contagem_de_saques, extrato_lista):
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

def menu(saldo, contagem_de_saques, extrato_lista):
  apaga_terminal()
  print("="*15, "MENU", "="*15)
  print("""
      d - Depositar
      s - Sacar
      e - Extrato
      v - Sair
       """)
  print("="*18 + "="*18)

  while True:
    caminho = input()
    if caminho == "d":
      deposito(saldo, contagem_de_saques, extrato_lista)
    elif caminho == "s":
      saque(saldo, contagem_de_saques, extrato_lista)
    elif caminho == "e":
      extrato(saldo, contagem_de_saques, extrato_lista)
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