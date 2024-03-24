# Notes: 
# 
# Time  Complexity: O(nlog(n))
# Space Complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Method #1: Sort both strings and compare if they're equal
        s = sorted(s)
        t = sorted(t)
        return s == t

        # Method #2: Use dicts to track frequency of each char in s and t and compare the two
        # if len(s) != len(t):
        #     return False
        # sDict = {}
        # tDict = {}
        # for i in range(len(s)):
        #     sDict[s[i]] = 1 + sDict.get(s[i], 0)
        #     tDict[t[i]] = 1 + tDict.get(t[i], 0)  
        # for sKey in sDict:
        #     if (sKey not in tDict) or (sDict[key] != tDict[key]):
        #         return False
        # return True
                