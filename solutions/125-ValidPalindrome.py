# Notes: Use 2 pointers and scan the string after converting it to only have alphanumeric characters in it
# Space Complexity: O(n)
# Time  Complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercaseStr = s.lower()
        alphanumeric = list('abcdefghijklmnopqrstuvwxyz0123456789')
        convertedStr = ""

        for char in lowercaseStr:
            if char in alphanumeric:
                convertedStr += char

        first, last = 0, len(convertedStr) - 1
        while (first <= last):
            if convertedStr[first] != convertedStr[last]:
                return False
            first += 1
            last -= 1
        return True
