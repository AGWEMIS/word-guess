"""Part of logic of the 'GUESS the WORD' game"""

import random as r
from words_list import words

#random choice the word
def get_word():
    word = r.choice(words)
    while '-' in word or ' ' in word:
        word = r.choice(words)
    return word.upper()

#displays letters that found
def display(user_input, word):
    display_letter = ''
    for letter in word:
        if letter in user_input.upper():
            display_letter += letter
        else:
            display_letter += '-'
    return display_letter


    
























