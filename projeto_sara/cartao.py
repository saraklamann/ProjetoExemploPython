class Cartao:
    def __init__(self, numero_cartao, titular, codigo_verificador):
        self.numero_cartao = numero_cartao
        self.titular = titular
        self.codigo_verificador = codigo_verificador

    # Getters and Setters
    def get_numero_cartao(self):
        return self.numero_cartao

    def set_numero_cartao(self, value):
        self.numero_cartao = value

    def get_titular(self):
        return self.titular

    def set_titular(self, value):
        self.titular = value

    def get_codigo_verificador(self):
        return self.codigo_verificador

    def set_codigo_verificador(self, value):
        self.codigo_verificador = value

    # Métodos da classe
    def realizar_compra(self):
        pass
