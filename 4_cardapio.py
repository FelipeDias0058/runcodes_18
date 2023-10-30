def main():

    subtotal = 0
    q_h = 0
    q_c = 0
    q_m = 0
    q_a = 0
    q_q = 0
        
    #O loop mostra o menu de opções e pede que um input do usuário,
    #parando o loop quando 'X' é digitado.
    while True:
        escolha = input().upper().strip()

        if escolha == "H":
            print("CÓDIGO  PRODUTO         PREÇO (R$)")
            print("H       Hamburger       5,50")
            print("C       Cheeseburger    6,80")
            print("M       Misto Quente    4,50")
            print("A       Americano       7,00")
            print("Q       Queijo Prato    4,00")
            print("X       PARA TOTAL DA CONTA")
            q_h += 1
            
        elif escolha == "C":
            print("CÓDIGO  PRODUTO         PREÇO (R$)")
            print("H       Hamburger       5,50")
            print("C       Cheeseburger    6,80")
            print("M       Misto Quente    4,50")
            print("A       Americano       7,00")
            print("Q       Queijo Prato    4,00")
            print("X       PARA TOTAL DA CONTA")
            q_c += 1
        elif escolha == "M":
            print("CÓDIGO  PRODUTO         PREÇO (R$)")
            print("H       Hamburger       5,50")
            print("C       Cheeseburger    6,80")
            print("M       Misto Quente    4,50")
            print("A       Americano       7,00")
            print("Q       Queijo Prato    4,00")
            print("X       PARA TOTAL DA CONTA")
            q_m += 1
        elif escolha == "A":
            print("CÓDIGO  PRODUTO         PREÇO (R$)")
            print("H       Hamburger       5,50")
            print("C       Cheeseburger    6,80")
            print("M       Misto Quente    4,50")
            print("A       Americano       7,00")
            print("Q       Queijo Prato    4,00")
            print("X       PARA TOTAL DA CONTA")
            q_a += 1
        elif escolha == "Q":
            print("CÓDIGO  PRODUTO         PREÇO (R$)")
            print("H       Hamburger       5,50")
            print("C       Cheeseburger    6,80")
            print("M       Misto Quente    4,50")
            print("A       Americano       7,00")
            print("Q       Queijo Prato    4,00")
            print("X       PARA TOTAL DA CONTA")
            q_q += 1
        elif escolha == "X":
            print("CÓDIGO  PRODUTO         PREÇO (R$)")
            print("H       Hamburger       5,50")
            print("C       Cheeseburger    6,80")
            print("M       Misto Quente    4,50")
            print("A       Americano       7,00")
            print("Q       Queijo Prato    4,00")
            print("X       PARA TOTAL DA CONTA")
            total = (q_h * 5.50) + (q_c * 6.80) + (q_m * 4.50) + (q_a * 7.00) + (q_q * 4.00)    
            print(f'{total:.2f}') #Quando o loop para, soma todos os itens e imprime o total
            break
        else:
            print("Não temos este item, desculpe.")
             
        
if __name__ == '__main__':
    main()
