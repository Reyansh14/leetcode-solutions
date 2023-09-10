# Notes: 
# Initialize pointers l and r at either ends of the height array and compute the area and update biggest as necessary
# Then, pick the bigger side (either height[l] or height[r]) and move the respective pointer accordingly (we want to keep the taller one)

# Time  Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        biggest = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            biggest = max(area, biggest)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return biggest
        