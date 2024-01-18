from cartao import Cartao
from main import Main
import random
import string


class CartaoDebito(Cartao):
    def __init__(self, numero_cartao_1,numero_cartao_2,numero_cartao_3,numero_cartao_4, titular, codigo_verificador, saldo=0):
        super().__init__(numero_cartao_1,numero_cartao_2,numero_cartao_3,numero_cartao_4, titular, codigo_verificador)
        self.__saldo = saldo

    # Getters and Setters
    def set_saldo(self, value):
        self.__saldo = value
    def get_saldo(self):
        return self.__saldo

    # Métodos especificos para cartão de débito
    def realizar_compra(self):
        valor = float(input("Digite o valor da compra: "))
        if valor <= self.get_saldo():
            self.set_saldo(self.get_saldo() - valor)
            print(f"Compra realizada com sucesso! Saldo atual: R${self.get_saldo():.2f}.")
        else:
            print("Saldo insuficiente! Operação não realizada.")

    def sacar(self):
        valor = float(input("Digite o valor do saque: "))
        if valor <= self.get_saldo():
            self.set_saldo(self.get_saldo() - valor)
            print(f"Saque realizado com sucesso! Saldo atual: R${self.get_saldo():.2f}.")
        else:
            print("Saldo insuficiente! Operação não realizada.")

    def depositar(self):
        valor = float(input("Digite o valor do depósito: "))
        self.set_saldo(self.get_saldo() + valor)
        print(f"Depósito realizado com sucesso! Saldo atual: R${self.get_saldo():.2f}.")

    def criar_cartao_debito():
        cd = CartaoDebito(
            numero_cartao_1=random.randint(1000,9999),
            numero_cartao_2=random.randint(1000,9999),
            numero_cartao_3=random.randint(1000,9999),
            numero_cartao_4=random.randint(1000,9999),
            titular=Main.pedir_dados("Insira o nome do titular: "),
            codigo_verificador=random.randint(100, 999),
            saldo=0,
        )
        return cd
