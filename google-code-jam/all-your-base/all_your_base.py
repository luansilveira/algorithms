# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(input(''))

    for i in range(n):
        L = []
        counter = 0
        crypt = input('')
        C = []
        for c in crypt:

            try:
                index = C.index(c)
                if index == 0:
                    L.append(1)
                elif index == 1:
                    L.append(0)
                else:
                    L.append(index)
            except ValueError:
                C.append(c)
                if counter == 0:
                    L.append(1)
                elif counter == 1:
                    L.append(0)
                else:
                    L.append(counter)
                counter += 1

        value = 0
        base = max(counter, 2)
        for index, j in enumerate(reversed(L)):
            value += j*(base**index)

        string = 'Case #' + str(i+1) + ': ' + str(value)
        print(string)



