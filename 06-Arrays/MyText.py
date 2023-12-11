def wordCount(x):
    y = x.count(" ")
    return y+1
def ordnenzu(x):
    array = x.split(" ")
    for i in range(0,len(array)-1):
        for j in range(0, len(array)-i-1):
               if len(array[j]) < len(array[j + 1]):
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
    return array
def alfabetic(x):
    array = x.split(" ")
    sorted_arr = sorted(array)
    return sorted_arr