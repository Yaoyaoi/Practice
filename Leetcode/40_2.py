from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]: 
        res = []
        def helper(tar, idx, cur):
            if tar == 0:
                res.append(cur[:])
                return
                
            for i in range(idx, len(candidates)):
                if candidates[i] > tar:
                    break
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                helper(tar - candidates[i], i + 1, cur)
                cur.pop()

        candidates.sort()
        helper(target, 0, [])
        return res

if __name__ == "__main__":
    print(Solution().combinationSum2([2,5,2,1,2],5))