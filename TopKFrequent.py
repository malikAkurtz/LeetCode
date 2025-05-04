'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

'''
from typing import List
from collections import defaultdict

def topKFrequent(nums: List[int], k: int) -> List[int]:
    my_dict = defaultdict(int)
    output = []

    for num in nums:
        my_dict[num] += 1

    sorted_items = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

    for i in range(k):
        output.append(sorted_items[i][0])

    return output

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))