class Solution:
    def get_hint(self, secret: str, guess: str) -> str:

        s_b, s_c = {}, {}
        bull, cow = 0, 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                s_b[secret[i]] = s_b.get(secret[i], 0) + 1
                s_c[guess[i]] = s_c.get(guess[i], 0) + 1

        for i, val in s_b.items():
            cow += min(s_c.get(i, 0), val)

        return f"{bull}A{cow}B"


def test():
    assert Solution().get_hint("1807", "7810") == "1A3B"
    assert Solution().get_hint("1123", "0111") == "1A1B"
