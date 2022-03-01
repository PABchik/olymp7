arr = [10, 8, 6]

for i in range(3):
    arrTemp = arr.copy()

    arrTemp[0] = arr[0] % 2 + arr[1] // 2 * 3
    arrTemp[1] = arr[1] % 2 + arr[2] // 3 * 4
    arrTemp[2] = arr[2] % 3 + arr[0] // 2

    arr = arrTemp.copy()

    print(*arr)