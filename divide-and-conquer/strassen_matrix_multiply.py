

if __name__ == '__main__':
    A = [[0,1,5],[2,3,8],[4,7,2]]
    B = [[3,4,1],[4,6,8],[2,9,3]]

    C = []
    for i in range(0,len(A)):
        aux = []
        for j in range(0,len(B[0])):
            aux.append(0)
        C.append(aux)


    print(A)
    print(B)
    print(C)

    print(len(A))
    print(len(B[0]))
    print(len(A[0]))
    print(len(B))

    for i in range(0,len(A)):
        for j in range(0,len(B[0])):
            for k in range(0, len(B)):
                C[i][j] += A[i][k]*B[k][j]



    print(A)
    print(B)
    print(C)
