from typing import List


class Solution:
    def unique_morse_representations(self, words: List[str]) -> int:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.",
                 "--.", "....", "..", ".---", "-.-", ".-..",
                 "--", "-.", "---", ".--.", "--.-", ".-.",
                 "...", "-", "..-", "...-", ".--", "-..-",
                 "-.--", "--.."]

        hash = dict(zip(alphabet, morse))

        result = {}

        for i in words:
            str = ""
            for x in i:
                str += hash[x]

            result[str] = True

        return len(result)

def test():
    assert Solution().unique_morse_representations(["gin","zen","gig","msg"]) == 2

