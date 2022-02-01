from bubbleSort import bubbleSort
from insertionSort import insertionSort
from selectionSort import selectionSort
from mergeSort import mergeSort
from quickSort import quickSort
import random
import time
from timeit import default_timer
from datetime import timedelta


print("This program explores different sort algorithms for numerical arrays.")

while True:

    try:
        # creating an array of numbers
        array_option = int(input(
            "\n1. I want to manually create an array of numbers. 2. I want an array of random numbers. 3. Quit  || Press 1 or 2 or 3: "))

        if array_option == 1:

            arr = []
            count = int(input("Number of elements in the array? "))

            for i in range(0, count):
                elem = int(input("Enter the element: "))
                arr.append(elem)

            print('The present array is:', arr)

        if array_option == 2:

            count = int(
                input("Number of elements in the array? "))
            min = int(
                input("Minimum of range within which random numbers will be generated? "))
            max = int(
                input("Maximum of range within which random numbers will be generated? "))
            arr = [random.randint(min, max) for n in range(count)]
            print('The present array is:', arr)
            print("\nSorting in progress..")
            time.sleep(5)

        if array_option == 3:
            quit()

        # sorting the array with 4 sort algorithms, timing the sort and printing results
        print("\nRESULTS \n")

        arr1 = arr
        start1 = default_timer()
        bubbleSort(arr1)
        end1 = default_timer()
        time_bubble = timedelta(seconds=end1-start1)

        print("Bubble Sort")
        print("Sorted array: ", arr1)
        print("Sorting executed in {} seconds \n".format(time_bubble))

        arr2 = arr
        start2 = default_timer()
        insertionSort(arr2)
        end2 = default_timer()
        time_insertion = timedelta(seconds=end2-start2)

        print("Insertion Sort")
        print("Sorted array: ", arr2)
        print("Sorting executed in {} seconds \n".format(time_insertion))

        arr3 = arr
        start3 = default_timer()
        selectionSort(arr3, len(arr3))
        end3 = default_timer()
        time_selection = timedelta(seconds=end3-start3)

        print("Selection Sort")
        print("Sorted array: ", arr3)
        print("Sorting executed in {} seconds \n".format(time_selection))

        arr4 = arr
        start4 = default_timer()
        mergeSort(arr4)
        end4 = default_timer()
        time_merge = timedelta(seconds=end4-start4)

        print("Merge Sort")
        print("Sorted array: ", arr4)
        print("Sorting executed in {} seconds \n".format(time_merge))

        arr5 = arr
        start5 = default_timer()
        quickSort(arr5, 0, len(arr5) - 1)
        end5 = default_timer()
        time_quick = timedelta(seconds=end5-start5)

        print("Quick Sort")
        print("Sorted array: ", arr5)
        print("Sorting executed in {} seconds \n".format(time_quick))

    except ValueError:
        print("Not a valid input")
