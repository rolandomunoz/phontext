# Written by Rolando Muñoz (2019-2022)

class PhonParser:

    def __init__(self):
        self.complexCharList = []

    def set_complex_chars(self, complexCharList):
        complexCharList = sorted(complexCharList, key=len, reverse = True)
        self.complexCharList = complexCharList

    def to_word(self, word):
        """ Split segments from a word
        Parameters:
        word (string): a word to be segmented
        Returns:
        Word: a segment representation of a word 
        """
        lst_word = list()
        while word != '':
            charLen = self.__char_distance(word)
            phon = word[0:charLen]
            word = word[charLen:]
            lst_word.append(phon)
        return Word(lst_word)

    def __char_distance(self, word):
        """
        Calculate how many characters should count as one segment from the start of a word 

        Parameters
        ----------
        word : str
            A word to be segmented

        Returns
        --------
        int
            The number of characters that count as one segment at the start of a word
        """
        charLen = 1
        for char in self.complexCharList:
            if word.startswith(char):
                charLen = len(char)
                break
        return charLen

class Word:
    """
    Represent a word.
    """

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
        """
        Check if the :class:`Word` starts with a segment.

        Returns
        -------
        bool
           `True` if the word starts with a segment. Otherwise, it is False.
        """
        return self[0] == segment

    def endswith(self, segment):
        """
        Check if the :class:`Word` ends with a segment.

        Returns
        -------
        bool
            `True` if the word ends with a segment. Otherwise, it is False.
        """
        maxIndex = len(self) - 1
        return self[maxIndex] == segment

    def copy(self):
        return Word(self.word.copy())

    def reverse(self):
        """
        Reverse the word segment.
        """
        self.word = [element for element in self.__reversed__()]

    def is_minimaldiff(self, other):
        is_minimal_pair(self, other)

    def is_minimal_pair(self, other):
        """
        Check if the word and `other` are minimal pairs.

        When two words are different in one segment, this difference
        must be between segments of the same type. For example, 
        `cana` and `canu` are minimal pairs, while `cana` and `cant`
        are not.

        Parameters
        ----------
        other : :class:`Word`
            A segment representation of a word to be compared.

        Returns
        -------
        bool
            `True` if it is minimal pair. Otherwise, return `False`.
        """
        if not len(self) == len(other):
            return False

        if self == other:
            return False

        diff_counter = 0
        for i in range(0, len(self)):
            if self[i] != other[i]:
                diff_counter+=1

            if diff_counter > 1:
                return False
        return True

    def to_cv(self, nucleus_list = None):
        """
        Convert to CV.

        Parameters
        ----------
        nucleus_list : list
            A list of syllabic nuclei.

        Returns
        -------
        str
            A cv representation of a word
        """
        if nucleus_list is None:
            nucleus_list = ['a', 'e', 'i', 'o', 'u']

        cv_pattern = []
        for phon in self:
            if phon in nucleus_list:
                cv_pattern.append('V')
            else:
                cv_pattern.append('C')
        cv_pattern= ''.join(cv_pattern)
        return cv_pattern

    def get_invalid_segments(self, valid_segment_list = []):
        """
        Get a list of invalid segments in a word

        Parameters
        ----------
        valid_segment_list : list
            A list of valid segment strings

        Returns
        -------
        list
            Only invalid segments
        """
        return [phon for phon in self if not phon in valid_segment_list]

if __name__ == '__main__':
    parser = PhonParser()
    parser.set_complex_chars(['ch', 'ts', 'aa'])
    word1 = parser.to_word('chincha')
    word2 = parser.to_word('chinchaa')
    print(word1)
