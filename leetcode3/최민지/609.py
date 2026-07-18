from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)

        for path in paths:
            parts = path.split()

            directory = parts[0]

            for file in parts[1:]:
                filename, content = file.split("(")
                content = content[:-1]         

                full_path = directory + "/" + filename
                content_map[content].append(full_path)

        return [files for files in content_map.values() if len(files) > 1]
        