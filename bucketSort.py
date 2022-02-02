# time complexity ... depends on underlining sorting algorithm
# space complexity... O(n + k).. k = number of buckets

from insertionSort import insertionSort


def bucketSort(array):

    bucket_size = max(array) / len(array)

    # creating list of n buckets
    buckets = []
    for i in range(len(array)):
        buckets.append([])

    # putting elements into buckets
    for i in range(len(array)):
        j = int(array[i] / bucket_size)
        if j != len(array):
            buckets[j].append(array[i])
        else:
            buckets[len(array) - 1].append(array[i])

    # sorting within buckets
    for i in range(len(array)):
        insertionSort(buckets[i])

    # linking buckets together
    sorted = []
    for i in range(len(array)):
        sorted = sorted + buckets[i]

    return sorted
