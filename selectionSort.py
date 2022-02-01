def selectionSort(array, size):

    for step in range(size):

        min_index = step

        for i in range(step + 1, size):

            if array[i] < array[min_index]:

                min_index = i

        # putting minimum value at the correct position
        (array[step], array[min_index]) = (array[min_index], array[step])
