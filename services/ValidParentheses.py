class Solution:
    def is_valid(self, s: str) -> bool:

        search_dict = {")": "(", "}": "{", "]": "["}

        result = []

        for i in s:
            if i in search_dict.keys():
                if result and result[-1] == search_dict.get(i):
                    result.pop()
                else:
                    return False
            else:
                result.append(i)

        return len(result) == 0
