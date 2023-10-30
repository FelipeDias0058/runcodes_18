def main():

    #Se a nota estiver entre 0 e 10, avança para as condicionais.
    #Se a nota for inválida, imprime um aviso e repete o input.
    while True:
        try:
            nota = float(input())
        except ValueError:
            print("Nota inválida.")
            continue
        else:
            break

    #As condicionais atribuem uma letra dependendo da nota.        
    if nota >= 8.5:
        conceito = "A"
    elif nota >= 7.0:
        conceito = "B"
    elif nota >= 5.0:
        conceito = "C"
    elif nota >= 4.0:
        conceito = "D"
    else:
        conceito = "E"

    #Saída de Dados
    print(f"{conceito}")

if __name__ == '__main__':
    main()
