import json
import os

class metodos_internos:

    atributo_dados = {}

    def __init__(self, arquivo):

        self.arquivo = arquivo
        try:
            print("Carregando seus dados do banco de dados...\n")

            with open(self.arquivo, 'r') as f:
                dados = json.load(f)
            self.seus_dados = dados
            
        except:
            print("Falhou...\n")
            print("Criando seu banco de dados")
            self.seus_dados = self._arquivo_criar()

        self.atributo_dados.self._arquivo_criar()

    def _arquivo_criar(self):

        with open(self.arquivo, 'w') as f:
            dados = {}
            json.dump(dados, f)

        return dados
        

    
    def _salvar(self, dados_novos):


        with open(self.arquivo, 'w+') as f:
            json.dump(dados_novos, f)
            
    
    def _verificador(self, novos_dados):

        chaves_iguais = []

        for i in novos_dados:
            
            verifica = self.dados.get(i)

            if verifica:

                chaves_iguais.append(i)

                raise KeyError(f"Chaves ja registrada | {chaves_iguais}")
            
        self._salvar(novos_dados)
                


class credenciais(metodos_internos):
    
    def __init__(self, arquivo):
        super().__init__(arquivo)

    def novas_credenciais(self):

        novos_dados = {}

        print("======Digite x para sair: ======\n")
        while True:

            novo_site = input("Digite o site: ").strip()

            if novo_site.lower() == 'x':
                print("\nVocê saiu da função adicionar senhas!")
                break

            nova_senha = input("Digite sua senha: \n").strip()

            if not nova_senha:
                print("Senha vazia! Tente novamente.\n")
                continue

            novos_dados[novo_site] = nova_senha
            self._verificador(novos_dados)
    

    def remover_credenciais(self, especif):
        if especif in self.atributo_dados:
            del self.atributo_dados[especif]
        else:
            print("Chave inexistente! ")    
    

class acesso(metodos_internos):
    
    def saida(self):
        for chave, valor in self.atributo_dados.items():
            print(f'\t| {chave} | = ( {valor} )\n')

    def saida_especificada(self):

        especifica = input("Digite seu site especifico: ")

        saida = self.atributo_dados.get(especifica)

        if saida:
            print(f'\t | {especifica} | = ({self.atributo_dados[especifica]})')
        else: 
            print("Chave nao encontrada! ")    
