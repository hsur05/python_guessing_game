import pytest
import random
from project import select_vocab, format_underscores, check_input


def test_select_vocab():
    vocab = ["test", "obfuscate", "funny", "computers", "coding", "python", "matrix", "programming", "iphone", "macbook", "screen"]
    assert select_vocab() in vocab


def test_format_underscores():
    vocab = ["test", "obfuscate", "funny", "computers", "coding", "python", "matrix", "programming", "iphone", "macbook", "screen"]
    random_vocab = random.choice(vocab)
    underscores = "_ " * len(random_vocab) #getting the length of the chosen word
    assert len(random_vocab)*2 == len(underscores)


def test_check_input():
    with pytest.raises(TypeError):
        check_input("as")
