from typing import Dict

from .mispar import hechrechi, gadol

class Mispar():
    '''A Mispar is a class that converts words into numbers
    '''

    def print_bad_letter_msg(self, letter: str) -> None:
        print(f'I don\'t recognize "{letter}". Skipping it')

    def mispar(self, word: str) -> int:
        value: int = 0
        letter: str
        for letter in list(word):
            try:
                value = value + self.mapping[letter]
            except KeyError:
                self.print_bad_letter_msg(letter)
        return value

class MisparHechrechi(Mispar):

    def __init__(self):
        self.mapping: Dict[str, int] = hechrechi()

class MisparGadol(Mispar):

    def __init__(self):
        self.mapping: Dict[str, int] = gadol()

class MisparhaAkhor(Mispar):

    def __init__(self):
        self.mapping: Dict[str, int] = hechrechi()

    def mispar(self, word: str) -> int:
        i: int = 0
        value: int = 0
        letter: str
        for letter in list(word):
            try:
                value = value + 10**i * self.mapping[letter]
                i = i + 1
            except KeyError:
                self.print_bad_letter_msg(letter)
        return value
