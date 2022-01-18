from tabnanny import check


def checknumber(arr, x):
    if len(arr) == 0:
        return False
    if arr[0] == x:
        return True
    return checknumber(arr[1:], x)
    pass


arr  = [21, 22, 456, 12, 61, 21, 33, 16, 99, 96]
print(checknumber(arr, 1))
print(checknumber(arr, 3))
print(checknumber(arr, 6))
print(checknumber(arr, 25))