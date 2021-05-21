from typing import Dict, Tuple, List
from collections import defaultdict

from .errors import *

__all__ = [
    'NumeralSystem'
]


class NumeralSystem:
    """
    Represents a numeral system like Roman Numerals generalized.
    """

    def __init__(self, characters: Dict[int, str]) -> None:
        """
        Create a numeral system like Roman Numerals.
        :param characters: a dictionary of value: character pairs
        :raises InvalidNumeralSystemError: if there are negative symbols
        """
        if any(map(lambda v: v <= 0, characters.keys())):
            raise InvalidNumeralSystemError('Negative symbols are not valid')

        self._symbols = self.enumerateSymbols(characters)
        self._characters = characters

    def __str__(self):
        return f'<{", ".join(map(lambda p: p[1], self._symbols))}>'

    def __repr__(self):
        return f'NumeralSystem({self._characters})'

    @staticmethod
    def enumerateSymbols(characters: Dict[int, str]) -> Tuple[Tuple[int, str]]:
        """
        Generates a set of symbols, which can be multi-character in the proper form for computation.
        :param characters: the characters to be used for enumeration
        :return: the set of symbols ordered by minimum value first.
        """
        symbols = defaultdict(list)  # value : symbol

        for value, char in characters.items():
            symbols[value].append(char)

        values = list(sorted(characters.keys()))

        for i, value in enumerate(values):
            for otherValue in values[:i]:
                symbols[value - otherValue].append(characters[otherValue] + characters[value])

        finalSymbols: List[Tuple[int, str]] = []

        for value, possible in symbols.items():
            finalSymbols.append((value, possible[0]))

        return tuple(sorted(finalSymbols, key=lambda p: p[0]))

    def formNumeral(self, value: int) -> str:
        """
        Form the valid numeral given a specific value. For example for Roman Numerals, formNumeral(7) -> 'VII'
        :param value: the value to create a numeral out of
        :raises ValueError: the given value can not be formed into a numeral in the given system, usually caused by a
                            missing 1 symbol
        :raises InvalidNumeralSystemError: the given system is invalid, usually caused by having a negative symbol
        :return: the numeral
        """
        maxIndex = len(self._symbols) - 1
        numeral = ''

        while value > 0 and maxIndex >= 0:
            symbol = self._symbols[maxIndex]
            if 1 <= symbol[0] <= value:
                value -= symbol[0]
                numeral += symbol[1]
                continue
            maxIndex -= 1

        if value > 0:
            raise ValueError(f'{value} can not be formed into a valid numeral under the system {self}.')

        if value < 0:  # Should never happen however it may happen so just to be safe
            raise InvalidNumeralSystemError(f'{self} is not a valid system')

        return numeral
