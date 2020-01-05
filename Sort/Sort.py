def BubbleSort(array):
    if not array:
        return 
    for i in range(1,len(array)):
        for j in range(len(array)-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]


def SelectSort(array):
    if not array:
        return 
    for i in range(0,len(array)-1):
        min = i
        for j in range(i+1,len(array)):
            if array[j]<array[min]:
                min = j
        temp = array[min]
        array[min] = array[i]
        array[i] = temp
    if array[len(array)-2] > array[len(array)-1]:
        temp = array[len(array)-2]
        array[len(array)-2] = array[len(array)-1]
        array[len(array)-1] = temp


def InsertSort(array):
    for i in range(len(array)):
        j = i
        while j > 0:
            if array[j-1] > array[j]:
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp
                j -= 1
            else:
                break


def ShellSort(array):
    gap = int(len(array)/2)
    while gap > 0:
        for i in range(len(array)):
            j = i - gap
            while  j >= 0:
                if array[j] > array[j+gap]:
                    temp = array[j]
                    array[j] = array[j+gap]
                    array[j+gap] = temp
                    j -= gap
                else:
                    break
        gap = int(gap/2)


if __name__ == '__main__':
    array = [2,32,25,46,5,77,11,4,58]
#    BubbleSort(array)
#    SelectSort(array)
#    InsertSort(array)
    ShellSort(array)
    print(array)