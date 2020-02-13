class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not path or len(path) > rows * cols:
            return False
        tempMatrix = []
        for i in range(rows):
            rl = []
            for j in range(cols):
                rl.append(matrix[j+i*cols])
            tempMatrix.append(rl)
        matrix = tempMatrix
        
        lableMatrix = []
        for i in range(rows):
            l = [0] * cols
            lableMatrix.append(l)

        def isPath(row, col, index):
            if index == len(path) - 1:
                return True
            lableMatrix[row][col] = 1
            targetChar = path[index+1]
            iP = False
            
            def direction(di):
                i = -1
                j = -1
                if di == 0:
                    if row > 0:
                        i = row - 1
                        j = col
                if di == 1:
                    if row < rows - 1:
                        i = row + 1
                        j = col
                if di == 2:
                    if col > 0:
                        i = row
                        j = col - 1
                if di == 3:
                    if col < cols - 1:
                        i = row
                        j = col + 1
                return i, j

            for d in range(4):
                i, j = direction(d)
                if not iP and i != -1 and j != -1 and not lableMatrix[i][j] and matrix[i][j] == targetChar:
                    iP = isPath(i, j, index+1)

            lableMatrix[row][col] = 0
            return iP 
        isP = False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == path[0]:
                    isP = isPath(r, c, 0)
                    if isP:
                        return True
        return False

if __name__ == "__main__":
    matrix = ["A","B","C","E","H","J","I","G","S","F","C","S","L","O","P","Q","A","D","E","E","M","N","O","E","A","D","I","D","E","J","F","M","V","C","E","I","F","G","G","S"]
    sol = Solution()
    print(sol.hasPath(matrix,5,8,'SGGFIECVAASABCEHJIGQEM'))

    