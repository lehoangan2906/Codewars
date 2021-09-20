def to_jaden_case(string):
    return ' '.join(w[0].upper() + w[1:] for w in string.split())

quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))
