class PessoaCRUD():
    def __init__(self, database):
        self.database = database

    #Função para criar uma nova Pessoa
    def create_pessoa(self, nome, idade, cpf): 
        query = f"CREATE (p:Pessoa {{nome: '{nome}', idade: '{idade}', cpf: '{cpf}'}})"
        self.database.execute_query(query)

    #Função para criar um novo Livro
    def create_livro(self, titulo, ano, autor, genero): 
        query = f"CREATE (l:Livro {{titulo: '{titulo}', ano: '{ano}', autor: '{autor}', genero: '{genero}'}})"
        self.database.execute_query(query) 

    #Função para criar uma nova Relação
    def create_relacao(self, data, nome, titulo): 
        query = f"MATCH (p:Pessoa {{nome: '{nome}'}}) MATCH (l:Livro {{titulo: '{titulo}'}}) CREATE (p)-[r:Alugou {{data: '{data}'}}]->(l)"
        self.database.execute_query(query)

    #Função para ler uma Pessoa
    def read_pessoa(self, nome):
        query = f"MATCH (p:Pessoa {{nome: '{nome}'}}) RETURN p.nome AS nome, p.idade AS idade, p.cpf AS cpf"
        results = self.database.execute_query(query)
        return [(result["nome"], result["idade"], result["cpf"]) for result in results]
    
    #Função para ler um Livro
    def read_livro(self, titulo):
        query = f"MATCH (l:Livro {{titulo: '{titulo}'}}) RETURN l.titulo AS titulo, l.ano AS ano, l.autor AS autor, l.genero AS genero"
        results = self.database.execute_query(query)
        return [(result["titulo"], result["ano"], result["autor"], result["genero"]) for result in results]
    
    #Função para deletar uma Pessoa
    def delete(self, nome):  
        query = f"MATCH (p:Pessoa {{nome: '{nome}'}}) DETACH DELETE p"
        self.database.execute_query(query)

    #Função para atualizar uma Pessoa
    def update(self, cpf, nome, idade): 
        query = f"MATCH (p:Pessoa {{cpf: '{cpf}'}}) SET p.nome = '{nome}', p.idade = '{idade}'"
        self.database.execute_query(query)

    #Função para ler o livro que uma Pessoa alugou
    def read_livro_by_person(self, nome): 
        query = f"MATCH (p:Pessoa {{nome: '{nome}'}})-[r:Alugou]->(l:Livro) RETURN l.titulo AS titulo"
        results = self.database.execute_query(query)
        return [(result["titulo"]) for result in results]
    
   