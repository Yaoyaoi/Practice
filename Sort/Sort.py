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
        for j in range(i):
            if array[j] > array[i]:
                array.insert(j,array[i])
                array.pop(i+1)
                break


def ShellSort(array):
    gap = int(len(array)/2)
    while gap > 1:
        for i in range(len(array)):
            for j in range(int(i/gap)):
                if array[i%gap*(j+1)] > array[i]:
                    k = i
                    while k > i%gap*(j+1):
                        temp = array[k]
                        array[k] = array[k-gap]
                        array[k-gap] = temp
                        k -= gap
        gap = int(gap/2)
    gap = 2
    for i in range(len(array)):
        for j in range(int(i/gap)):
            if array[i%gap*(j+1)] > array[i]:
                k = i
                while k > i%gap*(j+1):
                    temp = array[k]
                    array[k] = array[k-gap]
                    array[k-gap] = temp
                    k -= gap        
    InsertSort(array)

if __name__ == '__main__':
    array = [32,46,77,11,4,6,8]
#    BubbleSort(array)
#    SelectSort(array)
#    InsertSort(array)
    ShellSort(array)
    print(array)