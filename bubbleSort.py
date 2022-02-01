def bubbleSort(array):

    # loop to access each element
    for i in range(len(array)):

        swapped = False

        # loop to compare each element
        for j in range(0, len(array) - i - 1):

            if array[j] > array[j+1]:
                # swapping left and right element if left is greater than right
                (array[j], array[j+1]) = (array[j+1], array[j])

                swapped = True

        # if the array is already sorted, the function ends
        if not swapped:
            break
