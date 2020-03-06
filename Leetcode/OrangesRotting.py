class Solution:
    def orangesRotting(self, grid):
        if not grid[0]:
            return -1
        if len(grid) == 1:
            if len(grid[0])==1:
                if grid[0][0] == 1:
                    return -1
                else:
                    return 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j])
        count = 0
        while queue:
            i = len(queue)
            count += 1
            while i:
                item = queue.pop(0)
                i -= 1
                if item[0] > 0: #up
                    if grid[item[0]-1][item[1]] == 1:
                        grid[item[0]-1][item[1]] = 2
                        queue.append([item[0]-1,item[1]])
                if item[0] < len(grid)-1: #down
                    if grid[item[0]+1][item[1]] == 1:
                        grid[item[0]+1][item[1]] = 2
                        queue.append([item[0]+1,item[1]])
                if item[1] > 0: #left
                    if grid[item[0]][item[1]-1] == 1:
                        grid[item[0]][item[1]-1] = 2
                        queue.append([item[0],item[1]-1])
                if item[1] < len(grid[0])-1: #right
                    if grid[item[0]][item[1]+1] == 1:
                        grid[item[0]][item[1]+1] = 2
                        queue.append([item[0],item[1]+1])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return count-1


if __name__ == "__main__":
    sol = Solution()
    print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))