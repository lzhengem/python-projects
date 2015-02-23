""" In this module allow sentences to be palindromes.  
We ignore spaces, punctuation marks, etc. Also, not case-sensitive.

We define three functions:  stripper, normalize, and is_palindrome.

>>> stripper("Madam, I'm Adam!")
'MadamImAdam'

>>> normalize("Madam, I'm Adam!")
'MADAMIMADAM'
>>> normalize("Catch22")
'CATCH'

>>> is_palindrome('Bob')
True
>>> is_palindrome("race car")
True
>>> is_palindrome("A man, a plan, a canal, Panama!")
True

"""


import string

def stripper(s):
    """Removes spaces and non-letters.

    """
    # REPLACE THE pass BELOW WITH YOUR OWN LINES OF CODE
    # TO TEST IT DO ./testrunner at the unix command line
    stripped_s = "".join(char for char in s if char not in string.punctuation and not char.isspace())
    return stripped_s

def normalize(s):
    """Returns the string s as a string consisting only of upper-case letters.

    """
    # REPLACE THE pass BELOW WITH YOUR OWN LINES OF CODE
    # TO TEST IT DO ./testrunner at the unix command line
    s = s.upper()
    normalized_s =''.join([char for char in s if char in string.ascii_uppercase])
    return normalized_s

def is_palindrome(sentence):
    """Returns True only if the sentence spells the same backwards,
    when we ignore spaces, upper or lower case, and punctuation marks.
    """
    
    # REPLACE THE pass BELOW WITH YOUR OWN LINES OF CODE
    # TO TEST IT DO ./testrunner at the unix command line
    sentence = stripper(normalize(sentence))
    return sentence == sentence[::-1]
