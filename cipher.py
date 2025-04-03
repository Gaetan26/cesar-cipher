

import string


ALPHABET_LOWERS = list(string.ascii_lowercase)
ALPHABET_UPPERS = list(string.ascii_uppercase)


#
#
def getIndexOfChar(searchedChar: str):
    for i in range(len(ALPHABET_LOWERS)):
        if ( ALPHABET_LOWERS[i] == searchedChar):
            return i, ALPHABET_LOWERS
    
    for i in range(len(ALPHABET_UPPERS)):
        if ( ALPHABET_UPPERS[i] == searchedChar):
            return i, ALPHABET_UPPERS
			 
    raise ValueError("You can not search this char '" + searchedChar + "'");


#
#
def cipher(plainText, shiftKey):
    cipheredText = ""

    for i in range(len(plainText)):
        charPosition, charGroup = getIndexOfChar(plainText[i])
        key = charPosition + shiftKey
        
        if key >= 26:
            key = key - 26
        
        replaceVal = charGroup[key]
        cipheredText += replaceVal
        
    return cipheredText


#
#
def decipher(cypheredText, shiftKey):
    plainText = ""

    for i in range(len(cypheredText)):
        charPosition, charGroup = getIndexOfChar(cypheredText[i])
        key = charPosition - shiftKey

        replaceVal = charGroup[key]
        plainText += replaceVal

    return plainText


#
#
def cipherSentence(plainText, shifKey):
    cipheredSentence = ""
    for word in plainText.split(" "):
        cipheredSentence += cipher(word, shifKey) + " "
    return cipheredSentence


#
#
def decipherSentence(cypheredText, shifKey):
    plainText = ""
    for word in cypheredText.split(" "):
        plainText += decipher(word, shifKey) + " "
    return plainText