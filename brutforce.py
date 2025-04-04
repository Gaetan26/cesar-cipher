

from cipher import decipherSentence


sentence = input("sentence: ")

for n in range(1, 27):
    print(
        "for shifkey {} => {}" \
            .format(n, decipherSentence(sentence, n))
    )
