"""We read words from a file on hills that has almost half a million words.
We accept any line in that dictionary as a word.

>>> is_word('radar')
True
>>> is_word('Ada')
True
>>> is_word('Turing')
True
>>> is_word('hand-fed')
True

Our is_word is not case-sensitive.

>>> is_word('mESsY')
True

We create a set consisting of all the words, but written in lower-case.

For efficiency we keep go by word size. So, wordset(n) has all words of length n.

Remember that they are changed to lower-case.

>>> 'Turing' in wordset(6)    
False

>>> 'turing' in wordset(6)
True


Read the file tests/test_words.txt to see what we want from our is_word and wordset.

"""

HILLSDICTFILE = '/usr/share/dict/words'


def is_word(word_in_question):
    """Is the word in the hills dictionary?
        Allows any characters used in the hills dictionary words.
        Not case-sensitive.
    """
    # REPLACE THE pass BELOW WITH YOUR OWN CODE.
    dictionary = []
    with open(HILLSDICTFILE, 'r') as document:
        for word in document:
            dictionary.append(word.strip().lower())
    return word_in_question.lower() in dictionary


def wordset(size):
    """Returns a set, not a list, with all the words of that size from the hills dictionary.
       All words are changed to lower-case before added to that set.
    """

    # REPLACE THE pass BELOW WITH YOUR OWN CODE.

    words = set()
    with open(HILLSDICTFILE, 'r') as document:
        for line in document:
            if len(line.strip()) == size:
                words.add(line.strip().lower())
    return(words)

