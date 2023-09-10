# Notes: 
# The idea is to use sliding window and keep growing the window with r pointer if we keep seeing unique chars using a set 
# (sets only hold unique elements). If we come upon a duplicate (meaning window already contains char at s[r]), we keep 
# removing s[l] from the window until we get rid of the duplicate, and then we and add s[r] into the window. 

# Time  Complexity: O(n)
# Space Complexity: O(1)

# My Solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l, r = 0, 1
        longest = 1
        if len(s) == 0:
            return 0
        window.add(s[l])
        while l < r and r < len(s):
            while l < r:
                if s[r] in window:
                    window.remove(s[l])
                    l += 1
                else:
                    break
            window.add(s[r])
            r += 1
            longest = max(longest, len(window))
        return longest

# NeetCode Solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            longest = max(longest, r - l + 1)
        return longest

