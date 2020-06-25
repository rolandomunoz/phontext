# Written by Rolando Muñoz (2019-2020)

class ReadFile():
  def __init__(self):
    self.wordList = list()
  
  def get_wordlist_from_text_file(self, fpath, unique = False):
    wordList = list() 
    with open(fpath, mode = 'r') as f:
      text = f.readlines()
      for line in text:
        word = line.rstrip()
        wordList.append(word)
    if unique:
      wordList = list(set(wordList))
    return wordList.copy()
  
if __name__ == '__main__':
  fpath = "/home/rolando/Documents/nomatsigenga/trabajo_de_campo_2016/wordList.txt"
#  fpath = '/home/rolando/Documents/nomatsigenga/text.txt'
  read = ReadFile()
  wordList = read.get_wordlist_from_text_file(fpath, unique = True)
  print(wordList)
