def get_divisors(n, myList, m, myList2):
    for i in range(2, n + 1):
        if n % i == 0:
            myList.append(i)

    for i in range(2, m + 1):
        if m % i == 0:
            myList2.append(i)


def get_common_list(aList, bList, cList):
    for i in aList:
        if i in bList:
            cList.append(i)

    if cList == []:
        return True

    if cList != []:
        return False


print("""FRACTION REDUCER
VERSION 1.1\n""")

while True:
    print('PRESS 1 TO CONTINUE, PRESS 2 TO EXIT.')
    con = int(input('> '))

    if con == 1:
        num = int(input('Enter the numerator: '))
        den = int(input('Enter the denominator: '))
        numList, denList, comList = [], [], []

        get_divisors(num, numList, den, denList)
        if get_common_list(numList, denList, comList):
            print('This expression can\'t be simplified.')

        if not get_common_list(numList, denList, comList):
            print('This expression can be simplified.')
            a = comList[-1]
            num = num / a
            den = den / a
            print('Numerator:', str(num) + '\n' +
                  'Denominator:', str(den) + '\n')
    if con == 2:
        input('Press <enter> to exit.')
        quit()
