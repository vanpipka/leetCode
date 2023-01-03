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

        result: int = 0
        pos: int = 0
        dd: dict = self.matching_characters()
        roman_list: list = [dd.get(i) for i in s]

        while pos < len(roman_list)-1:

            if roman_list[pos] < roman_list[pos+1]:
                result -= roman_list[pos]
            else:
                result += roman_list[pos]
            pos += 1

        result += roman_list[pos]

        return result
