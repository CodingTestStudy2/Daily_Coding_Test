#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(n * m)

3. 자료구조/알고리즘 :
-

'''
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)

        for path_info in paths:
            parts = path_info.split()

            directory = parts[0]

            for file_info in parts[1:]:
                file_name, content = file_info.split("(")
                content = content[:-1]  # 마지막 ')' 제거

                full_path = directory + "/" + file_name
                content_to_paths[content].append(full_path)

        return [
            file_paths
            for file_paths in content_to_paths.values()
            if len(file_paths) >= 2
        ]
