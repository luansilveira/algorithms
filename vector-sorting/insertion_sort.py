from enum import Enum


class Order(Enum):
    asc = 0
    dsc = 1


def insertion_sort(array=[], order=Order(0)):
    if order == Order.asc:
        for j in range(1, len(array)):
            key = array[j]
            i = j-1
            while i >= 0 and array[i] > key:
                array[i+1] = array[i]
                i -= 1
            array[i+1] = key

    elif order == Order.dsc:
        for j in range(len(array)-2, -1, -1):
            key = array[j]
            i = j+1
            while i < len(array) and array[i] > key:
                array[i-1] = array[i]
                i += 1
            array[i-1] = key
    else:
        print('Wrong order', order)

    return array


if __name__ == '__main__':
    array = [10,3,5,3,0,9,-1,20,8,5,6,2,1,0]

    print('Array = ', array)
    print('Array Asc = ', insertion_sort(array))
    print('Array Dsc = ', insertion_sort(array,Order.dsc))
