


def bubblesort(array):
        for i in range(len(array)):
            for j in range(0, len(array)-i-1):
               if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        return array


arr = [64, 34, 25, 12, 22, 11, 90]
print(bubblesort(arr))