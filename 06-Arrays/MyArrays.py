def a(arr):
    temp = arr
    temp.remove(max(temp))
    return max(temp)


def b(arr):
    x = min(arr)
    y = max(arr)
    return y-x


def c(array):
    for i in range(len(array)):
            for j in range(0, len(array)-i-1):
               if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
            return array[len(array)//2]

def d(array):
    x = []
    x.append(min(array))
    x.append(max(array))
    return x

def e(array):
    for i in array:
        print(i,end="-")
