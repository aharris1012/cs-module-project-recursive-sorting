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


    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
