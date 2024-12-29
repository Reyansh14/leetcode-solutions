from typing import List

'''
Notes: 
The amount of water trapped above a bar depends on the shorter of the tallest 
bars to its left and right. To calculate water above each bar, you need to know:
- The tallest bar to its left (leftMax).
- The tallest bar to its right (rightMax).
Water trapped = min(leftMax, rightMax) − height[i].

Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                # Water trapped above the bar at left is determined by l_max
                l_max = max(height[l], l_max)
                water += l_max - height[l]
                l += 1
            else:
                # Water trapped above the bar at right is determined by r_max
                r_max = max(height[r], r_max)
                water += r_max - height[r]
                r -= 1
        return water
