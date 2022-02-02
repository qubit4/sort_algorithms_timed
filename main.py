from bubbleSort import bubbleSort
from insertionSort import insertionSort
from selectionSort import selectionSort
from mergeSort import mergeSort
from countingSort import countingSort
from bucketSort import bucketSort
import random
import time
from timeit import default_timer
from datetime import timedelta


print("This program explores different sort algorithms for numerical arrays.")

while True:

    try:
        # creating an array of numbers
        option = int(input(
            "\n1. I want an array of random numbers. 2. I want to input numbers manually. 3. Quit  || Press 1 or 2 or 3: "))

        if option == 1:

            count = int(
                input("Number of elements in the array? "))
            min = int(
                input("Minimum of range within which random numbers will be generated? "))
            max = int(
                input("Maximum of range within which random numbers will be generated? "))
            arr = [random.randint(min, max) for n in range(count)]

        if option == 2:

            arr = []
            count = int(input("Number of elements in the array? "))

            for i in range(count):
                elem = int(input("Enter the element: "))
                arr.append(elem)

        if option == 3:
            quit()

        # informing
        print('The present array is:', arr)
        print("\nSorting in progress..")
        time.sleep(5)

        # sorting the array with 6 sort algorithms, timing the sort and printing results
        print("\nRESULTS \n")

        sort_algorithms = [bubbleSort, insertionSort, selectionSort,
                           mergeSort, countingSort, bucketSort]

        for i in range(len(sort_algorithms)):
            start = default_timer()
            sort_algorithms[i](arr)
            end = default_timer()
            time = timedelta(seconds=end-start)

            print("{}".format(sort_algorithms[i].__name__))
            print("Sorted array: ", arr)
            print("Sorting executed in {} seconds \n".format(time))

    except ValueError:
        print("Not a valid input")
