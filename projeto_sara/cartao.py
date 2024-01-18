class Cartao:
    def __init__(self, numero_cartao_1,numero_cartao_2,numero_cartao_3,numero_cartao_4, titular, codigo_verificador):
            self.numero_cartao_1 = numero_cartao_1
            self.numero_cartao_2 = numero_cartao_2
            self.numero_cartao_3 = numero_cartao_3
            self.numero_cartao_4 = numero_cartao_4
            self.titular = titular
            self.codigo_verificador = codigo_verificador

    # Getters and Setters
    def get_numero_cartao_1(self):
        return self.numero_cartao_1
    def set_numero_cartao_1(self, value):
        self.numero_cartao_1 = value
    def get_numero_cartao_2(self):
        return self.numero_cartao_2
    def set_numero_cartao_2(self, value):
        self.numero_cartao_2 = value
    def get_numero_cartao_3(self):
        return self.numero_cartao_3
    def set_numero_cartao_3(self, value):
        self.numero_cartao_3 = value
    def get_numero_cartao_4(self):
        return self.numero_cartao_4
    def set_numero_cartao_4(self, value):
        self.numero_cartao_4 = value
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
