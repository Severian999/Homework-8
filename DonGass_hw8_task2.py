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

def substitutionEncrypt(plainText, key):
    return codedText(plainText, {c: key[index] for index, c in enumerate(alphabet)})

def substitutionDecrypt(cipherText, key):
    return codedText(cipherText, {key[index]: c for index, c in enumerate(alphabet)})

def valid_key(key):
    return True if (len(key) == 27) and set(key) == set(alphabet) else False

plainText = 'today is tuesday'
cipherText = substitutionEncrypt(plainText, key)
decodedText = substitutionDecrypt(cipherText, key)

print(valid_key(key))
print(plainText)
print(cipherText)
print(decodedText)