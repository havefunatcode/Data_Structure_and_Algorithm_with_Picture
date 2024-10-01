class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def print_all(self):
        current_node = self.head
        result = "["
        while current_node:
            result += str(current_node.data)
            current_node = current_node.next
            
            if current_node:
                result += ", "
        result += "]"
        print(result)
    
    def clear(self):
        self.head = None
        self.size = 0
        
    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("추가할 수 있는 범위를 넘어갔습니다.")
        
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        
        self.size += 1
        
    def insert_last(self, data):
        self.insert_at(self.size, data)
        
    def delete_at(self, index):
        if index < 0 or index > self.size:
            raise IndexError("삭제할 수 있는 범위를 넘어갔습니다.")
        
        if index == 0:
            deleted_node = self.head
            self.head = self.head.next
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            deleted_node = current_node.next
            current_node.next = current_node.next.next
        
        self.size -= 1
        return deleted_node
        
    def delete_last(self):
        self.delete_at(self.size - 1)
        
    def get_node_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("범위를 넘어갔습니다.")
        
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node
