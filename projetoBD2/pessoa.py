from livro import Livro

class Pessoa:
    def __init__(self, nome: str , idade: int, cpf: str, livro: Livro):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.livro = livro