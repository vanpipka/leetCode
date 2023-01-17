class Solution:
    def fib(self, n: int) -> int:

        if n < 2:
            return n

        result = self.fib(n-2) + self.fib(n-1)

        return result

def test():
    assert Solution().fib(5) == 5
    assert Solution().fib(2) == 1
    assert Solution().fib(3) == 2
    assert Solution().fib(4) == 3
