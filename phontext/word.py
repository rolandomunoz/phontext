# Written by Rolando Muñoz (2019-2020)

class Word():
  def __init__(self, lst_word):
    self.word = lst_word
  
  def __str__(self):
    return ' '.join(self.word)
  
  def __len__(self):
    return self.word.__len__()
  
  def __iter__(self):
    return self.word.__iter__()

  def __reversed__(self):
    return self.word.__reversed__()
    
  def __getitem__(self, index):
    return self.word.__getitem__(index)
  
  def __contains__(self, char):
    return self.word.__contains__(char)
    
  def __eq__(self, other):
    return self.word.__eq__(other.word)

  def __ne__(self, other):
    return self.word.__ne__(other.word)
  
  def __setitem__(self, index, value):
    return self.word.__setitem__(index, value)
    
  def startswith(self, segment):
    return self[0] == segment
  
  def endswith(self, segment):
    maxIndex = len(self) - 1
    return self[maxIndex] == segment
    
  def copy(self):
    return Word(self.word.copy())
  
  def reverse(self):
    self.word = [element for element in self.__reversed__()]
    
  def is_minimaldiff(self, other):
    """ Check if there is a minimal pair with other word object
    It does not take in care if the difference is between a consonant and a vowel (eg. cana vs cant).
    Parameters:
    other (Word): A segment representation of a word
    Returns:
    boolean: True or False
    """
    if not len(self) == len(other):
      return False

    if self == other:
      return False

    diffCounter = 0
    for i in range(0, len(self)):
      if self[i] != other[i]:
        diffCounter+=1
        
      if diffCounter > 1:
        return False
    return True
  
  def to_cv(self, nucleusList = ['a', 'e', 'i', 'o', 'u']):
    """ Convert to CV
    Parameters:
    nucleusList (list): a list of syllabic nuclei
    Returns:
    str: a cv representation of a word 
    """    
    cvPattern = list()
    for phon in self:
      if phon in nucleusList:
        cvPattern.append('V')
      else:
        cvPattern.append('C')
    cvPattern= ''.join(cvPattern)
    return cvPattern

  def get_invalid_segments(self, validSegmentList = []):
    """ Get a list of invalid segments in a word
    Parameters:
    validSegmentList (list): a list of valid segment strings
    Returns:
    list: only invalid segments 
    """   
    return [phon for phon in self if not phon in validSegmentList]

if __name__ == '__main__':
  lst_word = ['p', 'e','rr','o']
  
  word1 = Word(lst_word)
  cv1 = word1.to_cv()
  
  word2 = word1.copy() 
  word2.reverse()
  cv2 = word2.to_cv()
  
  print(word1,'\t', cv1)
  print(word2, '\t', cv2)
