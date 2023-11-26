#importando as principais bibliotecas
import json
import csv
from functools import reduce

#função para carregar os dados do arquivo json
def carregamento_dados():
    try:
        with open('dados_json.json', 'r', encoding='utf-8') as arquivo_json:
            dados_json = json.load(arquivo_json)
    except FileNotFoundError:
        dados_json = []
    return dados_json

#função para salvar os dados do arquivo json
def salvamento_dados(dados_json):
    with open('dados_json.json', 'w', encoding='utf-8') as arquivo_json:
        json.dump(dados_json, arquivo_json, indent=2, ensure_ascii=False)

#função para cadastrar as respostas da pesquisa 
def cadastro_eleitor():
    nome_cadastro = input(f'Qual seu nome?: ')
    idade_cadastro = int(input(f'Qual sua idade?: '))
    voto_cadastro = input(f'Qual candidato pretende votar?: ')
    
    dados_json = carregamento_dados()
    dados_json.append({'nome': nome_cadastro, 
                       'idade': idade_cadastro, 
                       'voto': voto_cadastro})
    salvamento_dados(dados_json)

#função para visualizar cadastro
def visualizando_resposta():
    dados_json = carregamento_dados()
    for resposta_eleitor in dados_json:
        print(resposta_eleitor)
#função para atualizar voto
def atualizando_voto():
    eleitor_cadastrado = input(f'Qual o nome do eleitor que quer atualizar?: ')
    novo_voto = input(f'Qual o novo candidato pretende votar?: ')
    dados_json = carregamento_dados()
    for dado_eleitor in dados_json:
        if dado_eleitor['nome'] == eleitor_cadastrado:
            dado_eleitor['voto'] = novo_voto
            print(f'Voto atualizado para {novo_voto}')
            salvamento_dados(dados_json)
            print(f'Resposta atualizada')
            return
    print(f'Eleitor não encontrado')

#função para deletar eleitor entrevistado
def deletando_eleitor():
    deletar_eleitor = input(f'Nome do eleitor para deletar: ')
    dados_json = carregamento_dados()
    dados_json = [dado_eleitor for dado_eleitor in dados_json 
                  if dado_eleitor['nome'] != deletar_eleitor]
    salvamento_dados(dados_json)

#função para visualizar idade média dos entrevistados
def idade_media():
    dados_json = carregamento_dados()
    if not dados_json:
        print('Não há cadastro')
        return
    dados_eleitores = [dado_eleitor['idade'] for dado_eleitor in dados_json]
    if dados_eleitores:
        soma_idade = reduce(lambda x, y: x + y, dados_eleitores)
        media_idade = soma_idade // len(dados_eleitores)
        print(f'A média da idade dos eleitores é: {media_idade:.0f}')

    with open('media_entrevistados.csv', 'w', newline='') as arquivo_csv:
        dado_media = csv.writer(arquivo_csv)
        dado_media.writerow(['Idade média dos entrevistados'])
        dado_media.writerow([media_idade])

#função para visualizar o entrevistado com maior e menor idade 
def idade_max_min():
    dados_json = carregamento_dados()
    if not dados_json:
        print('Dados não encontrados')
        return

    info_max = max(dados_json, key=lambda x: x['idade'])
    info_min = min(dados_json, key=lambda x: x['idade'])
 
    print(f'O entrevistado, ({info_max["nome"]}), possui a maior idade: {info_max["idade"]}')
    print(f'O entrevistado, ({info_min["nome"]}), possui a menor idade:  {info_min["idade"]}')

#função para filtrar os eleitores entrevistados por candidato 
def eleitores_candidato():
    dados_json = carregamento_dados()
    if not dados_json:
        print('Dados não encontrados')
        return
    
    candidatos_pesquisa = set(eleitor_pesquisa['voto'] for eleitor_pesquisa in dados_json)

    for candidato_unico in candidatos_pesquisa:
        eleitores_filtrados = filter(lambda x: x['voto'] == candidato_unico, dados_json)
        print(f'Eleitores que votaram em {candidato_unico}:')
        for eleitor_unico in eleitores_filtrados:
            print(eleitor_unico)
        print('-' * 30)

#função principal do programa 
def main(): 
        while True:
            print('-' * 30)
            print(f'1. Cadastrar pesquisado')
            print(f'2. Visualizar cadastro dos pesquisados')
            print(f'3. Idade média dos pesquisados')
            print(f'4. Atualizar voto dos pesquisados')
            print(f'5. Deletar pesquisado')
            print(f'6. Visualizar idade max ou min dos pesquisados')
            print(f'7. Visualizar eleitores por candidato')
            print(f'8. Sair')
            print('-' * 30)

            opcao_pesquisa = input(f'Escolha uma das opções: ')
            
            if opcao_pesquisa == '1':
                cadastro_eleitor()
            elif opcao_pesquisa == '2':
                visualizando_resposta()
            elif opcao_pesquisa == '3':
                idade_media()
            elif opcao_pesquisa == '4':
                atualizando_voto()
            elif opcao_pesquisa == '5':
                deletando_eleitor()
            elif opcao_pesquisa == '6':
                idade_max_min()
            elif opcao_pesquisa == '7':
                eleitores_candidato()
            elif opcao_pesquisa == '8':
                break
            else: 
                print(f'Opção inexistente')
            
            print()

if __name__ == "__main__":
    main()