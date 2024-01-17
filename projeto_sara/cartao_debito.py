from cartao import Cartao
from main import Main
import random


class CartaoDebito(Cartao):
    def __init__(self, numero_cartao, titular, codigo_verificador, saldo=0):
        super().__init__(numero_cartao, titular, codigo_verificador)
        self.__saldo = saldo

    # Getters and Setters

    def set_saldo(self, value):
        self.__saldo = value

    """ def set_saldo(self):    # não deve retornar o saldo e sim um atribuição
        return self.__saldo """

    def get_saldo(self):
        return self.__saldo

    # Métodos especificos para cartão de débito
    def realizar_compra(self):
        valor = float(input("Digite o valor da compra: "))
        if valor <= self.__saldo():
            self.set_saldo(self.get_saldo() - valor)
            print(f"Compra realizada com sucesso! Saldo atual: R${self.get_saldo()}.")
        else:
            print("Saldo insuficiente! Operação não realizada.")

    def sacar(self):
        valor = float(input("Digite o valor do saque: "))
        if valor <= self.__saldo():
            self.set_saldo(self.get_saldo() - valor)
            print(f"Saque realizado com sucesso! Saldo atual: R${self.get_saldo()}.")
        else:
            print("Saldo insuficiente! Operação não realizada.")

    def depositar(self):
        valor = float(input("Digite o valor do depósito: "))
        self.set_saldo(self.get_saldo() + valor)
        print(f"Depósito realizado com sucesso! Saldo atual: R${self.get_saldo()}.")

    # INCLUIDO DA CLASSE BANCO(ELIMINADA)
    def criar_cartao_debito():
        cd = CartaoDebito(
            numero_cartao=random.randint(1000000000000000, 9999999999999999),
            titular=Main.pedir_dados("Insira o nome do titular: "),
            codigo_verificador=random.randint(100, 999),
            saldo=0,
        )
        return cd
