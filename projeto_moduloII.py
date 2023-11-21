#importando as principais bibliotecas
import json
import csv

#função para carregar os dados do arquivo json
def carregamento_dados ():
    try:
        with open ('dados_json.json', 'r') as arquivo_json:
            dados_json = json.load(arquivo_json)
    except FileNotFoundError:
        dados_json = []
    return dados_json

#função para salvar os dados do arquivo json
def salvamento_dados(dados_json):
    with open('dados_json.json', 'w') as arquivo_json:
        json.dump(dados_json, arquivo_json, indent=2)

#função para cadastrar as respostas do questionário
def cadastro_eleitor ():
    nome_cadastro = input(f'Qual seu nome?: ')
    idade_cadastro = int(input(f'Qual sua idade?: '))
    voto_cadastro = input(f'Qual candidato pretende votar?: ')
    
    dados_json = carregamento_dados()
    dados_json.append({'nome_eleitor': nome_cadastro, 
                       'idade_eleitor': idade_cadastro, 
                       'voto_cadastro': voto_cadastro})
    
    salvamento_dados(dados_json)

#função para visualizar cadastro
def visualizar_resposta():
    dados_json = carregamento_dados
    for resposta_eleitor in dados_json:
        print(resposta_eleitor)

#função para visualizar estatística dos eleitores
def dados_estatisticos():
    dados_json = carregamento_dados()
    if not dados_json:
        print('Não há cadastro')
        return
    
    dados_eleitor = 'idade_eleitor'
    dado_estatistico = input(f'Digite max para valor máximo,
                              min para valor minímo,
                             med para mediana, mod para moda 
                             mea para média:  ')
    
    try:
        