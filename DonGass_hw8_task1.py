#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:22:26 2017

@author: Don Gass
"""

def hidden_word(word, guesses): 
    return ''.join([c if c in guesses else '-' for c in word])

def success(hidden_word):
    return True if '-' not in hidden_word else False

word = 'onomatopoeia'
max_number_guesses_allowed = 10
guess_number = 1
guesses = ''

while True:
    user_input = input('Enter a character (guess #%d): ' % guess_number)
    if len(user_input) != 1:
        print("You did not enter a single character. Please try again.")
        continue
    
    guesses += user_input
    print(hidden_word(word, guesses))
    
    if success(hidden_word(word, guesses)):
        print("Winner!")
        break
    
    if guess_number == max_number_guesses_allowed:
        print("Loser! The word was %s" % word)
        break
    
    guess_number += 1
                                         