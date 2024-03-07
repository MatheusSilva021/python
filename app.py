import os

restaurants = [] # Listas são mutáveis, para definir uma lista só usar os colchetes [], Dicionários usam chave e valor
options_list = ('1. Cadastrar restaurante','2. Listar restaurantes','3. Alternar Estado do Restaurante','4. Sair\n') #tuplas são parecidos com as listas, porém imutáveis, para definir uma tupla, só usar os parenteses ()

def show_name():
    '''Função para exibir o nome'''
    
    print('---------------')
    print('App pedidos')
    print('---------------\n')

def go_back_to_menu():
    '''Função para retornar ao menu'''
    input('\nAperte qualquer tecla para voltar ao menu\n')
    main()

def define_subtitle(subtitle):
    '''Função para exibir o titulo especifico dentro de cada opção
    
    Input: 
    - titulo(string)
    
    Output: 
    - titulo(string): exibido com travessões em cima e embaixo
    '''
    
    os.system('cls')
    lines = '-' * (len(subtitle))
    print(lines)
    print(subtitle)
    print(f'{lines}\n')
 
def options():
    '''Função para exibir as opções, que estão dentro de uma tupla'''
    
    for option in options_list:
        print(f'{option}')

def register_new_restaurant():
    '''Função para cadastrar um restaurante
    
    Inputs: 
    - Nome do restaurante(string)
    - Categoria do restaurante(string)
    
    Outputs:
    - Adicionar um restaurante a lista
    
    '''
    
    define_subtitle('Cadastrar restaurante',)
    rest_name = input('Nome do restaurante:')
    rest_category = input('Categoria do restaurante:')
    if not rest_name or not rest_category:
        print(f'\nO nome do restaurante e a categoria do restaurante não podem ser vazios')
        go_back_to_menu()
    else:
        restaurants.append({'name': rest_name,'category': rest_category,'active': False})
        print(f'\nO Restaurante "{rest_name}" foi cadastrado com sucesso')
        go_back_to_menu()

def show_restaurants():
    '''Função para exibir os restaurantes
    
    Outputs:
    - Lista de restaurantes
    '''
    
    define_subtitle('Lista de Restaurantes')
    if len(restaurants) == 0:
        print('Nenhum restaurante cadastrado')
        go_back_to_menu()
    elif len(restaurants) >= 1:
        print(f'{'Nome do restaurante'.ljust(20)}|{'Categoria do restaurante'.ljust(20)}|Ativo?')
        for restaurant in restaurants:
            name = restaurant['name']
            category = restaurant['category']
            active = 'Sim' if restaurant['active'] else 'Não'
            print(f'{name.ljust(20)}|{category.ljust(24)}|{active}')
        go_back_to_menu()
    else:
        print('Ocorreu algum erro.')
        go_back_to_menu()

def activate_restaurant():
    '''Função para ativar um restaurante
    
    Inputs:
    - Nome do restaurante(string)
    
    Output:
    - restaurant_found(bool): se for Verdadeiro, é equivalente a Sucesso na atualização, caso Falso, não foi alterado
    - Alterar o estado do restaurante
    '''
    
    define_subtitle('Alternar Estado do Restaurante')
    restaurant_name = input('Nome do Restaurante que deseja alterar o estado:')
    restaurant_found = False
    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            restaurant['active'] = not restaurant['active']
            restaurant_found = True
    if restaurant_found:
        print(f'O restaurante "{restaurant_name}" foi alterado com sucesso')
    else:
        print('O restaurante não foi encontrado')
    go_back_to_menu()
    
def end_program():
    '''Função para exibir a mensagem de finalização do programa'''
    
    os.system('cls')
    define_subtitle('Finalizando Programa')
    
def invalid_option():
    '''Função para exibir a mensagem de opção inválida'''
    
    print('Opção inválida \n')
    go_back_to_menu()
    
def options_response():
    '''Função para verificar a resposta recebida através do menu
    
    Inputs:
    - response (int)
    
    Outputs:
    - Retorna o método da opção escolhida
    
    '''
    
    try:
        response = int(input('Escolha uma opção: '))
        
        if response == 1:
            register_new_restaurant()

        elif response == 2:
            show_restaurants()

        elif response == 3:
            activate_restaurant()
            
        elif response == 4:
            end_program()
            
        else:
            invalid_option()
            
    except:
        invalid_option()

def main():
    '''Função main, executada caso o __name__ seja __main__'''
    
    os.system('cls')
    show_name() # Mostrar nome do app
    options() # Mostrar opções
    options_response() # Resultado da opção escolhida
    
if __name__ == '__main__':
    main()