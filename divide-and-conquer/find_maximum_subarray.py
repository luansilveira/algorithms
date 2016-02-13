

def brute_force(array = []):
    max_profit = 0;

    for i in range(0,len(array)):
        for j in range(i, len(array)):
            if array[j] - array[i] > max_profit:
                max_profit = array[j] - array[i]
                start = i
                end = j


    return start, end, max_profit


def find_max_crossing_subarray(array, low, mid, high):
    left_sum = float('-inf')
    sum = 0;

    for i in range(mid-1, low-1, -1):
        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = float('-inf')
    sum = 0

    for i in range(mid, high, 1):
        sum += array[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i

    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(arr, low, high):
    if low == high - 1:
        return low, high, arr[low]
    else:
        mid = (low+high)//2
        left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(arr, mid, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)

        if left_sum > right_sum and left_sum > cross_sum:
            return left_low, left_high, left_sum
        elif right_sum > left_sum and right_sum > cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


if __name__ == '__main__':
    array = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]

    start, end, max_profit = brute_force(array)

    print('Array = ', array)
    print('Max profit is equal to', max_profit)
    print('Buy: Day', start, ' Sell: Day', end)

    array_mod = []
    for i in range(1,len(array)):
        array_mod.append(array[i] - array[i-1])

    start, end, max_profit = find_maximum_subarray(array_mod, 0, len(array_mod))

    print('Array_mod = ', array_mod)
    print('Max profit is equal to', max_profit)
    print('Buy: Day', start, ' Sell: Day', end)

    array = [10, 11, 7, 10, 6]

    start, end, max_profit = brute_force(array)

    print('Array = ', array)
    print('Max profit is equal to', max_profit)
    print('Buy: Day', start, ' Sell: Day', end)

    array_mod = []
    for i in range(1, len(array)):
        array_mod.append(array[i] - array[i-1])
    start, end, max_profit = find_maximum_subarray(array_mod, 0, len(array_mod))

    print('Array_mod = ', array_mod)
    print('Max profit is equal to', max_profit)
    print('Buy: Day', start, ' Sell: Day', end)