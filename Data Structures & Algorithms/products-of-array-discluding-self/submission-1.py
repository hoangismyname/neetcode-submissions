class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        pre, post = 1, 1
        for num in nums:
            arr.append(pre)
            pre *= num
        for i in range(len(nums)-1, -1, -1):
            arr[i] = post*arr[i]
            post *= nums[i]
        return arr