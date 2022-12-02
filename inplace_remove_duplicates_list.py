

x = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7]
c = 0


def remove_duplicates(c, l):
    while len(l) > c+1:
        if l[c] == l[c + 1]:
            del l[c + 1]
        else:
            c += 1
    return c, l


remove_duplicates(c, x)
print(x)
