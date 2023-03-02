from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        len_chars = len(chars)
        if len_chars < 2:
            return len_chars

        count = 1
        pointer = 0
        while True:

            if pointer >= len(chars) - 1:
                if count > 1:
                    for i in str(count):
                        pointer += 1
                        chars.insert(pointer, i)
                else:
                    pointer += 1
                break
            if chars[pointer] == chars[pointer + 1]:
                count += 1
                chars.pop(pointer)
            else:
                if count > 1:
                    for i in str(count):
                        pointer += 1
                        chars.insert(pointer, i)
                    pointer += 1
                else:
                    pointer += 1
                count = 1

        return len(chars)


def test():
    assert Solution().compress(["a", "a", "b", "b", "c", "c", "c"]) == 6
