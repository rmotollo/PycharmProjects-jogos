def jogar():
    print("Bem vindo ao jogo de adivinhação do Motollo")

    numero_secreto = 33
    total_tentativas = 3
    rodada_num = 1
    while(rodada_num <= total_tentativas):

        #Na linha abaixo utilizamos a interpolação de strings, função de formatação .format chamada de dentro  de outra função.
        print("Tentativa {} de {}.".format(rodada_num, total_tentativas))

        chute_str = input("digite seu número secreto:")
        print("Você chutou:", chute_str)
        chute_int = int(chute_str)

        acertou_chute = chute_int == numero_secreto
        chute_alto = chute_int > numero_secreto
        chute_baixo = chute_int < numero_secreto

        if(acertou_chute):
            print("Você acertou!")
        elif(chute_alto):
            print("Você errou, chutou alto!")
        elif(chute_baixo):
            print("Você errou, chutou baixo!")

        rodada_num = rodada_num + 1

    print("Fim do jogo!")