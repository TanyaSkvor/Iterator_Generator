class FlatIterator:
    def __init__(self, list_of_list):
        self.lists = list_of_list
        self.cursor = 0
        self.stack = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor >= len(self.lists):
            if self.stack:
                self.lists, self.cursor = self.stack.pop()
                return next(self)
            else:
                raise StopIteration
        item = self.lists[self.cursor]
        self.cursor += 1
        if type(item) is not list:
            return item
        else:
            self.stack.append((self.lists, self.cursor))
            self.lists = item
            self.cursor = 0
            return next(self)

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
# for i in FlatIterator(list_of_lists_1):
#     print(i)

print(list(FlatIterator(list_of_lists_1)))

def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print("Проверка выполнена")

if __name__ == '__main__':
    test_1()