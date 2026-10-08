#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #brute force method - time complexity O(n^2), space complexity O(1) [ becasue we aren't using extra space, and 2 loops are constant for any input]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] ==  target - nums[i]:
                    return [i, j]
        return []

        # hash map method - two pass hash table method - time complexity O(n), space complexity O(n)
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):      
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []

        # hash map method - one pass hash table method - time complexity O(n), space complexity O(n)
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
        return []
    
print(Solution().twoSum([2, 7, 11, 15], 9))
