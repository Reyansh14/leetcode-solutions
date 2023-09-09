# Notes: 
# There are different cases to consider. We need to figure out if we're in the left sorted or right sorted sections after pivoting.
# If nums[l] <= nums[mid], we know we're in the left sorted section. Else, it's the right sorted section.
#
# In the left sorted section, if the target > nums[mid] we know we want to search in the right part of the rotated array. 
# Also in the left sorted section, if the target < nums[l], it means we want to once again we want to search in the right 
# part of the rotated array so we increase the left pointer in both cases.
#
# Similar logic applies to the right but ajust accordingly.

# Space Complexity: O(1)
# Time  Complexity: O(log(n))
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted section
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted section
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1