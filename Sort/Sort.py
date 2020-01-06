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

def Merge(array,brray):
    crray = []
    alen = len(array)
    blen = len(brray)
    i = j = 0
    while i < alen and j < blen:
        if array[i] < brray[j]:
            crray.append(array[i])
            i += 1
        else:
            crray.append(brray[j])
            j += 1
    if i < alen:
        crray.extend(array[i:])
    if j < blen:
        crray.extend(brray[j:])
    return crray


def MergeSort(array):
    l = len(array)
    if l > 2:
        array = Merge(MergeSort(array[:int(l/2)]),MergeSort(array[int(l/2):]))
    if l == 2:
        if array[0] > array[1]:
            temp = array[0]
            array[0] = array[1]
            array[1] = temp
    return array


def QuickSort(array):
    if len(array) < 2:
        return array
    i = 0
    j = len(array)-1
    key = array[i]
    while i < j:
        while array[j] > key and i < j:
            j -= 1
        if i < j:
            array[i] = array[j]
        while array[i] < key and i < j:
            i += 1
        if i < j:
            array[j] = array[i]
    array[i] = key
    brray = QuickSort(array[:i])
    brray.append(key)
    brray.extend(QuickSort(array[i+1:]))
    return brray


def BuildMaxHeap(array, last):
    if last < 1:
        return
    i = int((last-1)/2)
    while i > -1:
        ShiftDown(array, i, last)
        i -= 1


def ShiftDown(array, node, last):
    if 2*node+1 > last:
        return
    maxNode = node
    if array[node] < array[2*node+1]:
        maxNode = 2*node+1
    if 2*node+2 <= last:
        if array[maxNode] < array[2*node+2]:
            maxNode = 2*node+2
    if node == maxNode:
        return 
    temp = array[maxNode]
    array[maxNode] = array[node]
    array[node] = temp
    ShiftDown(array, maxNode, last)


def HeapSort(array):
    for i in range(len(array)-1):
        BuildMaxHeap(array,len(array)-1-i)
        temp = array[len(array)-1-i]
        array[len(array)-1-i] = array[0]
        array[0] = temp


def RadixSort(array):
    

if __name__ == '__main__':
    array = [2,32,25,46,5,77,11,4,58]
#    BubbleSort(array)
#    SelectSort(array)
#    InsertSort(array)
#    ShellSort(array)
#    array = MergeSort(array)
#    array = QuickSort(array)
#    HeapSort(array)

    print(array)