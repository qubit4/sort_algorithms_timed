def insertionSort(array):

    for step in range(1, len(array)):

        key = array[step]
        j = step - 1

        # comparing key with each element left of it until an element smaller than it is found
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # placing key after the element just smaller than it
        array[j + 1] = key
