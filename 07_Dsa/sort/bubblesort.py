# def bubble_sort(unordered_list):
#     iteration_number = len(unordered_list) - 1
#     for i in range (iteration_number, 0, -1 ):
#         for j in range(i):
#             temp = unordered_list[j]
#             unordered_list[j] = unordered_list[j+1]
#             unordered_list[j+1] = temp



def bubbleSort(arr):
    print(f"Before sorting {arr}")
    for i in range (len(arr)):
        for j in range (0, len(arr) - i -1):
            if arr[j] > arr [j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j+1] = temp
            print(arr)    
arr = [40, 35, 30, 25, 20]
bubbleSort(arr)
