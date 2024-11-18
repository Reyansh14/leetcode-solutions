from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ### METHOD 1:
        # Time Complexity:
        # Building Frequency Dictionary: 𝑂(𝑁)
        # Sorting: 𝑂(𝑀 log 𝑀)
        # Extracting Top k Elements: 𝑂(𝑘)
        # Overall: 𝑂(𝑁 + 𝑀 log 𝑀)
        # Where:
        # 𝑁 = total elements in nums
        # 𝑀 = unique elements in nums
        # Space Complexity:
        # Frequency Dictionary: 𝑂(𝑀)
        # Sorted List: 𝑂(𝑀)
        # Result List: 𝑂(𝑘)
        # Overall: 𝑂(𝑀 + 𝑘)

        # # Create a dictionary with the frequency of each element in nums
        # freq = Counter(nums)
        
        # # Sort the dictionary by frequency in descending order
        # sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # # Return the first k elements of the sorted dictionary
        # return [x[0] for x in sorted_freq[:k]]

        ### METHOD 2: Track occurrences in "count" Dict and use Bucket Sort so each element of
        #  "freq" is an array containing nums that occur that index number of times (ex. if 
        #  numbers 1 and 2 occur 3 times in nums array, freq[3] = [1,2]). 
        # Time Complexity
        # Building Frequency Dictionary: 𝑂(𝑁) — Iterating through nums to populate the frequency dictionary.
        # Populating Buckets: 𝑂(𝑀) — Iterating through each of the 𝑀 unique elements.
        # Collecting Top k Elements: 𝑂(𝑁) — Traversing the entire freq array of length 𝑁 + 1 in the worst case.
        # Overall: 𝑂(𝑁), since operations depend linearly on 𝑁 in the worst case.
        # Space Complexity
        # Frequency Dictionary: 𝑂(𝑀) — Storing frequencies for each unique element.
        # Buckets: 𝑂(𝑁) — Using 𝑁 + 1 buckets, with total size at most 𝑁 in the worst case.
        # Overall: 𝑂(𝑁).

        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        # for n, c in count.items():
        #     freq[c].append(n)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res

        ### METHOD 3: min-heap
        # Time Complexity:
        # Building the frequency dictionary takes 𝑂(𝑁).
        # Extracting the top k elements using a heap takes 𝑂(𝑀 log 𝑘).
        # Overall Time Complexity: 𝑂(𝑁 + 𝑀 log 𝑘).
        # Space Complexity:
        # Frequency dictionary: 𝑂(𝑀).
        # Min-Heap: 𝑂(𝑘).
        # Overall Space Complexity: 𝑂(𝑀 + 𝑘).

        freqMap = Counter(nums)
        minHeap = []
        for num, freq in freqMap.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [num for freq, num in minHeap]
