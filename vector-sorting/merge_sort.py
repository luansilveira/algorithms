from enum import Enum


class Order(Enum):
    asc = 0
    dsc = 1


def merge(array, p, q, r, order):
    a = array[p:q]
    b = array[q:r]
    if order == Order.asc:
        a.append(float('inf'))
        b.append(float('inf'))
    else:
        a.append(float('-inf'))
        b.append(float('-inf'))

    i = j = 0
    while i < len(a)-1 or j < len(b)-1:
        if order == Order.asc:
            if a[i] > b[j]:
                array[p+i+j] = b[j]
                j += 1
            else:
                array[p+i+j] = a[i]
                i += 1
        elif order == Order.dsc:
            if a[i] < b[j]:
                array[p+i+j] = b[j]
                j += 1
            else:
                array[p+i+j] = a[i]
                i += 1
        else:
            print('Wrong order', order)


def merge_sort(array, p,r, order = Order(0)):
    if p < r-1:
        q = (p+r)//2
        merge_sort(array,p,q,order)
        merge_sort(array,q,r,order)
        merge(array,p,q,r,order)

    return array

if __name__ == '__main__':
    array = [10,3,5,3,0,9,-1,20,8,5,6,2,1,0]

    print('Array = ', array)
    print('Array Asc = ', merge_sort(array,0,len(array)))
    print('Array Dsc = ', merge_sort(array,0,len(array),Order.dsc))
