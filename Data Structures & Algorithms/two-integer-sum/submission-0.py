class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            cur = nums[i]
            x = target - cur
            if x in hashmap:
                return [hashmap.get(x), i]
            hashmap[cur] = i
        return None