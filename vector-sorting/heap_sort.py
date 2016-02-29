class MyHeap:
    def __init__(self, array):
        self.array = array[:]
        self.size = len(array)

        self.build()

    def build(self):
        for i in reversed(range(self.size//2)):
            self.heapfy(i)

    def heapfy(self, i):
        l = 2*i + 1
        r = 2*i + 2

        if l < self.size and self.array[l] > self.array[i]:
            largest = l
        else:
            largest = i

        if r < self.size and self.array[r] > self.array[largest]:
            largest = r

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.heapfy(largest)

    def sort(self):
        for i in reversed(range(1, len(self.array))):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.size -= 1
            self.heapfy(0)


if __name__ == '__main__':

    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

    print("The original array is:", A)
    h = MyHeap(A)

    print("The max heap array is :", h.array)

    h.sort()

    print("The sorted array is :", h.array)