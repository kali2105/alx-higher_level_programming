#!/usr/bin/python3
def multiple_returns(sentence):
    mult_r = ()
    if len(sentence) == 0:
        mult_r = 0, 'None'
        return mult_r
    else:
        mult_r = len(sentence), sentence[0]
        return mult_r
