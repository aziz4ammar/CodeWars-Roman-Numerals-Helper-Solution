class RomanNumerals:
    @staticmethod
    def to_roman(n):
        """Converts an integer to a Roman numeral."""
        roman_numerals = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        roman_numeral = ''
        for num, symbol in roman_numerals.items():
            while n >= num:
                roman_numeral += symbol
                n -= num

        return roman_numeral

    @staticmethod
    def from_roman(roman):
        """Converts a Roman numeral to an integer."""
        roman_numerals = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        num = 0
        prev_value = None
        for char in roman:
            if char not in roman_numerals:
                raise ValueError("Invalid Roman numeral")
            value = roman_numerals[char]
            if prev_value and value > prev_value:
                num += value - 2 * prev_value
            else:
                num += value
            prev_value = value

        return num
