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
            return -1  
 
    @staticmethod
    def pedir_dados(mensagem):
        return input(mensagem)
 
    @staticmethod
    def mostrar_dados_debito(cartao):
        return "=============================\n" \
               "            DADOS            \n" \
               "=============================\n" \
               f"Titular: {cartao.get_titular()} \n" \
               f"Número do cartão: {cartao.get_numero_cartao_1()}.{cartao.get_numero_cartao_2()}.{cartao.get_numero_cartao_3()}.{cartao.get_numero_cartao_4()} \n" \
               f"Código verificador: {cartao.get_codigo_verificador()} \n" \
               f"Saldo: R${cartao.get_saldo():.2f}\n"
 
    @staticmethod
    def mostrar_dados_credito(cartao):
        from cartao_credito import CartaoCredito
        return "=============================\n" \
               "            DADOS            \n" \
               "=============================\n" \
               f"Titular: {cartao.get_titular()} \n" \
               f"Número do cartão: {cartao.get_numero_cartao_1()}.{cartao.get_numero_cartao_2()}.{cartao.get_numero_cartao_3()}.{cartao.get_numero_cartao_4()} \n" \
               f"Código verificador: {cartao.get_codigo_verificador()} \n" \
               f"Limite disponível: R${cartao.get_limite():.2f} \n" \
               f"Fatura atual: R${cartao.get_valor_fatura():.2f} \n"
 
    @staticmethod
    def main():
        import os
        from cartao_debito import CartaoDebito
        from cartao_credito import CartaoCredito
        credito_existe = False
        debito_existe = False

        opcao = 1
        while opcao != 0:
            opcao = Main.pedir_opcao()
            match opcao:
                case 1:
                    os.system("cls")
                    debito_existe = True
                    cartao_debito = CartaoDebito.criar_cartao_debito()
                    print("Cartão de débito criado com sucesso!")
                case 2:
                    os.system("cls")
                    credito_existe = True
                    cartao_credito = CartaoCredito.criar_cartao_credito()
                    print("Cartão de crédito criado com sucesso!")
                case 3:
                    os.system("cls")
                    opcao_dados = Main.pedir_dados("1 - Mostrar dados cartão de débito \n"
                                                "2 - Mostrar dados cartão de crédito\n"
                                                "Selecione a opção desejada: ")
                    match opcao_dados:
                        case "1":
                            os.system("cls")
                            if (debito_existe==False):
                                os.system("cls")
                                print("Você não possui um cartão de débito!")
                            else:
                                os.system("cls")
                                dados_debito = Main.mostrar_dados_debito(cartao_debito)
                                print(dados_debito)
                        case "2":
                            os.system("cls")
                            if (credito_existe==False):
                                os.system("cls")
                                print("Você não possui um cartão de crédito!")
                            else:
                                os.system("cls")
                                dados_credito = Main.mostrar_dados_credito(cartao_credito)
                                print(dados_credito)
                        case __:
                            os.system("cls")
                            print("Opção Inválida!")
                case 4:
                    os.system("cls")
                    opcao_dados = Main.pedir_dados("1 - Realizar compra no cartão de débito \n"
                                                   "2 - Realizar compra no cartão de crédito \n"
                                                   "Selecione a opção desejada: ")
                    match opcao_dados:
                        case "1":
                            if debito_existe==True:
                                os.system("cls")
                                cartao_debito.realizar_compra()
                            else:
                                os.system("cls")
                                print("Você não possui um cartão de débito!")
                        case "2":
                            if credito_existe==True:
                                os.system("cls")
                                cartao_credito.realizar_compra()
                            else:
                                os.system("cls")
                                print("Você não possui um cartão de crédito!")
                        case __:
                            os.system("cls")
                            print("Opção inválida!")
                case 5:
                    os.system("cls")
                    if debito_existe==True:
                        os.system("cls")
                        cartao_debito.sacar()
                    else:
                        os.system("cls")
                        print("Você não possui um cartão de débito!")
                case 6:
                    os.system("cls")
                    if debito_existe==True:
                        os.system("cls")
                        cartao_debito.depositar()
                    else:
                        os.system("cls")
                        print("Você não possui um cartão de débito!")
                case 7:
                    os.system("cls")
                    if credito_existe==True:
                        os.system("cls")
                        cartao_credito.pagar_fatura()
                    else:
                        os.system("cls")
                        print("Você não possui um cartão de crédito!")
                case 0:
                    os.system("cls")
                    print("Obrigada por utilizar o programa!")
                case __:
                    os.system("cls")
                    print("Opção Inválida!")

if __name__ == "__main__":
    Main.main()
