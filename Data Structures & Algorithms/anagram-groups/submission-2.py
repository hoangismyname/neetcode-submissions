from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dùng defaultdict để tự động khởi tạo list cho key mới
        hashmap = defaultdict(list)
        
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            # Ép mảng đếm thành tuple để làm key cho hashmap
            hashmap[tuple(count)].append(string)
            
        return list(hashmap.values())