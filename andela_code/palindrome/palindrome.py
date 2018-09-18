'''
Created on Jul 19, 2018
the task was to create a program that takes a word/phrase from the user and checks if it is a palindrome
the program should also store the last 5 words the user entered

i will create a method called is_palindrome in this method the user is prompted to enter a 
word to check if it is a palindrome and return the word before promting for the next word
it initially takes 5 words but a prompt for the user to check extra words is provided
@author: Yan
'''
from builtins import str

emptylist = list()

# this is my method


def is_palindrome(num, num2):
    print('welcome!!\n\n')
    while num < num2:
        print('enter a word to check if its a palindrome')
        statement = str(input('--->'))
        statement.casefold()
        revstatement = reversed(statement)
        if list(revstatement) == list(statement):
            print('it is indeed a palindrome')
        else:
            print('this word is not a palindrome, better luck next round!')
        emptylist.append(statement)
        print(statement)
        num = num + 1


# this is where the program begins!
palindrome = is_palindrome(0, 5)
print('\nwould you like to enter another word?')
answer = str(input('enter "Y" or "N"').capitalize())
if answer == 'Y':
    print('\nhow many more words do you want to check?')
    additional = int(input('enter an integer value!'))
    palindromeExtra = is_palindrome(0, additional)
elif answer == 'N':
    print('\nOkay, Thank You')

print('\nthis is the record of the last five words: ')

for word in emptylist[-5:]:
    print(word)
