def  to_camel_case(text):
    list = [x for x in text]
    if len(list) != 0:
        for i in range(len(list)):
            if list[i] in ('-','_'):
                list[i+1] = list[i+1].upper()
        list = ''.join([i for i in list if i not in ('-', '_')])
        return str(list)
    else:
        return ""

def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s

print(to_camel_case("The_stealth_warrior"))
