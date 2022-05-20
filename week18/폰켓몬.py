def solution(nums):
    # n = len(nums) / 2
    # nums = set(nums)
    # return len(nums) if len(nums) < n else n
    
    return min(len(nums) / 2, len(set(nums)))