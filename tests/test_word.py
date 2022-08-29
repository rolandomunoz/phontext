import sys
import os
sys.path.insert(0, os.path.abspath('../src'))
from phontext import Word

if __name__ == '__main__':

    config = {
        'vowels': ['a', 'e', 'i', 'o', 'u'],
        'consonants': ['ch', 'ts', 'rr']
    }

    word1 = Word('chincha', **config)
    word2 = Word('chinchaa', **config)
    word3 = Word(['p', 'e', 'rr', 'o'], **config)


    a = word3.get_invalid_segments()
    print(a)

    print(word1)
    print(word2)
    print(word3)
    word3.reverse()
    print(word3)

    # Check minimal pairs
    # This must be True
    word4 = Word('paso', **config)
    word5 = Word('peso', **config)
    word6 = Word('kasa', **config)

    # This must be False
    word7 = Word('tasa', **config)
    word8 = Word('tasl', **config)
    result = word7.is_minimal_pair(word8)
    print(result)
