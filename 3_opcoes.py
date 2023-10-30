def main():

    #O loop mostra o menu de opções e pede que um input do usuário,
    #parando o loop quando '0' é digitado.
    while True:
        print('''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')
        
        escolha = int(input())

        if escolha == 1:
            print("1 - Olá. Como vai?")
        elif escolha == 2:
            print("2 - Vamos estudar mais.")
        elif escolha == 3:
            print("3 - Meus Parabéns!")
        elif escolha == 0:
            print("0 - Fim de serviço.")
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    main()
