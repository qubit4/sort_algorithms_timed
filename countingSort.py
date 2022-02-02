# time complexity O(n)
# space complexity O(k).. k = maximum
# time-memory trade off


def countingSort(array):

    maximum = max(array)

    # creating an auxiliary array where counts of each value are stored
    counts = [0] * (maximum + 1)

    for i in array:
        counts[i] += 1

    sorted = [0] * len(array)

    # overwriting the count array to store target indices
    index = 0
    for i, count in enumerate(counts):
        counts[i] = index
        index += count

    # placing original items into correct position
    for i in array:
        sorted[counts[i]] = i
        counts[i] += 1

    return sorted
