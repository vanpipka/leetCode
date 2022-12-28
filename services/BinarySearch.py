from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0  # В этих переменных храним границы той части списка,
        high = len(nums) - 1  # в которой выполняется поиска

        while low <= high:  # Пока не останется одна позиция
            mid = (low + high)  # Проверяем средний элемент
            guess = nums[mid]
            if guess == target:  # Если искомое значение равно середине
                return mid  # возвращаем ничего
            if guess > target:  # Если много
                high = mid - 1
            else:  # Если мало
                low = mid + 1

        return -1  # Если значение не существует