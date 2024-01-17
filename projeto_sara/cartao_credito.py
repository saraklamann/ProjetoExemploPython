from cartao import Cartao
from main import Main
import random


class CartaoCredito(Cartao):
    def __init__(
        self, numero_cartao, titular, codigo_verificador, limite=1000, valor_fatura=0
    ):
        super().__init__(numero_cartao, titular, codigo_verificador)
        self.__limite = limite
        self.__valor_fatura = valor_fatura

    # Getters and Setters
    def get_limite(self):
        return self.__limite

    def set_limite(self, value):
        self.__limite = value

    def get_valor_fatura(self):
        return self.__valor_fatura

    def set_valor_fatura(self, value):
        self.__valor_fatura = value

    # Métodos especificos para cartão de crédito
    def realizar_compra(self):
        valor = float(input("Digite o valor da compra: "))
        if valor <= self.get_limite():
            self.set_limite(self.get_limite() - valor)
            self.set_valor_fatura(self.get_valor_fatura() + valor)
            print(
                f"Compra realizada com sucesso! Limite atual: R${self.get_limite()}. Sua fatura está em: R${self.get_valor_fatura()}"
            )
        else:
            print("Saldo insuficiente! Operação não realizada.")

    def pagar_fatura(self):
        print(f"Sua fatura está em R${self.get_valor_fatura()}.")
        valor = float(input("Digite o valor que deseja pagar: "))
        if valor > self.get_valor_fatura() or valor <= 0:
            print("Valor Inválido!")
        elif valor < self.get_valor_fatura():
            self.set_valor_fatura(self.get_valor_fatura - valor)
            self.set_limite(self.get_limite() + valor)
            print(
                f"Pagamento parcial realizado! Seu limite disponivel é: R${self.get_limite()}. Sua fatura está em: R${self.get_valor_fatura}"
            )

    # INCLUIDO DA CLASSE BANCO(ELIMINADA)
    def criar_cartao_credito():
        cc = CartaoCredito(
            numero_cartao=random.randint(1000000000000000, 9999999999999999),
            titular=Main.pedir_dados("Insira o nome do titular: "),
            codigo_verificador=random.randint(100, 999),
            limite=1000,
            valor_fatura=0,
        )
        return cc
