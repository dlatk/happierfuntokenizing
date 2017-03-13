# Happier Fun Tokenizer

This code implements a basic, Twitter-aware tokenizer. Originally developed by [Christopher Potts](http://web.stanford.edu/~cgpotts/) 
([Happy Fun Tokenizer](http://sentiment.christopherpotts.net/code-data/happyfuntokenizing.py)) and updated by [H. Andrew Schwartz](http://www3.cs.stonybrook.edu/~has/). Shared with Christopher's permission.

### Usage

```python
from happierfuntokenizing.happierfuntokenizing import Tokenizer

tokenizer = Tokenizer()

message = """OMG!!!! :) I looooooove this tokenizer lololol"""
tokens = tokenizer.tokenize(message)
print(tokens)
['omg', '!', '!', '!', '!', ':)', 'i', 'looooooove', 'this', 'tokenizer', 'lololol']

message = """OMG!!!! :) I looooooove this tokenizer LoLoLoLoLooOOOOL"""
tokenizer = Tokenizer(preserve_case=True)
tokens = tokenizer.tokenize(message)
print(tokens)
['OMG', '!', '!', '!', '!', ':)', 'I', 'looooooove', 'this', 'tokenizer', 'LoLoLoLoLooOOOOL']
```

### Installation

This is available through `pip`

```sh
pip install happierfuntokenizing
```

If you do not have sudo privileges you can use the `--user` flag

```sh
pip install --user happierfuntokenizing
```

## Requirements

This uses Python 2.7. Package dependencies include `re` and `htmlentitydefs`.

## License

Licensed under a [GNU General Public License v3 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html)

## Background

Adapted by the [World Well-Being Project](http://www.wwbp.org) based out of the University of Pennsylvania
and Stony Brook University. Originally developed by [Christopher Potts](http://web.stanford.edu/~cgpotts/). 
