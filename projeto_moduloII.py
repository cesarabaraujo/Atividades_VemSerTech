#importando as principais bibliotecas
import json
import csv

#função para carregar os dados do arquivo json
def carregamento_dados():
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

#função para cadastrar as respostas da pesquisa 
def cadastro_eleitor():
    nome_cadastro = input(f'Qual seu nome?: ')
    idade_cadastro = int(input(f'Qual sua idade?: '))
    voto_cadastro = input(f'Qual candidato pretende votar?: ')
    
    dados_json = carregamento_dados()
    dados_json.append({'nome_eleitor': nome_cadastro, 
                       'idade_eleitor': idade_cadastro, 
                       'voto_cadastro': voto_cadastro})
    salvamento_dados(dados_json)

#função para visualizar cadastro
def visualizando_resposta():
    dados_json = carregamento_dados()
    for resposta_eleitor in dados_json:
        print(resposta_eleitor)

#função para atualizar voto
def atualizando_voto():
    eleitor_cadastrado = input(f'Qual o nome do eleitor que quer atualizar?: ')
    novo_voto = input(f'Qual o novo candidato pretende votas?: ')
    dados_json = carregamento_dados()
    for dado_eleitor in dados_json:
        if dado_eleitor['nome_eleitor'] == eleitor_cadastrado:
            dado_eleitor['voto_cadastro'] = novo_voto
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
                  if dado_eleitor['nome_eleitor'] != deletar_eleitor]
    salvamento_dados(dados_json)

#função para visualizar idade média dos entrevistado
def idade_media():
    dados_json = carregamento_dados()
    if not dados_json:
        print('Não há cadastro')
        return
    dados_eleitores = [dado_eleitor['idade_eleitor'] for dado_eleitor in dados_json]
    if dados_eleitores: 
        soma_idade = sum(dados_eleitores)
        media_idade = soma_idade / len(dados_eleitores)
        print(f'A média da idade dos eleitores é: {media_idade:.2f}')
    
def idade_max_min():
    dados_json = carregamento_dados()
    if not dados_json:
        print('Dados não encontrados')
        return
    try:
        dados_eleitores = [dado_eleitor['idade_eleitor'] for dado_eleitor in dados_json]
    except KeyError:
        print('Dados de idade não encontrados')
        return
    
    idade_max = max(zip(dados_json, dados_eleitores), key=lambda dado: dado[1])
    idade_min = min(zip(dados_json, dados_eleitores), key=lambda dado: dado[1])
 
    print(f'Maior idade: {idade_max[1]} ({idade_max[0]["nome_eleitor"]})')
    print(f'Menor idade: {idade_min[1]} ({idade_min[0]["nome_eleitor"]})')

#função principal do nosso programa 
def main(): 
        while True:
            print(f'1. Cadastrar pesquisado')
            print(f'2. Visualizar cadastro dos pesquisados')
            print(f'3. Idade média dos pesquisados')
            print(f'4. Atualizar voto dos pesquisados')
            print(f'5. Deletar pesquisado')
            print(f'6. Visualizar idade max ou min dos pesquisados')
            print(f'7. Sair')

            opcao_pesquisa = input(f'Escolha uma das opções:')
            
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
                break
            else: 
                print(f'Opção inexistente')

if __name__ == "__main__":
    main()