    # 1528. Shuffle String || Solution Performance - Memory: 85.02% ||  Runtime: 75.29%
    
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = {}
        letters = []
        finalans = ""
        letters = list(s)
        for i in range(0,len(indices)):
            ans[indices[i]] = letters[i]
        
        indices.sort()
        for i in indices:
            finalans = finalans + ans[i]
        return finalans


    # 1351. Count Negative Numbers in a Sorted Matrix || Solution Performance - Memory: 45.97% ||  Runtime: 88.62%

    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for arr in grid:
            for num in arr:
                if num<0:
                    count+=1
        return count