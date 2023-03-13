# Insertion sort is a simple sorting algorithim that works similar to the the way you sort playing cards in your hands. The array is vartually split into a sorted and unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part 


def insertion_sort(unsor_list):
    for index in range (1, len(unsor_list)):
        search_index = index
        insert_value = unsor_list[index]
        while search_index>0 and unsor_list[search_index-1]> insert_value:
            unsor_list[search_index] = unsor_list[search_index-1]
            search_index -= 1
            unsor_list[search_index] = insert_value
            print(unsor_list)

        # print(unsorted_list)

arr = [50, 40, 30, 20, 10]
insertion_sort(arr)


