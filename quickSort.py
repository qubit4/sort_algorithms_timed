# time complexity O(n**2)
# space complexity O(n)

def partition(array, start, end):

    pivot = array[end]
    boundary = start - 1

    for i in range(start, end):
        if array[i] <= pivot:

            boundary += 1
            (array[boundary], array[i]) = (array[i], array[boundary])

    (array[boundary + 1], array[end]) = (array[end], array[boundary + 1])

    return boundary


def quickSort(array, start, end):
    # base condition
    if start < end:

        boundary = partition(array, start, end)

        # recursive calls
        quickSort(array, start, boundary - 1)
        quickSort(array, boundary + 1, end)
