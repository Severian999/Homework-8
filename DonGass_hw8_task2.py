#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:33:47 2017

@author: Career
"""

alphabet = "abcdefghijklmnopqrstuvwxyz "
key = "sxzaijhbwpekfcqrgdtluv noym"

def codedText(text, keyMap):
    return ''.join([keyMap[c] for c in text])
#    answer = ''
#    for c in text:
#        answer += keyMap[c]
#    return answer

def substitutionEncrypt(plainText, key):
#    keyMap = {}
#    for (index,c) in enumerate(alphabet):
#        keyMap[c] = key[index]
    return codedText(plainText, keyMap) ### the 3 commented lines should be 
#coded into the keyMap argument for codedText using dictionary comprehension

def substitutionDecrypt(cipherText, key):
    inverseKeyMap = {}
    for (index,c) in enumerate(alphabet):
        inverseKeyMap[key[index]] = c
    return codedText(cipherText, inverseKeyMap)

def valid_key(key):
    return True if (len(key) == 27) and set(key) == set(alphabet) else False

plainText = 'today is tuesday'
cipherText = substitutionEncrypt(plainText, key)
decodedText = substitutionDecrypt(cipherText, key)

print(valid_key(key))
print(plainText)
print(cipherText)
print(decodedText)