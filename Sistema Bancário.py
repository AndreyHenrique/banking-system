import os
import sys
from abc import ABC, abstractclassmethod, abstractproperty

class Cliente():
  def __init__(self, endereco):
    self.endereco = endereco
    self.contas = []

  def adicionar_conta(self, conta):
    self.contas.append(conta)

  def ver_contas_cliente(self):
    for i, conta in enumerate(self.contas, 1):
      print(f"\nConta: {i}")
      print(f"  Saldo: {conta.saldo}")
      print(f"  Número: {conta.numero}")
      print(f"  Agência: {conta.agencia}")
      print("-" * 30)

class PessoaFisica(Cliente):
  def __init__(self, cpf, nome, data_nascimento, endereco):
    super().__init__(endereco)
    self.cpf = cpf
    self.nome = nome
    self.data_nascimento = data_nascimento

class Conta():

  def __init__(self, numero, cliente, saldo):
    self._saldo = saldo
    self._numero = numero
    self._agencia = "0001"
    self._cliente = cliente
    self._historico = Historico()

  @property
  def saldo(self):
    return self._saldo

  @property
  def numero(self):
    return self._numero

  @property
  def agencia(self):
    return self._agencia

  @property
  def cliente(self):
    return self._cliente

  @property
  def historico(self):
    return self._historico

  def sacar(self, valor):
    valor = float(valor)
    if self._saldo >= valor and self._saldo > 0:
        self._saldo -= valor
        print("A operação foi um sucesso!")
        input("\nAperte enter para voltar ao menu.")
        return True

    print("A operação foi um fracasso!")
    input("\nAperte enter para voltar ao menu.")
    return False

  def depositar(self, valor):
    valor = float(valor)
    if valor > 0:
        self._saldo += valor
        print("A operação foi um sucesso!")
        input("\nAperte enter para voltar ao menu.")
        return True

    print("A operação foi um fracasso!")
    input("\nAperte enter para voltar ao menu.")
    return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, saldo, limite = 500, limite_saques = 3):
      super().__init__(numero, cliente, saldo)
      self.limite = limite
      self.limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero_da_conta, saldo):
      nova_conta = cls(numero_da_conta, cliente, saldo)
      cliente.adicionar_conta(nova_conta)
      return nova_conta
    
    def sacar(self, valor):
      valor = float(valor)
      numero_de_saques = sum(1 for transacao in self.historico.transacoes if transacao.tipo == "Saque")

      excedeu_limite = valor > self.limite

      excedeu_saque = numero_de_saques + 1 > self.limite_saques

      if not excedeu_limite:
        if not excedeu_saque:
          return super().sacar(valor=valor)
        else:
          print("Você excedeu o limite de saques.")
          input("Aperte enter para voltar ao menu.")
      else:
        print("Você excedeu o limite do saque.")
        input("Aperte enter para voltar ao menu.")
      return False

class Historico():
    def __init__(self):
      self._transacoes = []

    @property
    def transacoes(self):
      return self._transacoes

    def adicionar_transacao(self, operacao):  
      self._transacoes.append(operacao)

    def ver_extrato(self):
      apaga_terminal()
      for i, operacao in enumerate(self._transacoes, 1):
        print(f"Operação {i}:")
        print(f"  Tipo: {operacao.tipo}")
        print(f"  Valor: {operacao.valor}")
        print(f"  Numero da Conta: {operacao.numero_da_conta}")
        print(f"  Nome do Cliente: {operacao.nome_do_cliente}")
        print("-" * 30)

class Transacao(ABC):
  @property
  @abstractproperty
  def valor(self):
      pass

  @abstractclassmethod
  def registrar(self, conta):
      pass

class Depositar(Transacao):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor
  
  def registrar(self, conta):
    if conta.depositar(self._valor):
      historico = conta._historico
      operacao = Operacao(tipo="Depósito", valor=self._valor, numero_da_conta=conta.numero, nome_do_cliente=conta._cliente.nome)
      historico.adicionar_transacao(operacao)

class Sacar(Transacao):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor
  
  def registrar(self, conta):
    
    if conta.sacar(valor=self._valor):
      historico = conta._historico
      operacao = Operacao(tipo="Saque", valor=self._valor, numero_da_conta=conta.numero, nome_do_cliente=conta._cliente.nome)
      historico.adicionar_transacao(operacao)

class Operacao():
  def __init__(self, tipo, valor, numero_da_conta, nome_do_cliente):
    self.tipo = tipo
    self.valor = valor
    self.numero_da_conta = numero_da_conta
    self.nome_do_cliente = nome_do_cliente

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

def encontra_cpf(clientes, cpf):
  for cliente in clientes:
    if cliente.cpf == cpf:
      return cliente
  return None

def menu():
  apaga_terminal()
  print("="*15, "MENU", "="*15)
  print("""
      c - Contas
      o - Operações

      v - Sair
       """)
  print("="*18 + "="*18)

def menu_contas():
  apaga_terminal()
  print("="*15, "MENU", "="*15)
  print("""
      cl - Adicionar cliente
      vc - Ver Clientes
      cc - Criar Conta
      cv - Ver Contas

      v  - voltar
       """)
  print("="*18 + "="*18)

def menu_operacoes():
  apaga_terminal()
  print("="*15, "MENU", "="*15)
  print("""
      d  - Depositar
      s  - Sacar
      e  - Extrato
        
      v  - voltar
       """)
  print("="*18 + "="*18)

def cria_cliente(clientes):
    cpf = input("Digite seu CPF: ")
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereço: ")
    cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
    clientes.append(cliente)
    print("Cliente adicionado com sucesso!")
    input("\nAperte enter para voltar ao menu.")
    return clientes

def ver_clientes(clientes):
    if len(clientes) == 0:
        print("Não foram criadas contas.")
    else:
        for i, cliente in enumerate(clientes, 1):
            print(f"Cliente {i}:")
            print(f"  Nome: {cliente.nome}")
            print(f"  CPF: {cliente.cpf}")
            print(f"  Data de Nascimento: {cliente.data_nascimento}")
            print(f"  Endereço: {cliente.endereco}")
            print("-" * 30)

    input("\nAperte enter para voltar ao menu.")

def cria_conta(clientes):
  if len(clientes) == 0:
    print("Não existem clientes cadastrados.")
    input("\nAperte enter para voltar ao menu.")
  else:
    cpf = input("Digite o cpf do cliente que quer criar a conta: ")
    cliente = encontra_cpf(clientes, cpf)
    if cliente:
      numero_da_conta = len(cliente.contas) + 1
      ContaCorrente.nova_conta(cliente=cliente, numero_da_conta=numero_da_conta, saldo=0)
      print("\nConta Criada com Sucesso!")
      input("\nAperte enter para voltar ao menu.")
    else:
      print("O CPF digitado não está cadastrado no sistema.")
      input("\nAperte enter para voltar ao menu.")

def ver_contas(clientes):
  cpf = input("Digite o cpf do cliente que deseja ver as contas: ")
  cliente = encontra_cpf(clientes, cpf)
  if cliente:
    if len(cliente.contas) == 0:
      print("O cliente não tem contas.")
      input("\nAperte enter para voltar ao menu.")
    else:
      cliente.ver_contas_cliente()
      input("\nAperte enter para voltar ao menu.")
  else:
    print("O CPF digitado não está cadastrado no sistema.")
    input("\nAperte enter para voltar ao menu.")

def depositar(clientes):
  if len(clientes) == 0:
    print("Não existem clientes cadastrados.")
    input("\nAperte enter para voltar ao menu.")
  else:
    cpf = input("Digite o cpf do cliente que deseja fazer a transação: ")
    cliente = encontra_cpf(clientes, cpf)
    if cliente:
      if len(cliente.contas) == 0:
        print("Não existem contas cadastradas.")
        input("\nAperte enter para voltar ao menu.")
      else:
        conta = cliente.contas[0]
        valor = input("\nDigite o valor que deseja depositar: ")
        deposito = Depositar(valor)
        deposito.registrar(conta=conta)
    else:
      print("O CPF digitado não está cadastrado no sistema.")
      input("\nAperte enter para voltar ao menu.")

def sacar(clientes):
  if len(clientes) == 0:
    print("Não existem clientes cadastrados.")
    input("\nAperte enter para voltar ao menu.")
  else:
    cpf = input("Digite o cpf do cliente que deseja fazer a transação: ")
    cliente = encontra_cpf(clientes, cpf)
    if cliente:
      if len(cliente.contas) == 0:
        print("Não existem contas cadastradas.")
        input("\nAperte enter para voltar ao menu.")
      else:
        conta = cliente.contas[0]
        valor = input("\nDigite o valor que deseja sacar: ")
        saque = Sacar(valor)
        saque.registrar(conta=conta)
    else:
      print("O CPF digitado não está cadastrado no sistema.")
      input("\nAperte enter para voltar ao menu.")

def extrato(clientes):
  if len(clientes) == 0:
    print("Não existem clientes cadastrados.")
    input("\nAperte enter para voltar ao menu.")
  else:
    cpf = input("Digite o cpf do cliente que deseja fazer a transação: ")
    cliente = encontra_cpf(clientes, cpf)
    if cliente:
      if len(cliente.contas) == 0:
        print("Não existem contas cadastradas.")
        input("\nAperte enter para voltar ao menu.")
      else:
        conta = cliente.contas[0]
        historico = conta._historico
        historico.ver_extrato()
        input("\nAperte enter para voltar ao menu.")
    else:
      print("O CPF digitado não está cadastrado no sistema.")
      input("\nAperte enter para voltar ao menu.")

def main():
  andrey = PessoaFisica("0", "Andrey Henrique de Abreu Carneiro", "14/01/2005", "Rua perdigão de Oliveira, 832")
  clientes = [andrey]
  conta_do_andrey = ContaCorrente(numero=0, saldo=1000, cliente=andrey)
  andrey.adicionar_conta(conta_do_andrey)

  while True:
    menu()
    caminho = input("=> ")

    if caminho.lower() == "c":

      while True:
        menu_contas()
        caminho = input("=> ")

        if caminho.lower() == "cl":
          cria_cliente(clientes)
          break
        elif caminho.lower() == "vc":
          ver_clientes(clientes)
          break
        elif caminho.lower() == "cc":
          cria_conta(clientes)
          break
        elif caminho.lower() == "cv":
          ver_contas(clientes)
          break
        elif caminho.lower() == "v":
            break
        else:
            print("\nA entrada de dados é irreconhecida. Por favor, tente novamente.")
            input("\n Aperte enter para voltar ao menu.")

    elif caminho.lower() == "o":
      while True:
        menu_operacoes()
        caminho = input("=> ")

        if caminho.lower() == "d":
          depositar(clientes)
          break
        elif caminho.lower() == "s":
          sacar(clientes)
          break
        elif caminho.lower() == "e":
          extrato(clientes)
          break
        elif caminho.lower() == "v":
            break
        else:
            print("\nA entrada de dados é irreconhecida. Por favor, tente novamente.")
            input("\n Aperte enter para voltar ao menu.")

    elif caminho.lower() == "v":
      print("\nObrigado por utilizar nossos sistemas, volte sempre!")
      break

    else:
      print("A entrada de dados é irreconhecida. Por favor, tente novamente.")

main()
