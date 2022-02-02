# time complexity O(n**2)

def selectionSort(array):

    size = len(array)
    for i in range(size):

        min_index = i

        for j in range(i + 1, size):

            if array[j] < array[min_index]:

                min_index = j

        # putting minimum value at the correct position
        (array[i], array[min_index]) = (array[min_index], array[i])
