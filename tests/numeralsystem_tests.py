import unittest
import numeralsystems


class NumeralSystemTest(unittest.TestCase):
    def test_symbolEnumeration(self):
        symbols = numeralsystems.NumeralSystem.enumerateSymbols({1: 'I', 5: 'V', 10: 'X', 16: 'W'})
        self.assertEqual(len(symbols), 9)
        self.assertEqual(symbols[0], (1, 'I'))
        self.assertEqual(symbols[1], (4, 'IV'))
        self.assertEqual(symbols[2], (5, 'V'))
        self.assertEqual(symbols[3], (6, 'XW'))
        self.assertEqual(symbols[4], (9, 'IX'))
        self.assertEqual(symbols[5], (10, 'X'))
        self.assertEqual(symbols[6], (11, 'VW'))
        self.assertEqual(symbols[7], (15, 'IW'))
        self.assertEqual(symbols[8], (16, 'W'))

    def test_strImplementation(self):
        system = numeralsystems.NumeralSystem({1: 'I', 5: 'V', 10: 'X'})

        self.assertEqual(str(system), '<I, IV, V, IX, X>')

    def test_reprImplementation(self):
        system = numeralsystems.NumeralSystem({1: 'I', 5: 'V', 10: 'X'})

        self.assertEqual(repr(system), "NumeralSystem({1: 'I', 5: 'V', 10: 'X'})")

    def test_simpleNumeralFormation(self):
        system = numeralsystems.NumeralSystem({1: 'I', 5: 'V', 10: 'X'})

        cases = [
            (1, 'I'),
            (2, 'II'),
            (3, 'III'),
            (4, 'IV'),
            (5, 'V'),
            (6, 'VI'),
            (7, 'VII'),
            (8, 'VIII'),
            (9, 'IX'),
            (10, 'X')
        ]

        for v, correct in cases:
            self.assertEqual(system.formNumeral(v), correct)

    def test_romanNumerals(self):
        cases = [
            (23, 'XXIII'),
            (108, 'CVIII'),
            (594, 'DXCIV'),
            (288, 'CCLXXXVIII'),
            (1644, 'MDCXLIV'),
            (2025, 'MMXXV'),
        ]

        for v, correct in cases:
            self.assertEqual(numeralsystems.ROMAN_NUMERAL_SYSTEM.formNumeral(v), correct)

    def test_unreachableNumber(self):
        with self.assertRaises(ValueError):
            system = numeralsystems.NumeralSystem({2: 'J', 5: 'V', 10: 'X'})

            system.formNumeral(1)

    def test_invalidSystem(self):
        with self.assertRaises(numeralsystems.InvalidNumeralSystemError):
            system = numeralsystems.NumeralSystem({-1: 'J', 5: 'V', 10: 'X'})


if __name__ == '__main__':
    unittest.main()
