class CombinationIterator:

    position: int
    combinations: []

    def __init__(self, characters: str, combinationLength: int):
        self.position = -1
        self.combinations = []

        def dfs(idx, path):
            if len(path) == combinationLength:
                self.combinations.append(("").join(path))
                return

            for i in range(idx, len(characters)):
                path.append(characters[i])
                dfs(i+1, path)
                path.pop()

        dfs(0, [])

        self.combinations.sort()

    def next(self) -> str:
        self.position += 1
        return self.combinations[self.position]

    def hasNext(self) -> bool:
        return self.position < len(self.combinations)-1


def test():
    itr = CombinationIterator("abc", 2)
    itr.next()  # return "ab"
    itr.hasNext()  # return True
    itr.next()  # return "ac"
    itr.hasNext()  # return True
    itr.next()  # return "bc"
    itr.hasNext()
