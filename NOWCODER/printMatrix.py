class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix1(self, matrix):
        # write code here
        if not matrix:
            return []

        nRow = len(matrix)              # number of rows
        if nRow == 1:
            return matrix[0]
        nCol = len(matrix[0])           # number of column

        matrixList = []
        up = 0
        down = nRow -1
        left = 0
        right = nCol  -1
        i = up
        j = left

        while True:
            for j in range(left,right+1):
                matrixList.append(matrix[i][j])
            up += 1
            if up > down:
                break

            for i in range(up,down+1):
                matrixList.append(matrix[i][j])
            right -= 1
            if left > right:
                break

            for j in range(right,left-1,-1):
                matrixList.append(matrix[i][j]) 
            down -= 1
            if up > down:
                break

            for i in range(down,up-1,-1):
                matrixList.append(matrix[i][j])
            left += 1
            if left > right:
                break
        return matrixList
    
    def printMatrix2(self, matrix):
       matrixList = []
        while True:
            matrixList.extend(matrix[0])
            if len(matrix)>1:
                matrix = matrix[1::]
            else :
                break
            matrix = [[row[i] for row in matrix] for i in range(len(matrix[0])-1 , -1 , -1)]
        return matrix
        


if __name__ == '__main__':
    a = [[1]]
    b = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
    c = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

    sol =Solution()
    print(sol.printMatrix(a))
    print(sol.printMatrix(b))
    print(sol.printMatrix(c))