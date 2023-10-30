#Adiciona os números à variável 'lista'
def f_soma_lista(lista):
    while True:
        n = int(input())
        lista.append(n)
        if n == 0: break

def main():

    #Guarda os números digitados
    lista = []

    #Executa a função
    f_soma_lista(lista)

    #Saída de Dados
    print(sum(lista))

if __name__ == '__main__':
    main()
