import os
import time

restaurantes = [
    {'nome':'Pizzaria Suprema', 'categoria':'Pizzaria', 'ativo':True},
    {'nome':'Mizaki Sushi', 'categoria':'Japonesa', 'ativo':True},
    {'nome':'Puro Açaí', 'categoria':'Brasileira', 'ativo':False}
    ]


def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print("""
╭━━━┳━━━┳━━╮╭━━━┳━━━╮ ╭━━━┳━╮╭━┳━━━┳━━━┳━━━┳━━━┳━━━╮
┃╭━╮┃╭━╮┃╭╮┃┃╭━╮┃╭━╮┃ ┃╭━━┻╮╰╯╭┫╭━╮┃╭━╮┃╭━━┫╭━╮┃╭━╮┃
┃╰━━┫┃╱┃┃╰╯╰┫┃╱┃┃╰━╯┃ ┃╰━━╮╰╮╭╯┃╰━╯┃╰━╯┃╰━━┫╰━━┫╰━━╮
╰━━╮┃╰━╯┃╭━╮┃┃╱┃┃╭╮╭╯ ┃╭━━╯╭╯╰╮┃╭━━┫╭╮╭┫╭━━┻━━╮┣━━╮┃
┃╰━╯┃╭━╮┃╰━╯┃╰━╯┃┃┃╰╮ ┃╰━━┳╯╭╮╰┫┃╱╱┃┃┃╰┫╰━━┫╰━╯┃╰━╯┃
╰━━━┻╯╱╰┻━━━┻━━━┻╯╰━╯ ╰━━━┻━╯╰━┻╯╱╱╰╯╰━┻━━━┻━━━┻━━━╯
""")

def exibir_opcoes_do_programa():
    ''' Exibe todas as opções no Menu Principal'''
    print('1. Cadastrar restaurante')
    print('2. Lista de restaurantes')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair\n')

def voltar_ao_menu():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao Menu Principal ')
    main()

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes

    '''
    exibir_subtitulo('🅒🅐🅓🅐🅢🅣🅡🅞 🅓🅔 🅝🅞🅥🅞🅢 🅡🅔🅢🅣🅐🅤🅡🅐🅝🅣🅔🅢\n')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_novo_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}

    print(f'\n O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')


    restaurantes.append(dados_do_novo_restaurante)
    voltar_ao_menu()

def lista_de_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela junto com a categoria e status
    '''
    exibir_subtitulo('🅛🅘🅢🅣🅐 🅓🅔 🅡🅔🅢🅣🅐🅤🅡🅐🅝🅣🅔🅢\n')

    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status\n'.upper())

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'

        print(f'-> {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu()

def ativar_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('🅐🅣🅘🅥🅐🅡/🅓🅔🅢🅐🅣🅘🅥🅐🅡 🅡🅔🅢🅣🅐🅤🅡🅐🅝🅣🅔\n')

    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu()

def escolher_opcao_no_programa():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            lista_de_restaurantes()
        elif opcao_escolhida == 3: 
            ativar_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida!\n')
    voltar_ao_menu()

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    print('Finalizando o app...\n')
    time.sleep(2)
    os.system('cls')



def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes_do_programa()
    escolher_opcao_no_programa()

if __name__ == '__main__':
    main()