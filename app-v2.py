# Projeto 1 - Game em linguagem Python - Versão 2

import random
from os import system, name


def clean_screen():

    # windows
    if name == 'nt':
        _ = system('cls')

    # mac ou linux
    else:
        _ = system('clear')


# Função que desenha a forca na tela
def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 8 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 7
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 6
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]


def game():

    clean_screen()

    print("\nBem vindo(a) ao jogo da forca!!")
    print("Adivinhe a palavra abaixo\n")

    # 1- Definir a lista de palavras possíveis
    palavras = ['banana', 'abacaxi', 'melancia', 'jabuticaba', 'mexerica',
                'laranja', 'pera', 'graviola', 'melao', 'mangostao', 'manga']

    # 2- Escolher uma palavra aleatória da lista
    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    # 4- Definir o número máximo de tentativas permitidas
    chances = 8

    # 3- Criar uma lista vazia para armazenar as letras adivinhadas
    letras_incorretas = []
    letras_tentadas = set()

    # 5- Enquanto o número de tentativas não atingir o limite máximo:s
    while chances > 0:

        print(display_hangman(chances))
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras incorretas:", " ".join(letras_incorretas))

        while True:
            tentativa = input("\nDigite uma letra: ").lower()
            
            if len(tentativa) != 1 or not tentativa.isalpha():
                print("Entrada inválida. Por favor, digite apenas uma letra.")
            elif tentativa in letras_tentadas:
                print(f"Você já tentou a letra '{tentativa}'. Tente outra letra.")
            else:
                letras_tentadas.add(tentativa)
                break


        clean_screen()
        

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
        print("""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """)
        print("\nVocê perdeu! A palavra era:", palavra)


if __name__ == "__main__":
    while True:
        game()
        resposta = input("Você quer jogar de novo? (sim/não): ").strip().lower()
        if resposta == "não":
            print("Finalizando o programa.")
            break
        elif resposta != "sim":
            print("Resposta inválida. Finalizando o programa.")
            break
