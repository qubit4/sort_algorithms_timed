# time complexity O(n log n)
# space complexity O(n)

def mergeSort(array):
    # base condition
    if len(array) > 1:

        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        # recursively sorting subarrays
        mergeSort(left)
        mergeSort(right)

        # pointers
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
                k += 1
            else:
                array[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
