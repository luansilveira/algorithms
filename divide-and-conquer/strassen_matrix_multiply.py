
def multiply(A,B):
    C = []
    for i in range(0,len(A)):
        C.append([]);
        for j in range(0,len(B[0])):
            C[i].append(0)
            for k in range(0, len(B)):
                C[i][j] += A[i][k]*B[k][j]

    return C



def strassen_algorithm2x2(A, B):
    C = A[:]

    S0 = B[0][1] - B[1][1]
    S1 = A[0][0] + A[0][1]
    S2 = A[1][0] + A[1][1]
    S3 = B[1][0] - B[0][0]
    S4 = A[0][0] + A[1][1]
    S5 = B[0][0] + B[1][1]
    S6 = A[0][1] - A[1][1]
    S7 = B[1][0] + B[1][1]
    S8 = A[0][0] - A[1][0]
    S9 = B[0][0] + B[0][1]

    P0 = A[0][0] * S0
    P1 = S1 * B[1][1]
    P2 = S2 * B[0][0]
    P3 = A[1][1] * S3
    P4 = S4 * S5
    P5 = S6 * S7
    P6 = S8 * S9

    C[0][0] = P4 + P3 - P1 + P5
    C[0][1] = P0 + P1
    C[1][0] = P2 + P3
    C[1][1] = P4 + P0 - P2 - P6

    return C

if __name__ == '__main__':
    A = [[7, 8], [2, 3]]
    B = [[3, 4], [4, 6]]

    C = multiply(A, B)

    print(C)

    C = strassen_algorithm2x2(A, B)

    print(C)
