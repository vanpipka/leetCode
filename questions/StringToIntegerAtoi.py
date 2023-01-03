class Solution:
    def my_atoi(self, s: str) -> int:

        is_negative = False
        data = []
        for i in range(len(s)):
            if s[i] != ' ':
                data = [x for x in s[i:]]
                break

        if not data:
            return 0

        if data[0] == '-':
            is_negative = True
            data = data[1:]
        elif data[0] == '+':
            data = data[1:]

        result = '-' if is_negative else ''

        for i in data:
            if not i.isdigit():
                break
            result += i

        if not result or result == '-':
            return 0

        result = int(result)

        if result < -2 ** 31:
            return -2 ** 31
        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1

        return result
