import string

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s.lower():
            return False
    return True

pangram = "The quick, brown fox jumps over the lazy dog!"

print(is_pangram(pangram))