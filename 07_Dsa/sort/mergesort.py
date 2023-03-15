def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        start = arr [:mid]
        end = arr [mid:]

        mergeSort(start)
        mergeSort(end)

        i = j = k =0


        while i < len(start):
            arr[k] = start[i]
            i += 1
            k += 1

        while j < len(end):
            arr[k] = end[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [6, 5, 4, 8, 1, 9] 
    mergeSort(arr)
    for i in range (len(arr)):
        print(arr[i], end="")               