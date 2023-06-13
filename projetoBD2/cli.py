from pessoa import Pessoa
from livro import Livro


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com o comando: ")
            if command == "quit":
                print("Programa finalizado!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Por favor entre novamente!")


class PessoaCLI(SimpleCLI):
    def __init__(self, pessoa_model):
        super().__init__()
        self.pessoa_model = pessoa_model
        #Adicionando comandos para o CLI
        self.add_command("createPessoa", self.create_pessoa)  #cria uma nova Pessoa
        self.add_command("createLivro", self.create_livro) #cria um novo Livro
        self.add_command("createRelacao", self.create_relacao) #cria uma nova Relação
        self.add_command("readPessoa", self.read_pessoa) #lê uma Pessoa e o livro que ela alugou
        self.add_command("readLivro", self.read_livro) #lê um Livro 
        self.add_command("update", self.update_pessoa) #atualiza o cpf de uma Pessoa
        self.add_command("delete", self.delete_pessoa) #deleta uma Pessoa

    #Função para criar uma nova Pessoa
    def create_pessoa(self):
        name = input("Entre com o nome: ")
        idade = int(input("Entre com a idade: "))
        cpf = input("Entre com o CPF: ")
        self.pessoa_model.create_pessoa(name, idade, cpf)

        #Cria um objeto pessoa
        pessoa = Pessoa(name, idade, cpf, None)
        print("Pessoa criada com sucesso")

    #Função para criar um novo Livro
    def create_livro(self):
        titulo = input("Entre com o titulo: ")
        ano = int(input("Entre com o ano de lançamento: "))
        autor = input("Entre com o nome do autor: ")
        genero = input("Entre com o genero: ")
        self.pessoa_model.create_livro(titulo, ano, autor, genero)

        #Cria um objeto livro
        livro = Livro(titulo, ano, autor, genero)
        print("Livro criado com sucesso")

        

    #Função para criar uma nova Relação
    def create_relacao(self):
        name = input("Entre com o nome da pessoa: ")
        titulo = input("Entre com o titulo do livro: ")
        data = input("Entre com a data de aluguel: (dd/mm/aaaa) ")
        self.pessoa_model.create_relacao(data, name, titulo)

        #Criando um objeto pessoa com o livro alugado

        result1 = self.pessoa_model.read_livro(titulo)
        livro = Livro(titulo, result1[0][0], result1[0][1], result1[0][2])

        result2 = self.pessoa_model.read_pessoa(name)
        pessoa = Pessoa(name, result2[0][1], result2[0][1], livro)

        print("Relação criada com sucesso")



    #Função para ler uma Pessoa
    def read_pessoa(self):
        name = input("Entre com o nome: ")
        pessoa = self.pessoa_model.read_pessoa(name)
        if pessoa:
            print(pessoa)
            livro = self.pessoa_model.read_livro_by_person(name)
            if livro:
                print("Livro(s) alugado(s):")
                print(livro)
            else:
                print("Pessoa ainda não alugou nenhum livro")

    #Função para ler um Livro
    def read_livro(self):
        titulo = input("Entre com o titulo: ")
        livro = self.pessoa_model.read_livro(titulo)
        if livro:
            print(livro)
        else:
            print("Livro não encontrado")
            
    #Função para atualizar uma Pessoa    
    def update_pessoa(self):
        cpf = input("Entre com o CPF da Pessoa: ")
        nome = input("Entre com o novo nome: ")
        idade = int(input("Entre com a nova idade: "))
        self.pessoa_model.update(cpf, nome ,idade)
        print("Pessoa atualizada com sucesso")

    #Função para deletar uma Pessoa
    def delete_pessoa(self):
        name = input("Entre com o nome: ")
        self.pessoa_model.delete(name)
        print("Pessoa deletada com sucesso")
        
    #Função para rodar o CLI
    def run(self):
        print("Bem vindo a Biblioteca Beabá CLI!")
        print("Comandos disponíveis: createPessoa, createLivro, createRelacao, readPessoa, readLivro, update, delete, quit")
        super().run()
        