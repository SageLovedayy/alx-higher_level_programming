#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        lenSentence = len(sentence)
        firstChar = sentence[0]
    else:
        firstChar = None
        lenSentence = 0

    my_tuple = (lenSentence, firstChar)
    return (my_tuple)
