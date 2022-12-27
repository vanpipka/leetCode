class Solution:

    @staticmethod
    def matching_characters() -> dict:
        return {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000, }

    def roman_to_int(self, s: str) -> int:
        dd = self.matching_characters()

        result_list = [dd.get(i) for i in s]

        return result_list