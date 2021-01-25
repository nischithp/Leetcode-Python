# 237. Delete Node in a Linked List
def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
            


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

# 461. Hamming Distance || Solution Performance - Memory: 97.74% (13.6MB) ||  Runtime: 89.96% (28ms)
def hammingDistance(self, x: int, y: int) -> int:
    newX = "{0:032b}".format(x)
    newY = "{0:032b}".format(y)

    count = 0

    for i in range(0,len(newX)):
        if newX[i] != newY[i]:
            count+=1
    return count

# 905. Sort Array By Parity || Solution Performance - Memory: 94.53% (14.2MB) ||  Runtime: 34.32% (120ms)
def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return (even+odd)

# 1299. Replace Elements with Greatest Element on Right Side Runtime: 4648 ms, faster than 27.96% || Memory Usage: 14.7 MB, less than 86.04%

def replaceElements(self, arr: List[int]) -> List[int]:
    for i in range(0,len(arr)-1):
        arr[i] = max(arr[i+1:len(arr)])
    arr[-1] = -1
    return arr

# 1374. Generate a String With Characters That Have Odd Counts ||Runtime: 28 ms, faster than 80.76% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.
# Memory Usage: 13.6 MB, less than 99.65%
def generateTheString(self, n: int) -> str:
    
    ans = ""
    if(n %2 == 0):
        for i in range(0,n-1):
            ans = ans + "a"
        ans = ans + "b"
    else:
        for i in range(0,n):
            ans = ans + "a"
    return ans

# 442. Find All Duplicates in an Array
# Runtime: 380 ms, faster than 81.54% of Python3 online submissions for Find All Duplicates in an Array.
# Memory Usage: 20.9 MB, less than 90.39% of Python3 online submissions for Find All Duplicates in an Array.
def findDuplicates(self, nums: List[int]) -> List[int]:
    nums.sort()
    ans = []
    if len(nums) == 0:
        return ans
    prev = nums[0]
    for i in range(1,len(nums)): 
        if prev == nums[i]:
            ans.append(nums[i])
        prev = nums[i]
    return ans