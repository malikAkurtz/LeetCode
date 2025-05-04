"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109"""

def longestConsecutive(nums: list[int]) -> int:
    k = 0
    tempk = 0
    num_set = set(nums)

    # for every number
    for number in num_set:
        # if it is the start of a sequence
        if (number - 1) not in num_set:
            # incremenet counter
            tempk = 1
            temp_num = number + 1
            while temp_num in num_set:
                tempk += 1
                temp_num += 1
            if tempk > k:
                k = tempk
        else:
            continue
    
    return k
        
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))