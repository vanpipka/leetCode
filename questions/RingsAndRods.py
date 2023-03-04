class Solution:
    def count_points(self, rings: str) -> int:

        _map = {}
        result = 0
        for i in range(0, len(rings), 2):
            _m = _map.get(rings[i + 1], set())
            _m.add(rings[i])

            _map[rings[i + 1]] = _m

        for key, value in _map.items():
            if len(value) == 3:
                result += 1

        return result


def test():
    assert Solution().count_points("B0B6G0R6R0R6G9") == 1



