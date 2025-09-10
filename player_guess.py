"""
    computer choice random word, and player will guess.
"""

from logic import get_word, display


def iPlay():
    word = get_word()
    
    word_letters = set(word)
    user_input=''
    print(f'>>> The word have {len(word)} letters, let`s guess!!!')
    
    while len(word_letters)>0:
        print(display(user_input, word))
        if len(user_input)>0:
            print(f'>>> For now, the letters that you have entered - {user_input}')
        
        letter = input('Enter the Letter:  ').upper()
        if len(letter)==1 and letter.isalpha():
            if letter in user_input:
                print('>>> You have already entered this letter, please try other one..')
                continue
            elif letter in word:
                word_letters.remove(letter)
                print(f'{letter} is correct')
            else:
                print('>>> There word does not contain this letter.') 
        else:
            print('>>> Please enter 1 letter...')
            continue
            
        user_input += letter
    print(f'>>> Congrats! \n{word} found in {len(user_input)} attemps.')
    
    return len(user_input)