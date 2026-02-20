class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicates = defaultdict(list)
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            files = parts[1:]
            for file in files:
                name, contents = file.split("(")
                content = contents[:-1]
                full_path = directory + "/" + name
                duplicates[content].append(full_path)
        result = []
        for files in duplicates.values():
            if len(files) > 1:
                result.append(files)
        return result