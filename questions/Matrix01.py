from typing import List
import copy


class Solution:

    def update_matrix(self, mat: List[List[int]]) -> List[List[int]]:

        def get_index(list):
            try:
                result_ = list.index(pointer, y + 1)
            except:
                result_ = None

            return result_

        h = len(mat)
        w = len(mat[0])

        result = []

        for a in range(len(mat)):
            result.append([None for b in mat[a]])

        pointer = 0
        while True:

            result_found = True

            for x in range(len(mat)):

                if pointer not in mat[x]:
                    continue

                y = mat[x].index(pointer)

                while y is not None:

                    result_found = False

                    if result[x][y] is None and pointer != 0:
                        y = get_index(mat[x])
                        continue

                    result[x][y] = pointer

                    if x >= 1:
                        if result[x - 1][y] is None:
                            mat[x - 1][y] = 0 if mat[x - 1][y] == 0 else pointer+1
                            result[x - 1][y] = 0 if mat[x - 1][y] == 0 else pointer+1
                    if x + 1 < h:
                        if result[x + 1][y] is None:
                            mat[x + 1][y] = 0 if mat[x + 1][y] == 0 else pointer+1
                            result[x + 1][y] = 0 if mat[x + 1][y] == 0 else pointer+1
                    if y >= 1:
                        if result[x][y - 1] is None:
                            mat[x][y - 1] = 0 if mat[x][y - 1] == 0 else pointer+1
                            result[x][y - 1] = 0 if mat[x][y - 1] == 0 else pointer+1
                    if y + 1 < w:
                        if result[x][y + 1] is None:
                            mat[x][y + 1] = 0 if mat[x][y + 1] == 0 else pointer+1
                            result[x][y + 1] = 0 if mat[x][y + 1] == 0 else pointer+1

                    y = get_index(mat[x])

            pointer += 1

            if result_found:
                break

        return result

