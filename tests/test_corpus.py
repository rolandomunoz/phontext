import sys
import os
sys.path.insert(0, os.path.abspath('../src'))
from phontext import Corpus

if __name__ == '__main__':

    fin = r'C:\Users\rolan\Documents\tesis-yessica\datos_procesados\wordlist-bora.txt'
    fout = r'C:\Users\rolan\Documents\tesis-yessica\datos_procesados\análisis.txt'

    config = {
        'vowels': ['a', 'e', 'i', 'o', 'u', 'ɨ', 'ɨɨ', 'ee'],
        'consonants': ['ʔ', 'ts', 'm', 'pj', 'ɲ', 'kʷ', 'ʧ', 'kw', 'ɻ', 'ɲ']
    }

    corpus = Corpus(**config)
