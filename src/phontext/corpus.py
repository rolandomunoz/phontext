"""
Manage word list for phonology analysis.
"""
from phontext import Word

class Corpus:

    def __init__(self, vowels = None, consonants = None):

        if vowels is None:
            vowels = ['a', 'e', 'i', 'o', 'u']

        if consonants is None:
            consonants = []

        self._vowels = vowels
        self._consonants = consonants

        word_list = []

    @property
    def vowels(self):
        return self._vowels

    @property
    def consonants(self):
        return self._consonants

    def read_from_text_file(self, file_path, encoding = 'UTF-8'):
        config = {
            'vowels':self.vowels,
            'consonants':self.consonants
        }
        list_ = []
        with open(file_path, 'r', encoding = encoding) as text_file:
            for line in text_file.readlines():
                word_str = line.rstrip()
                word = Word(word_str, **config)
                list_.append(word)
        self.word_list = list_

    def write(self, path):
        with open(path, 'w', encoding = 'utf-8') as text_file:
            for word in self.word_list:
                text_file.write(f'{word.word_str}\t{word.cv}\n')
