def BubbleSort(array):
    for i in range(1,len(array)):
        for j in range(len(array)-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array
            



if __name__ == '__main__':
    array = [2,4,6,37,32,17,5]
    BubbleSort(array)
    print(array)