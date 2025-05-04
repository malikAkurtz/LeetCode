'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

'''

def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix_products = [0] * n
    suffix_products = [0] * n
    prefix_products[0] = nums[0]
    suffix_products[n-1] = nums[n-1]

    for i in range(1, n):
        prefix_products[i] = nums[i] * prefix_products[i-1]
    for i in range(n - 2, -1, -1):
        suffix_products[i] = nums[i] * suffix_products[i+1]

    output = [0] * n

    output[0] = suffix_products[1]
    output[n-1] = prefix_products[n-2]

    for i in range(1, n-1):
        output[i] = prefix_products[i-1] * suffix_products[i+1]
    
    return output

    

print(productExceptSelf([1,2,3,4]))