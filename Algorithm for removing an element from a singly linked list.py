class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def add__at_head(self, data):
        self.head = Node(data=data, next_node = self.head)

    def delete_at_head(self):
        self.head = self.head.next_node

    def search(self,value):
        current_node = self.head
        while current_node:
            if current_node.data == value: 
                return True
            current_node = current_node.next_node
        return False
    
linked_list = LinkedList()
linked_list.add__at_head(3)
linked_list.add__at_head(5)
linked_list.delete_at_head()
print(linked_list.search(3))
print(linked_list.search(5))