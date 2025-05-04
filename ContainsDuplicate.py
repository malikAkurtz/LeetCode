from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))

def main():
    print(containsDuplicate([1,2,3]))

main()