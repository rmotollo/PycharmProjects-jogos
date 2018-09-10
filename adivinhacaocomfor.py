def jogar():
    import random


    print("Bem vindo ao jogo de adivinhação do Motollo")

    #numero_secreto = 50
    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    rodada_num = 1
    pontos = 1000

    print("Escolha um nível de dificuldade:")
    print("1 - Fácil(total de tentativas 15)")
    print("2 - Médio(total de tentativas 10)")
    print("3 - Dificil(total de tentativas 5)")
    nivel = int(input("Opção:"))


    if(nivel == 1):
        total_tentativas = 15
    elif(nivel == 2):
        total_tentativas = 10
    elif(nivel == 3):
        total_tentativas = 5
    else:
        print("Opção inválida, saindo!")
        quit()


    for rodada_num in range(1, total_tentativas + 1):

        #Na linha abaixo utilizamos a interpolação de strings, função de formatação .format chamada de dentro  de outra função.
        print("Tentativa {} de {}.".format(rodada_num, total_tentativas))

        chute_str = input("digite seu número secreto:")
        print("Você chutou:", chute_str)
        chute_int = int(chute_str)

        if(chute_int < 1 or chute_int > 100):
            print("O valor deve ser entre 1 e 100!")
            continue

        acertou_chute = chute_int == numero_secreto
        chute_alto = chute_int > numero_secreto
        chute_baixo = chute_int < numero_secreto

        if(acertou_chute):
            print("Você acertou!")
            print("Você fez {} pontos.".format(pontos))
            break
        else:
            if(chute_alto):
                print("Você errou, chutou alto!")
                pontos_perdidos = abs(numero_secreto - chute_int)
                pontos = pontos - pontos_perdidos
            elif(chute_baixo):
                print("Você errou, chutou baixo!")
                pontos_perdidos = abs(numero_secreto - chute_int)
                pontos = pontos - pontos_perdidos




    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()