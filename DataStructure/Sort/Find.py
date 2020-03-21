def BinarySearch(target, array): # recursive
    low = 0 
    high = len(array)-1
    mid = int((low + high)/2)
    if target < array[low] or target > array[high]:
        return False
    if target == array[mid]:
        return True
    if low == high:
        return False
    if target > array[mid]:
        brray = array[mid+1:]
        if(BinarySearch(target,brray)):
            return True
        else:
            return False
    if target < array[mid]:
        brray = array[:mid]
        if(BinarySearch(target,brray)):
            return True
        else:
            return False



if __name__ == '__main__':
    array = [2,4,6,7,15,27,32]
    print(BinarySearch(32,array))   