from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Khởi tạo một dictionary với giá trị mặc định là list trống
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sắp xếp các ký tự của chuỗi s và join lại làm key
            sorted_s = "".join(sorted(s))
            # Thêm từ gốc vào danh sách tương ứng với key
            anagram_map[sorted_s].append(s)
            
        # Trả về tất cả các nhóm anagram (values của dictionary)
        return list(anagram_map.values())