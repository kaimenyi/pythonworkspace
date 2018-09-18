'''
Created on Jul 19, 2018

@author: Yan
'''


def main():
    words = str(input("Input Sentence:")).split()
    wordlist = list(words)
    for word in words:
        print(word[1:] + word[0] + "ay", end=" ")
    print()


main()

'''

# PygLatin Converter Code
pyg = 'ay'

original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first == ('a' or 'e' or 'i' or 'o' or 'u'):
        new_word = word + pyg
        print new_word
    else:
        new_word = word[1:] + first + pyg
        print new_word
else:
    print 'empty'



original = raw_input('Enter a word:')
word = original.lower()
first = word[0]

if len(original) > 0 and original.isalpha():
    if first == "a" or "e" or "i" or "o" or "u":
        print "vowel"
    else:
        print "consonant"
else:
    print "empty"
'''
