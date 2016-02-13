from enum import Enum


def bubble_sort(array = []):
    for i in range(len(array)):
        for j in range(len(array)-1,i,-1):
            if array[j] < array[j-1]:
                aux = array[j]
                array[j] = array[j-1]
                array[j-1] = aux

    return array


if __name__ == '__main__':
    array = [10,3,5,3,0,9,-1,20,8,5,6,2,1,0]

    print(array)
    print(bubble_sort(array))