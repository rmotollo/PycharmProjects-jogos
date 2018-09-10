def jogar():

    print("Bem vindo ao jogo da forca do Motollo")
    palavra_secreta = "banana"
    enforcou = False
    acertou = False



    while(not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip()

        index = 1
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
        print("jogando!")


if(__name__ == "__main__"):


