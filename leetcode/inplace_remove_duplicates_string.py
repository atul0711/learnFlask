import string

s = list('Atuhuuulji Srivasggtava isamak'.lower())


def remove_duplicates(c, st):
    while len(st) > c:
        for i in range(c + 1, len(st)):
            if st[c] == st[i] and st[i] != ' ':
                del st[i]
                break
        else:
            c += 1


c = 0
remove_duplicates(c, s)
print(''.join(s))
