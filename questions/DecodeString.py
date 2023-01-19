from typing import List


class Solution:

    def __init__(self):
        self.pointer = 0

    def decode_string(self, s: str) -> str:

        self.pointer = 0

        def get_str():

            res_str = ""
            multiplier = ""

            while self.pointer < len(s):
                self.pointer += 1
                if s[self.pointer-1].isdigit():
                    multiplier += s[self.pointer-1]
                    continue
                if s[self.pointer-1] == "[":
                    tmp = get_str()

                    if multiplier == "":
                        res_str += tmp
                    else:
                        res_str += int(multiplier)*tmp
                        multiplier = ""
                    continue

                elif s[self.pointer-1] == "]":
                    return res_str

                res_str += s[self.pointer-1]

            return res_str

        result = get_str()

        return result


def test():

    assert Solution().decode_string("3[x]") == "xxx"
    assert Solution().decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert Solution().decode_string("3[a2[c]]") == "accaccacc"

