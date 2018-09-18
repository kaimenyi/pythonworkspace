'''
Created on Jul 10, 2018

@author: Yan
'''


def is_isogram(word):
    if word != '':
        if not isinstance(word, str):
            raise TypeError("This should be a string")
        if not word:
            isogram = False
        else:
            isogram = len(word) == len(set(word.lower()))
        return(word, isogram)
    return (word, False)
