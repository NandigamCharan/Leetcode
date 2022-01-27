def sumArray(arr):
    if len(arr) == 0:
        return 0 
    return arr[0] + sumArray(arr[1:])


def sum_arr(arr):
    def recurse(A, acc):
        # acc means accumulator, we are imitating for loop here
        if len(A) == 0:
            return acc
        else:
            return recurse(A[1:], acc + A[0])
    return recurse(arr, 0)


A = [1 ,2 ,3 ,4, 5]
print(sumArray(A))