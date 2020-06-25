# Written by Rolando Muñoz (2019-2020)
try:
  from .word import Word
except:
  from word import Word

class PhonParser:
  def __init__(self):
    self.complexCharList = []
  
  def set_complex_chars(self, complexCharList):
    complexCharList = sorted(complexCharList, key=len, reverse = True)
    self.complexCharList = complexCharList
    
  def to_word(self, str_word):
    """ Split segments from a word
    Parameters:
    str_word (string): a word to be segmented
    Returns:
    Word: a segment representation of a word 
    """
    lst_word = list()
    while str_word != '':
      charLen = self.__char_distance(str_word)
      phon = str_word[0:charLen]
      str_word = str_word[charLen:]
      lst_word.append(phon)
    return Word(lst_word)
    
  def __char_distance(self, str_word):
    """ Calculate how many characters should count as one segment from the start of a word 
    Parameters:
    str_word (string): a word to be segmented
    Returns:
    int: the number of characters that count as one segment at the start of a word
    """
    charLen = 1
    for char in self.complexCharList:
      if str_word.startswith(char):
        charLen = len(char)
        break
    return charLen
    
if __name__ == '__main__':
  parser = PhonParser()
  parser.set_complex_chars(['ch', 'ts', 'aa'])
  word1 = parser.to_word('chincha')
  word2 = parser.to_word('chimcha')
  print(word1)
  print(word2)
