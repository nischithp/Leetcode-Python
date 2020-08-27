
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

# 1347. Minimum Number of Steps to Make Two Strings Anagram || Solution Performance - Memory: 39.50% ||  Runtime: 5.05%

def minSteps(self, s: str, t: str) -> int:
    if (s == "") or (t == ""):
        return 0
    count = 0
    for i in range(0,len(s)):
        if s[i] in t:
            newT = t.replace(s[i],'',1)
            t = newT 
        else:
            count+=1
    return len(t)