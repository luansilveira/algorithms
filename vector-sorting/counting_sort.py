
def counting_sort(A, B, k):

    C = [0 for x in range(k)]

    for j in range(len(A)):
        C[A[j]] += 1

    for i in range(1, k):
        C[i] += C[i-1]

    for j in reversed(range(len(A))):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1


if __name__ == '__main__':
    A = [2, 5, 3, 0, 2, 3, 0, 3]

    k = max(A) + 1
    B = [0 for x in range(len(A))]

    print(A)
    counting_sort(A, B, k)
    print(B)
