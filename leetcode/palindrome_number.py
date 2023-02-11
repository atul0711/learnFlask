import time


def is_palindrome(num):
    c = 10
    y=-1
    if num < 0:
        return False
    else:
        while num:
            x = num % c
            num //= 10
            y = x if y < 0 else y*10+x
            if num <= y or num == 1:
                print(y, num)
                return y == num or y//10 == num

num = 500
print(is_palindrome(num))

