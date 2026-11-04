class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            x = target - nums[i]
            if x in hashmap:
                return [hashmap.get(x), i]
            hashmap[nums[i]] = i
        return None