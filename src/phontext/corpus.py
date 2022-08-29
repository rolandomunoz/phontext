"""
Manage word list for phonology analysis.
"""
from phontext.word import Word

class Corpus:

    def __init__(self, vowels = None, consonants = None):

        if vowels is None:
            vowels = ['a', 'e', 'i', 'o', 'u']

        if consonants is None:
            consonants = []

        self._vowels = vowels
        self._consonants = consonants

        self._data = []

    def __len__(self):
        return self._data.__len__()

    def __iter__(self):
        return self._data.__iter__()

    @property
    def word_list(self):
        return self._data

    @property
    def vowels(self):
        return self._vowels

    @property
    def consonants(self):
        return self._consonants

    def append(self, new_word):
        """

        """
        if isinstance(new_word, (str, list, tuple)):
            new_word_ = Word(new_word)
        elif isinstance(new_word, Word):
            new_word_ = new_word
        else:
            raise ValueError('Add only str, list, tuple or Word obects.')
        self._data.append(new_word_)
