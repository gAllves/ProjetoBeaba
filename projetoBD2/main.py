from database import Database
from pessoaCRUD import PessoaCRUD 
from cli import PessoaCLI

#Faz a conexão com o banco no Neo4j
db = Database("bolt://3.87.13.212:7687", "neo4j", "step-brothers-rooms")

#Cria um objeto PessoaCRUD
pessoa = PessoaCRUD(db)

#Cria um objeto PessoaCLI
cli = PessoaCLI(pessoa)

#Inicia o CLI
cli.run()

#Pesquisando o livro mais antigo da biblioteca
'''
query = "MATCH (l:Livro) RETURN l.titulo AS Título ORDER BY l.ano LIMIT 1"
print("Livro mais antigo da biblioteca: ")
print(db.execute_query(query))

#Pesquisando a pessoa mais velha cadastrada
query = "MATCH (p:Pessoa) RETURN p.nome AS Nome ORDER BY p.idade DESC LIMIT 1"
print("Pessoa mais velha cadastrada: ")
print(db.execute_query(query))
'''

#Fecha a conexão com o Banco de Dados
db.close()

