class Solution:
    import datetime
    def day_of_year(self, date: str) -> int:

        return int(self.datetime.datetime.strptime(date, '%Y-%m-%d').date().strftime("%j"))


def test():
    assert Solution().day_of_year("2019-01-09") == 9
    assert Solution().day_of_year("2019-02-10") == 41
