def Find(target, array):
    if not array:
        return False
    if not array[0]:
        return False
    i = 0
    while target > array[i][len(array[0])-1]:
        i += 1
        if i == len(array):
            return False
    for j in range(i,len(array)):
        if BinarySearch(target,array[j]):
            return True
    return False
def BinarySearch(target, array):
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

#    d1len = len(array)
#    d2len = len(array[0])
#
#    lenmin = min(d1len, d2len)
#    lenmax = max(d1len, d2len)
#
#    low  = 0
#    high = lenmin
#    mid = (low+high)/2
#
#    if (target == array[low][low] or target == array[high][high]):
#        return True
#    if (target < array[low][low]):
#        return False
#    if (target > array[high][high]):
#        if high == lenmax:
#            return False
#            


if __name__ == "__main__":
    a = [1,2,8,9]
    b = [2,4,9,12]
    c = [4,7,10,13]
    d = [6,8,11,15]
    array = [a,b,c]
    target = 16
    print(Find(target,[[]]))

