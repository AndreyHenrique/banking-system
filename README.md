# Sistema Bancário

Este projeto é um sistema bancário desenvolvido em Python, utilizando conceitos de Programação Orientada a Objetos (POO). Ele permite o gerenciamento de clientes e contas bancárias, além de realizar operações de depósito e saque, mantendo um histórico detalhado de transações.

## Funcionalidades

- **Gerenciamento de Clientes**: Adição e visualização de clientes.
- **Gerenciamento de Contas**: Criação de contas para clientes e visualização das contas associadas a cada cliente.
- **Operações Bancárias**: Realização de depósitos e saques, com registro detalhado das transações.
- **Histórico de Transações**: Cada conta mantém um histórico de todas as transações realizadas.

## Estrutura do Projeto

O projeto está organizado em várias classes, cada uma responsável por uma parte específica do sistema:

- **Cliente**: Classe base para clientes. Possui métodos para realizar transações e adicionar contas.
- **PessoaFisica**: Subclasse de Cliente, específica para clientes pessoas físicas.
- **Conta**: Classe base para contas bancárias. Possui métodos para depósito e saque.
- **ContaCorrente**: Subclasse de Conta, específica para contas correntes. Implementa limites de saque.
- **Historico**: Classe para manter o histórico de transações de uma conta.
- **Operacao**: Classe que representa uma operação (transação) no sistema.
- **Transacao**: Classe abstrata para operações de depósito e saque.
- **Depositar**: Subclasse de Transacao para depósitos.
- **Saque**: Subclasse de Transacao para saques.
