import forca
import adivinhacaocomfor

def jogos():
    print("Escolha o seu jogo")


    print("(1) Adivinhação")
    print("(2) Forca")
    jogo_opcao = int(input("Qual Jogo?"))

    if(jogo_opcao == 1):
        adivinhacaocomfor.jogar()
    elif(jogo_opcao == 2):
        forca.jogar()

if(__name__ == "__main__")

