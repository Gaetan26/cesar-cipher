

from cipher import cipherSentence, decipherSentence

key = 3
base = "Universite Loyola du Congo"

base_ = cipherSentence(plainText=base, shifKey=key)

print(base, "=>", base_)
print(base_, "=>", decipherSentence(cypheredText=base_, shifKey=key))