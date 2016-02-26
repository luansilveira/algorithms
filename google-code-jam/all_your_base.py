# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(input('n'))

    for i in range(n):
        L = []
        counter = 0
        crypt = input('input')
        C = []
        for c in crypt:

            try:
                L.append(C.index(c))
            except ValueError:
                C.append(c)
                if counter == 0:
                    L.append(1)
                elif counter == 1:
                    L.append(0)
                else:
                    L.append(counter)
                counter += 1

        print(L)
        print(C)
        print(counter)
        value = 0
        for index, i in enumerate(reversed(L)):
            value += i*(counter**index)

        print(value)



