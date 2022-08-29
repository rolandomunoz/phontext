import sys
import unittest
import os
sys.path.insert(0, os.path.abspath('../src'))
from phontext import Word

config = {
    'vowels': ['a', 'e', 'i', 'o', 'u'],
    'consonants': ['ch', 'ts', 'rr']
}

class TestWordMethods(unittest.TestCase):

    def test_attributes(self):
        word = Word('chincha', **config)
        self.assertEqual(len(word), 5)
        self.assertEqual(word.cv, "CVCCV")
        self.assertEqual(word.word_str, "ch i n ch a")
        self.assertEqual(word.word, ["ch", "i","n", "ch", "a"])

    def test_operators(self):
        word1 = Word('paso', **config)
        word2 = Word(['p','a', 's','o'], **config)
        word3 = Word('peso', **config)

        self.assertTrue(word1==word2)
        self.assertFalse(word1==word3)

    def test_minimal_pairs(self):
        word1 = Word('tasa', **config)
        word2 = Word('kasa', **config)
        word3 = Word('tasl', **config)

        self.assertTrue(word1.is_minimal_pair(word2))
        self.assertFalse(word1.is_minimal_pair(word3))

if __name__ == '__main__':
    unittest.main()

