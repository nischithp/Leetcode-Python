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