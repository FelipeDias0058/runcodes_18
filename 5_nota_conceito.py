def main():

    #Se a nota estiver entre 0 e 10, avança para as condicionais.
    #Se a nota for inválida, imprime um aviso e repete o input.
    while True:
        nota = float(input(""))

        if 0 <= nota <= 10:
            break
        else:
            print("Nota inválida.")


    #As condicionais atribuem uma letra dependendo da nota.        
    if nota >= 8.5:
        conceito = "A"
    elif nota >= 7.0:
        conceito = "B"
    elif nota >= 5.0:
        conceito = "C"
    elif nota >= 4.0:
        conceito = "D"
    elif nota >= 0.0:
        conceito = "E"

    #Saída de Dados
    print(f"{conceito}")

if __name__ == '__main__':
    main()

