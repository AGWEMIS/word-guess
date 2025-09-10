"""
pc guesses the word, that player is going to choose
"""
from words_list import alphabet
from player_guess import iPlay
import random as r

def pcPlay():
    print('>>> Let`s play! <<<')
    word_len = int(input('How many letters in you word(set)\n>>> '))
    pc_input = ''
    pc_found = []
    
    while True:
        letter = r.choice(alphabet)
        if len(pc_input) == len(alphabet):
            print('There is not any letter left that unused...')
            break
        
        if letter not in pc_input:
            print(f'I guess the {letter.upper()} letter...')
            pc_input += letter
        else:
            continue
        
        while True:
            sign = input('If this letter in your word, type "+", if not "-"\n>>> ')
            if sign == "+":
                pc_found.append(letter)
                print("YEhoooo, I found one, let`s continue...")
                break
            elif sign == "-":
                print("My BAD, next time I will find it! ")
                break
            else:
                print("Please, give me right info")
                print('If true type "+", if not "-"\n>>> ')
                
        if len(pc_found) == word_len:
            print(f'I DID IT!\n you see, in {len(pc_input)} attemps.')
            break
        
    return len(pc_input)
        
        
        
    