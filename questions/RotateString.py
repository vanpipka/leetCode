class Solution:
    def rotate_string(self, s: str, goal: str) -> bool:
        for i in range(len(goal)):
            if s == goal[i:] + goal[:i]:
                return True
        return False


def test():
    assert Solution().rotate_string("abcde", "cdeab") is True
