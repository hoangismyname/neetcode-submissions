class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] = hashmap.get(num)+1
        return [item for item, _ in sorted(hashmap.items(), key=lambda x: x[1], reverse=True)][:k]