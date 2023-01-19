class Solution:
    def backspace_compare(self, s: str, t: str) -> bool:

        def del_symbol(string):

            data = [i for i in string]

            while True:

                if "#" not in data:
                    print(data)
                    return data
                else:
                    i_s = data.index("#")
                    data.pop(i_s)
                    if i_s != 0:
                        data.pop(i_s-1)

            print(data)

            return data

        return del_symbol(s) == del_symbol(t)


def test():

    assert Solution().backspace_compare("y#fo##f", "y#f#o##f") is True
    assert Solution().backspace_compare("ab#c", "ad#c") is True
    assert Solution().backspace_compare("ab##", "c#d#") is True
    assert Solution().backspace_compare("a#c", "b") is False
