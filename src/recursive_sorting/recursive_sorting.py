# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    next_smallest_left_index = 0
    next_smallest_right_index = 0
    
    for i in range (elements):
        if next_smallest_left_index >= len(arrA):
            return merged_arr.extend(arrB[next_smallest_right_index:])
        
        elif next_smallest_right_index >= len (arrB):
            return merged_arr.extend(arrA[next_smallest_left_index:])

        elif arrA[next_smallest_left_index] < arrB[next_smallest_right_index]:
            merged_arr[i] = arrA[next_smallest_left_index]
            next_smallest_left_index += 1

        else:
            merged_arr[i] =arrB[next_smallest_right_index]
            next_smallest_right_index +=1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        return merge(merge_sort(left), merge_sort(right))


    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1

    if arr[mid] <= arr[start2]:
        return arr

    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1

        else:
            value = arr[start2]
            index = start2

            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            start += 1
            mid += 1
            start2 += 1


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if len(arr) <= 1:
        return arr

    if l < r:

        mid = (l + r) // 2

        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)

        sorted_arr = merge_in_place(arr, l, mid, r)

        return sorted_arr


    


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):
#     # Your code here

#     return arr
