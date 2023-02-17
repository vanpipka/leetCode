class Solution:
    def interpret(self, command: str) -> str:

        return command.replace("()", "o").replace("(al)", "al")


def test():
    assert Solution().interpret("G()()()()(al)") == "Gooooal"

