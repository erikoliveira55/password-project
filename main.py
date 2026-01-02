from logica import acesso, credenciais

class User:
    cont_instacia = 0 

    def __init__(self):
        User.cont_instacia += 1
        self.arquivo = f"banco_senhas{str(User.cont_instacia)}"
        self.instan_crede = credenciais(self.arquivo)
        self.instan_acesso = acesso()

    @staticmethod
    def menu():

        while True:

            print("\nAcessar senhas (1)")
            print("Listar senha especifica (2)")
            print("Adicionar senhas ao arquivo de senhas (3)")
            print("Remover senha especifica (4)")

            match input('\n'):
                case '1':
                    User.saidas()
                case '2':
                    especif = input("Digite seu site especifico: ")
                    User.saidas(especif)
                case '3':
                    User.novos_inputs()
                case '4':
                    especif = input("Digite seu site especifico")
                    User.remover(especif)
                case _:
                    print("Input invalido! ")
                    continue

    def novos_inputs(self):
        self.instan_crede.novas_credenciais()

    def remover(self, especif):
        self.instan_crede.remover_credenciais(especif)   

    def saidas(self, especif=None):
        
        if especif:
            self.instan_acesso.saida_especificada()
        else:
            self.instan_acesso.saida() 
