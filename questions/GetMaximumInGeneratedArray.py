class Solution:
    def get_maximum_generated(self, n: int) -> int:

        if n == 0:
            return 0

        result = [0, 1]
        maximum = 1
        for i in range(2, n+1):

            index = i // 2
            if i % 2:
                result.append(result[index] + result[index+1])
            else:
                result.append(result[index])
            maximum = max(maximum, result[-1])

        return maximum

def test():
    assert Solution().get_maximum_generated(7) == 3
