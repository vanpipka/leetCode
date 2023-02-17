from typing import List


class Solution:
    def defang_ip_addr(self, address: str) -> str:

        return address.replace(".", "[.]", 3)


def test():
    assert Solution().defang_ip_addr("1.1.1.1") == "1[.]1[.]1[.]1"
