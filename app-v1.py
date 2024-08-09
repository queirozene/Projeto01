# Projeto 1 - Game em linguagem Python - Versão 1

import random
from os import system, name


def clean_screen():

    # windows
    if name == 'nt':
        _ = system('cls')
    
    #mac ou linux
    else:
        _ = system('clear')


def game():

    clean_screen()
    print("\nBem vindo(a) ao jogo da forca!!")
    print("Adivinhe a palavra abaixo\n")

    # 1- Definir a lista de palavras possíveis
    palavras = ['banana', 'abacaxi', 'melancia', 'jabuticaba', 'mexerica', 'laranja', 'pera', 'graviola', 'melao', 'mangostao', 'manga']

    # 2- Escolher uma palavra aleatória da lista
    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]
    
    # 4- Definir o número máximo de tentativas permitidas
    chances = 8
    
    # 3- Criar uma lista vazia para armazenar as letras adivinhadas
    letras_incorretas = []

    # 5- Enquanto o número de tentativas não atingir o limite máximo:
    while chances > 0:

        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras incorretas:", " ".join(letras_incorretas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_incorretas.append(tentativa)

        if "_" not in letras_descobertas:
            print("Você venceu, a palavra era:", palavra)
            break
    
    if "_" in letras_descobertas:
        print("\nVocê perdeu! A palavra era:", palavra)


if __name__ == "__main__":
    game()