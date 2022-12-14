"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string,
they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""



# MY VERSION
def rot13(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newWord = []

    for i in message:
        if i.lower() not in alphabet:
            newWord.append(i)
        elif message[message.index(i)].isupper():
            newWord.append(alphabet[(alphabet.find(i.lower()) + 13) % len(alphabet)].upper())
        else:
            newWord.append(alphabet[(alphabet.find(i) + 13) % len(alphabet)])

    return ''.join(newWord[newWord.index(c)] for c in newWord)
    
 
# SOMEONE'S CODE (BEST WAY)
"""
import string
from codecs import encode as _dont_use_this_
from string import maketrans, lowercase, uppercase

def rot13(message):
    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
    return message.translate(lower).translate(upper)
"""
