class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: 
        res = []
        def helper(tar, idx, cur):
            if tar == 0:
                res.append(cur[:])
                return
                
            for i in range(idx, len(candidates)):
                if candidates[i] > tar:
                    break
                cur.append(candidates[i])
                helper(tar - candidates[i], i, cur)
                cur.pop()

        candidates.sort()
        helper(target, 0, [])
        return res