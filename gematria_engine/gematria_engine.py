from typing import Dict

from .mispar import hechrechi, gadol


class Mispar:
    """A Mispar is a class that converts words into numbers"""

    def __init__(self, strip: bool = False):
        self.mapping: Dict[str, int] = {}
        self.strip: bool = strip

    def get_bad_letter_msg(self, letter: str, word: str):
        return f'I don\'t recognize "{letter}" in {word}.'

    def mispar(self, word: str) -> int:
        value: int = 0
        letter: str
        for letter in list(word):
            try:
                value = value + self.mapping[letter]
            except KeyError:
                if self.strip:
                    continue
                raise ValueError(self.get_bad_letter_msg(letter, word))
        return value


class MisparHechrechi(Mispar):
    def __init__(self, strip: bool = False):
        super().__init__(strip=strip)
        self.mapping = hechrechi()


class MisparGadol(Mispar):
    def __init__(self, strip: bool = False):
        super().__init__(strip=strip)
        self.mapping = gadol()


class MisparhaAkhor(Mispar):
    def __init__(self, strip: bool = False):
        super().__init__(strip=strip)
        self.mapping = hechrechi()

    def mispar(self, word: str) -> int:
        i: int = 0
        value: int = 0
        letter: str
        for letter in list(word):
            try:
                value = value + 10**i * self.mapping[letter]
                i = i + 1
            except KeyError:
                if self.strip:
                    continue
                raise ValueError(self.get_bad_letter_msg(letter, word))
        return value
