class HashTable:
    def __init__(self, len: int):
        self.len = len
        self.hash_table = [[]] * len

    def __str__(self):
        return ''.join(map(str, self.hash_table))

    def hash_func(self, key):
        return key % self.len

    def add(self, key: int, data):
        index = self.hash_func(key)
        if not self.hash_table[index]:
            self.hash_table[index] = [key, data]
        else:
            self.hash_table[index].extend([key, data])

    def search(self, key):
        index = self.hash_func(key)
        if self.hash_table[index]:
            return self.hash_table[index][self.hash_table[index].index(key) + 1]
        else:
            return None

    def remove(self, key: int, data):
        index = self.hash_func(key)
        result = self.search(key)
        if result:
            if data in self.hash_table[index]:
                self.hash_table[index].remove(key)
                self.hash_table[index].remove(data)
            else:
                error = ValueError(f'Відсутнє значення \'{data}\' з ключем ({key}).')
                raise error
        else:
            error = KeyError(f'Відсутній ключ ({key}) у хеш-таблиці.')
            raise error

hash_table = HashTable(7)
hash_table.add(1, 'John')
hash_table.add(2, 'Bil')
hash_table.add(3, 'Peter')
hash_table.add(4, 'Derek')
hash_table.add(5, 'Tom')
hash_table.add(6, 'Jerry')
hash_table.add(7, 'Luke')

print(hash_table)

print(hash_table.search(1))
print(hash_table.search(2))
print(hash_table.search(3))
print(hash_table.search(4))
print(hash_table.search(5))
print(hash_table.search(6))
print(hash_table.search(7))

hash_table.remove(4, "Derek")
print(hash_table)