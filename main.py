from linSearch import linearSearch
from jumpSearch import jumpSearch
from expSearch import exponentialSearch
from binSearch import binarySearch
from terSearch import ternarySearch
from fibonacci_cache import fibonacci_of
from bubbleSort import bubbleSort
from timeit import default_timer
from datetime import timedelta


print("This program explores different search algorithms for numerical arrays.")

while True:

    try:
        # creating an array of numbers
        option = int(input(
            "\n1. I want to use Fibonacci sequence. 2. I want to input numbers manually. 3. Quit  || Press 1 or 2 or 3: "))

        if option == 1:

            count = int(
                input("Number of elements in the Fibonacci sequence? "))
            arr = [fibonacci_of(n) for n in range(count)]
            print('The present array is:', arr)

        if option == 2:

            arr = []
            count = int(input("Number of elements in the array? "))

            for i in range(0, count):
                elem = int(input("Enter the element: "))
                arr.append(elem)

            print("Sorting the array now.")
            bubbleSort(arr)
            print('The present array is:', arr)

        if option == 3:
            quit()

        # selecting target number
        target = int(
            input("Enter the element you want to search for in the present array: "))

        # searching with 5 search algorithms, timing the search and printing results
        print("\nRESULTS \n")

        # storing algorithms in tuples because some algorithms take different number of parameters than others
        search_algorithms = [(linearSearch, [arr, target]), (jumpSearch, [arr, target]), (exponentialSearch, [
            arr, target]), (binarySearch, [arr, 0, len(arr), target]), (ternarySearch, [arr, 0, len(arr), target])]

        for function, args in search_algorithms:
            start = default_timer()
            result = function(*args)
            end = default_timer()
            time = timedelta(seconds=end-start)

            print("{}".format(function.__name__))
            print("Target element is present at index", result)
            print("Searching executed in {} seconds \n".format(time))

    except ValueError:
        print("Not a valid input")
