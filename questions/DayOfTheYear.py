class Solution:
    import datetime
    def day_of_year(self, date: str) -> int:

        return int(self.datetime.datetime.strptime(date, '%Y-%m-%d').date().strftime("%j"))
