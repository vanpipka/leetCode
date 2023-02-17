from typing import List


class Solution:
    def decode_message(self, key: str, message: str) -> str:

        hash = {}
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
        position = 0
        for i in key.replace(" ", ""):
            if hash.get(i, None) is None:
                hash[i] = alphabet[position]
                position += 1

        result = ""
        for i in message:
            if i == " ":
                result += " "
            else:
                result += hash[i]

        print(result)

        return result

def test():
    assert Solution().decode_message("the quick brown fox jumps over the lazy dog",
                                     "vkbs bs t suepuv") == "this is a secret"
    assert Solution().decode_message("eljuxhpwnyrdgtqkviszcfmabo",
                                     "zwx hnfx lqantp mnoeius ycgk vcnjrdb") == "the five boxing wizards jump quickly"


