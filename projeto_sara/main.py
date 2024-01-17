class Main:
    @staticmethod
    def pedir_opcao():
        try:
            return int(input("============================\n"
                         "             MENU            \n"
                         "=============================\n"
                         "1 - Pedir cartão de débito\n"
                         "2 - Pedir cartão de crédito\n"
                         "3 - Mostrar dados cartão\n"
                         "4 - Realizar compra \n"
                         "5 - Realizar saque\n"
                         "6 - Realizar depósito\n"
                         "7 - Pagar fatura\n"
                         "0 - Sair\n"
                         "Selecione uma opção: "))
        except ValueError:
            print("Opção inválida. Por favor, insira um número inteiro.")
            return -1  # ou outra indicação de valor inválido
 
    @staticmethod
    def pedir_dados(mensagem):
        return input(mensagem)
 
    @staticmethod
    def mostrar_dados_debito(cartao):
        return "=============================\n" \
               "            DADOS            \n" \
               "=============================\n" \
               f"Titular: {cartao.get_titular()} \n" \
               f"Número do cartão: {cartao.get_numero_cartao()} \n" \
               f"Código verificador: {cartao.get_codigo_verificador()} \n" \
               f"Saldo: R${cartao.get_saldo()}\n"
 
    @staticmethod
    def mostrar_dados_credito(cartao):
        from cartao_credito import CartaoCredito
        return "=============================\n" \
               "            DADOS            \n" \
               "=============================\n" \
               f"Titular: {cartao.get_titular()} \n" \
               f"Número do cartão: {cartao.get_numero_cartao()} \n" \
               f"Código verificador: {cartao.get_codigo_verificador()} \n" \
               f"Limite disponível: R${cartao.get_limite()} \n" \
               f"Fatura atual: R${cartao.get_valor_fatura()} \n"
 
    @staticmethod
    def main():
        from cartao_debito import CartaoDebito
        from cartao_credito import CartaoCredito
        credito_existe = False
        debito_existe = False

        opcao = 1
        while opcao != 0:
            opcao = Main.pedir_opcao()
            match opcao:
                case 1:
                    debito_existe = True
                    cartao_debito = CartaoDebito.criar_cartao_debito()
                case 2:
                    credito_existe = True
                    cartao_credito = CartaoCredito.criar_cartao_credito()
                case 3:
                    opcao_dados = Main.pedir_dados("1 - Mostrar dados cartão de débito \n"
                                                "2 - Mostrar dados cartão de crédito\n"
                                                "Selecione a opção desejada: ")
                    match opcao_dados:
                        case "1":
                            if (debito_existe==False):
                                print("Você não possui um cartão de débito!")
                            else:
                                dados_debito = Main.mostrar_dados_debito(cartao_debito)
                                print(dados_debito)
                        case "2":
                            if (credito_existe==False):
                                print("Você não possui um cartão de crédito!")
                            else:
                                dados_credito = Main.mostrar_dados_credito(cartao_credito)
                                print(dados_credito)
                        case __:
                            print("Opção Inválida!")
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 0:
                    print("Obrigada por utilizar o programa!")
                case __:
                    print("Opção Inválida!")

if __name__ == "__main__":
    Main.main()
