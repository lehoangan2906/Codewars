""" Create a RomanNumerals class that can convert a roman numeral to and from an integer value. 
    It should follow the API demonstrated in the example below. Multiple roman numeral values 
    will be tested for each helper method. 
    
    Modern Roman numerals are written by expressing each digit separately starting with the left 
    most digit and skipping any digit with a zero. In roman numerals 1990 is redered: 1000 = M, 
    900 = CM, 90 = XC; resulting in MCMXC. 2008 is written as 2000 = MM, 8 = VIII; or MMVIII. 
    1666 uses each Roman symbol in descending order: MDCLXVI
    
    input range: 1 <= n <= 4000
    
    in this kata 4 shoud be represented as IV, not as IIII.     
    
    Examples:
        RomanNumerals.to_roman(1000) # should return 'M'
        RomanNumerals.from_roman('M') # should return 1000
"""

class RomanNumerals:
    
    def to_roman(num):
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D",
            "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L",
            "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V",
            "VI", "VII", "VIII", "IX"]
    
        # Converting to roman
        thousands = m[num // 1000]
        hundereds = c[(num % 1000) // 100]
        tens = x[(num % 100) // 10]
        ones = i[num % 10]
    
        ans = (thousands + hundereds +
            tens + ones)
    
        return ans

    def from_roman(s):
        translations = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000
                }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number

print('Decimal to Roman: ' + RomanNumerals.to_roman(1990))
print('Roman to Decimal: ' + str(RomanNumerals.from_roman('M')))