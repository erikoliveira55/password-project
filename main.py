from utils import credenciais, acesso

class User:
    cont_instacia = 0 

    def __init__(self):
        User.cont_instacia += 1
        self.arquivo = f"banco_senhas{str(User.cont_instacia)}"
        self.instan_acesso = acesso(self.arquivo)

   
    def menu(self):

        while True:

            print("\nAcessar senhas (1)")
            print("Listar senha especifica (2)")
            print("Adicionar senhas ao arquivo de senhas (3)")
            print("Remover senha especifica (4)")

            match input('\n'):
                case '1':
                    self.saidas()
                case '2':
                    especif = input("Digite seu site especifico: \n")
                    self.saidas(especif)
                case '3':
                    self.novos_inputs()
                case '4':
                    especif = input("Digite seu site especifico\n")
                    self.remover(especif)
                case _:
                    print("Input invalido! ")
                    continue

    def novos_inputs(self):
        self.instan_acesso.novas_credenciais()

    def remover(self, especif):
        self.instan_acesso.remover_credenciais(especif)   

    def saidas(self, especif=None):
        
        if especif:
            self.instan_acesso.saida_especificada(especif)
        else:
            self.instan_acesso.saida()

pessoa = User()
pessoa.menu()
