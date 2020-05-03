'''
Determine if N is Prime
27 December, 2017
'''


def is_prime(n):
    prime = True

    if n == 2 or n == 3:
        prime = True
    elif n % 2 == 0:
        prime = False
    else:
        for x in range(5, n // 2, 2):
            if n % x == 0:
                prime = False
                break

    return prime


n = input('(! to quit)  > ')
while n != '!':
    print('Yes' if is_prime(int(n)) else 'No')
    n = input('(! to quit)  > ')
