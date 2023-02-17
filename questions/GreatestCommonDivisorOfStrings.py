class Solution:
    def gcd_of_strings(self, str1: str, str2: str) -> str:

        # you can use the math.gcd here ++++++++++++++++++++++++++++

        max_reminder = min(len(str1), len(str2))
        max_len = max(len(str1), len(str2))
        max_str = max_len
        reminder = max_reminder

        while True:
            reminder = max_len - max_reminder * (max_len//max_reminder)
            if reminder == 0:
                break
            max_len, max_reminder = max_reminder, reminder

        # -----------------------------------------------------------

        # you can use A+B == B+A to check strings symmetry

        while max_reminder >= 1:
            divider = str1[0:max_reminder]
            flag = False
            if len(str1) % max_reminder or len(str2) % max_reminder:
                max_reminder -= 1
                continue

            for i in range(max_str//max_reminder):

                position_f = i*max_reminder
                position_t = position_f + max_reminder
                if str1[position_f:position_t] and str1[position_f:position_t] != divider:
                    flag = True
                    break
                if str2[position_f:position_t] and str2[position_f:position_t] != divider:
                    flag = True
                    break

            if not flag:
                return divider

            max_reminder -= 1

        return ""


def test():

    assert Solution().gcd_of_strings("ABCABC", "ABC") == "ABC"
    assert Solution().gcd_of_strings("ABABCCABAB", "ABAB") == ""
    assert Solution().gcd_of_strings("TAUXXTAUXXTAUXXTAUXXTAUXX",
                                     "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX") == "TAUXX"

