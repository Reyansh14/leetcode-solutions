# Notes: 
# 
# Time  Complexity: O(nklog(k)), where n is # of strings and k is length of the string
# Space Complexity: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        index = 0
        res = []

        for s in strs:
            newS = ''.join(sorted(s.lower()))
            if newS in anagrams:
                res[anagrams[newS]].append(s)
            else:
                anagrams[newS] = index
                res.append([s])
                index += 1
            
        return res

        