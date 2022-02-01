def mergeSort(array):
    if len(array) > 1:

        point = len(array)//2
        array_left = array[:point]
        array_right = array[point:]

        mergeSort(array_left)
        mergeSort(array_right)

        # pointers
        i = j = k = 0

        while i < len(array_left) and j < len(array_right):
            if array_left[i] < array_right[j]:
                array[k] = array_left[i]
                i += 1
            else:
                array[k] = array_right[j]
                j += 1
            k += 1

        while i < len(array_left):
            array[k] = array_left[i]
            i += 1
            k += 1

        while j < len(array_right):
            array[k] = array_right[j]
            j += 1
            k += 1
