def create_phone_number(n):
    phonenum = "("
    for i in range(len(n)):
        if i < 3:
            phonenum += str(n[i])
            if i == 2:
                phonenum += ') '
        elif i <= 13:
            phonenum += str(n[i])
            if i == 5:
             phonenum += '-'
    return phonenum


def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])