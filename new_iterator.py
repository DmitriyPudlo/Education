class FlatIterator:
    def __init__(self, lists):
        self.lists = lists
        self.sum_list = self._open_list()
        self.current = 0

    def _open_list(self):
        self.sum_list = []
        for list_ in self.lists:
            self.sum_list += list_
        return self.sum_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.sum_list):
            result = self.sum_list[self.current]
            self.current += 1
            return result
        raise StopIteration


nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]

for item in FlatIterator(nested_list):
    print(item)