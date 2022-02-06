import random
from re import S
import replit
import os
import sys
import time


play = True


def run():


    IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    with open(os.path.join(sys.path[0], "palabras.txt"), encoding="utf8", errors='ignore') as f:
        DB = f.read().split()
    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6
    lista_usados = []
    
    while True:
        replit.clear()
        for character in spaces:
            print(character, end=" ")
        print(IMAGES[attemps])
        print(lista_usados)
        letter = input("Elegí una letra: ")

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
        if not found:
            attemps -= 1
            lista_usados.append(letter)
            
            
        if "_" not in spaces:
            replit.clear()
            print("Ganaste!! La palabra era " + word.upper())
            time.sleep(4)
            break
            
            
        if attemps == 0 :
            #replit.clear()
            print("Perdiste!! La palabra era " + word.upper())
            time.sleep(4)
            break
            
            # else:
            #     quit()
            
            

    run()

if __name__=='__main__':
    run()