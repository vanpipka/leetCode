class Solution:

    def check_inclusion(self, s1: str, s2: str) -> bool:

        len_s1 = len(s1)

        if len_s1 > len(s2):
            return False

        symbol_list = {}
        pointer = True

        for i in s1:
            if i in symbol_list.keys():
                continue
            symbol_list[i] = s1.count(i)

        for i in range(len(s2)-len_s1+1):

            curr_str = s2[i:i+len_s1]
            pointer = True
            for key, value in symbol_list.items():

                if curr_str.count(key) < value:
                    pointer = False
                    break

            if pointer:
                break

        return pointer
