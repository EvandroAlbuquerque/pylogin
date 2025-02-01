from controllers import PessoaController, LoginController

def menu_principal():
    print('==========> MENU <==========')
    opcao = input('\n\nDigite 1 para cadastrar\n'
                  'Digite 2 para logar\n'
                  'Digite 9 para sair\n\n\n')
    
    match opcao:
        case "1":
            print('Por favor, digite as informações da pessoa a ser cadastrada.\n\n')
            nome = input('Digite o nome: ')
            email = input('Digite o e-mail: ')
            senha = input('Digite a senha: ')
            PessoaController.cadastrar(nome=nome, email=email, senha=senha)
            menu_principal()
        case "2":
            print('Por favor, digite as informações para login.\n\n')
            email = input('Digite o e-mail: ')
            senha = input('Digite a senha: ')
            LoginController.login(email=email, senha=senha)
            menu_principal()
        case "9":
            exit()
        case _:
            print('Por favor, escolha uma opção válida.')
            menu_principal()
            

while True:
    menu_principal()