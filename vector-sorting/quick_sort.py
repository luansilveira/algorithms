from random import randrange


def randomized_partition(A,p,r):
    i = randrange(p, r)
    A[i], A[r-1] = A[r-1], A[i]
    return partition(A, p, r)


def partition(A, p, r):
    x = A[r-1]
    i = p - 1

    for j in range(p, r-1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r-1] = A[r-1], A[i+1]

    return i+1


def quicksort(A,p,r):
    if p < r-1:
        q = randomized_partition(A, p, r)
        quicksort(A, p, q)
        quicksort(A, q, r)


if __name__ == '__main__':
    array = [2, 8, 7, 1, 3, 5, 6, 4]

    print(array)
    quicksort(array, 0, len(array))

    print(array)

    array = [10,3,5,3,0,9,-1,20,8,5,6,2,1,0]


    print(array)
    quicksort(array, 0, len(array))

    print(array)