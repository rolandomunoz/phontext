# PhonText
A python package for phonology analysis from text files

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install phontext.

```bash
pip install phontext
```

## Usage

Use this package to parse words
```python
import phontext

lst_charGroups = ['ts', 'ch', 'rr']
parser = phontext.Parser()
parser.set_complex_chars(lst_charGroups)

# Parse words into segments
word = parser.to_word('hitsacha')
print(word)
>> h i ts a ch a

# Find minimal pairs

word1 = parser.to_word('perro')
word2 = parser.to_word('pero')

word1.is_minimaldiff(word2)
>> True

# and much more...

```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.txt)
