def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [letter for letter in string_ if letter not in vowels]
    result = ''.join(result)
    return result

print(disemvowel("This website is for losers LOL!"))