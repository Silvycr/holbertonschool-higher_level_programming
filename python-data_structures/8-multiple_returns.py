#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        nueva = (len(sentence), sentence[0])
    else:
        nueva = (0, None)
    return nueva
