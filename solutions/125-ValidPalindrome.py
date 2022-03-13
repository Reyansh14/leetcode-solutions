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


# Notes: More space efficient solution -> Use 2 pointers again, use ord to see if it's alphanumeric; while left/right pointer isn't alphanumeric, keep incrementing/decrementing as required
# Space Complexity: O(1)
# Time  Complexity: O(n)
class Solution:
    def alphaNumeric(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNumeric(s[l]):
                l += 1
            while r > l and not self.alphaNumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
