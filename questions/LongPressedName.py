class Solution:
    def is_long_pressed_name(self, name: str, typed: str) -> bool:

        if name[0] != typed[0] or len(name) > len(typed):
            return False

        i = 0

        while i < len(name):

            if i >= len(typed):
                return False

            if name[i] != typed[i]:
                if typed[i] != typed[i - 1]:
                    return False
                else:
                    typed = typed[:i] + typed[i + 1:]
            else:
                i += 1

        if len(typed) > len(name):
            suff = set(typed[len(name) - 1:])
            if len(suff) == 1:
                typed = typed[:len(name) - 1] + typed[-1]

        return name == typed


def test():
    assert Solution().is_long_pressed_name("alex", "aaleex") is True
    assert Solution().is_long_pressed_name("vtkgn", "vttkgnn") is True
