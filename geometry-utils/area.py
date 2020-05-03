print('AREA SOLVER \n VERSION 1.0')
while True:
    print("""Here are you choices:\n1. Square\n2. Rectangle\n3. Trapezoid\n4. Circle\n5. Hexagon\n6. Triangle\n7. Quit
Please choose 1/2/3/4/5/6/7.""")
    choice = int(input('> '))

    if choice == 1:
        side = int(input('\nLength of side: '))
        a = side ** 2
        print('The area is', str(a) + '.')

    if choice == 2:
        l = int(input('\nLength of length: '))
        w = int(input('Length of width: '))
        a = l * w
        print('The area is', str(a) + '.')

    if choice == 3:
        b1 = int(input('\nLength of Base 1: '))
        b2 = int(input('Length of Base 2: '))
        h = int(input('Height:'))
        a = ((b1 + b2) / 2) * h
        print('The area is', str(a) + '.')

    if choice == 4:
        r = int(input('Length of radius: '))
        pi = 3.1415926535897932384626433832795028841971693993751058209749445923078
        a = 2 * pi * r
