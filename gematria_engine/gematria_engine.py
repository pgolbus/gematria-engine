from typing import Dict

from .mispar import hechrechi, gadol

class Mispar():
    '''A Mispar is a class that converts words into numbers
    '''

    def mispar(self, word: str) -> int:
        return sum([self.mapping[letter] for letter in list(word)])

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
        return sum([10**i * self.mapping[letter] for i, letter in enumerate(list(word))])