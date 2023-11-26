#importando as principais bibliotecas
import json 
import random

#função para gerar nomes dos entrevistados aleatoriamente 
def nomes_entrevistados(lista_nomes):
    lista_entrevistados = ['Isabele', 'Lala', 'Julio', 'Aldrin', 'Will', 'Ana', 'Henrique',
                       'Larissa', 'Camila', 'Mariana', 'Judá', 'Juarez', 'Levi', 'Júlia',
                       'Maria', 'João', 'Flávia', 'André', 'Marta', 'Aquiles', 'Socrátes',
                       'Kant', 'Platão', 'Sparta', 'Helena', 'Era', 'Eva', 'Adão']
    
    nome_unico = [nome_lista for nome_lista in lista_entrevistados if nome_lista not in lista_nomes]

    if nome_unico:
        nome_escolhido = random.choice(nome_unico)
        lista_nomes.append(nome_escolhido)
        return nome_escolhido
     
#função para gerar idades aleatória para os entrevistados
def idade_entrevistados():
    return random.randint(18, 100)

#função para gerar os votos nos candidatos de forma aleátoria 
def voto_entrevistados():
    lista_candidatos = ['Candidato1', 'Candidato2', 'Candidato3', 'Candidato4', 'Candidato5']
    return random.choice(lista_candidatos)

#função para gerar o cadastro inicial dos entrevistados de forma aleátoria 
def gerador_cadastro():
    nomes_utilizados = []
    nome_entrevistado = nomes_entrevistados(nomes_utilizados)
    idade_entrevistado = idade_entrevistados()
    voto_entrevistado = voto_entrevistados()
    return {'nome': nome_entrevistado, 'idade': idade_entrevistado, 'voto': voto_entrevistado}

#cria variável que guarda lista de dicionários com os cadastros aleatórios
cadastro_aleatorio = [gerador_cadastro() for _ in range(28)]

#salvar cadastros aleatórios em um arquivo json
with open('dados_json.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(cadastro_aleatorio, arquivo_json, indent=2, ensure_ascii=False)
