class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # вычисляем хэш-код ключа
        return sum(ord(char) for char in key) % self.size

    def _find_index(self, key, cells):
        # находим индекс ячейки для ключа
        for i in range(len(cells)):
            if cells[i][0] == key:
                return i
        return None

    def _add_to_tree(self, node, value):
        # добавляем узел в дерево
        if node is None:
            return TreeNode(value)
        if node.key == value[0]:
            node.value = value[1]
        elif node.key < value[0]:
            node.right = self._add_to_tree(node.right, value)
        else:
            node.left = self._add_to_tree(node.left, value)
        return node

    def _delete_from_tree(self, node, key):
        # удаляем узел из дерева
        if node is None:
            return node
        if node.key == key:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            min_node = node.right
            while min_node.left is not None:
                min_node = min_node.left
            node.key = min_node.key
            node.value = min_node.value
            node.right = self._delete_from_tree(node.right, min_node.key)
        elif node.key < key:
            node.right = self._delete_from_tree(node.right, key)
        else:
            node.left = self._delete_from_tree(node.left, key)
        return node

    def add(self, key, value):
        index = self._hash(key)
        cells = self.table[index]
        i = self._find_index(key, cells)
        if i is not None:
            cells[i][1] = value
        else:
            cells.append([key, value])
            if len(cells) > 1:
                # дерево создается только при наличии коллизий
                tree = None
                for key, value in cells:
                    tree = self._add_to_tree(tree, (key, value))
                cells[0][1] = tree

    def get(self, key):
        index = self._hash(key)
        cells = self.table[index]
        i = self._find_index(key, cells)
        if i is not None:
            return cells[i][1] if len(cells[i]) == 2 else self._find_value_in_tree(cells[i][1], key)
        return None

    def _find_value_in_tree(self, node, key):
        # поиск значения в дереве по ключу
        while node is not None:
            if node.key == key:
                return node.value
            elif node.key < key:
                node = node.right
            else:
                node = node.left
        return None

    def delete(self, key):
        index = self._hash(key)
        cells = self.table[index]
        i = self._find_index(key, cells)
        if i is not None:
            if len(cells[i]) == 2:
                # удаляем из дерева
                cells[i][1] = self._delete_from_tree(cells[i][1], key)
            else:
                cells.pop(i)

    def __repr__(self):
        result = ""
        for i, cells in enumerate(self.table):
            result += f"{i}: {cells}\n"
        return result

hash_table = HashTable(5)
hash_table.add('hello', 'world')
hash_table.add('apple', 5)
hash_table.add('banana', {'a': 1, 'b': 2})
hash_table.add('cat', 'dog')

print(hash_table)  

print(hash_table.get('hello'))  
print(hash_table.get('apple'))  
print(hash_table.get('banana'))  
print(hash_table.get('cat'))  

print(hash_table.get('unknown'))  