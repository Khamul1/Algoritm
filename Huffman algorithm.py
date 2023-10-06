from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value
    
    def get_code(self, root, codes=dict(), code=''):
        if root is None:
            return
        
        if isinstance(root.value, str):
            codes[root.value] = code
            return codes
        
        self.get_code(root.left, codes, code + '0')
        self.get_code(root.right, codes, code + '1')
        
        return codes
    
    def get_tree(self, string):
        string_count = Counter(string)
        
        if len(string_count) <= 1:
            node = Node(None)
            
            if len(string_count) == 1:
                node.left = Node([key for key in string_count][0])
                node.right = Node(None)
            
            string_count = {node: 1}
        
        while len(string_count) != 1:
            node = Node(None)
            spamm = string_count.most_common()[:-3:-1]
            
            if isinstance(spamm[0][0], str):
                node.left = Node(spamm[0][0])
            else:
                node.left = spamm[0][0]
                
            if isinstance(spamm[1][0], str):
                node.right = Node(spamm[1][0])
            else:
                node.right = spamm[1][0]

            del string_count[spamm[0][0]]
            del string_count[spamm[1][0]]
            string_count[node] = spamm[0][1] + spamm[1][1]
        
        return list(string_count.keys())[0]

    def coding(self, string, codes):
        res = ''
        i = 0
        
        while i < len(string):
            for code in codes:
                if code in codes and string[i:].find(codes[code]) == 0:
                    res += code
                    i += len(codes[code])
        
        return res


my_string = input('Введите строку для сжатия: ')
tree = Node(None).get_tree(my_string)

codes = Node(None).get_code(tree)
print(f'Шифр: {codes}')

coded_str = Node(None).coding(my_string, codes)
print(f'Сжатая строка: {coded_str}')

if my_string == coded_str:
    print('Успешно!')
else:
    print('Ошибка!')