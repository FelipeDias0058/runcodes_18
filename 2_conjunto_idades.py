#Importa o módulo de estatísticas
import statistics

#Adiciona os números à variável 'lista_idades'
def f_lista(lista_idades):
    while True:
        n = int(input())
        if n > 0:
            lista_idades.append(n)
        if n <= 0: break

def main():

    #Guarda os números digitados
    lista_idades = []

    #Executa a função
    f_lista(lista_idades)

    #Variáveis, formatadas
    media = statistics.mean(lista_idades)
    menor_idade = min(lista_idades)
    maior_idade = max(lista_idades)
    
    #Saída de Dados
    print(len(lista_idades))
    print(f'{media:.2f}')
    print(menor_idade)
    print(maior_idade)

if __name__ == '__main__':
    main()
