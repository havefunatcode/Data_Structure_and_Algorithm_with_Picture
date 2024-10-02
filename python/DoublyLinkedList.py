class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def print_all(self):
        current = self.head
        result = "["
        while current:
            result += str(current.data)
            if current.next:
                result += ", "
            current = current.next
        result += "]"
        print(result)
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("추가할 수 있는 범위를 넘어갔습니다.")
        
        new_node = Node(data)
        
        # 첫 번째 노드 추가
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        # 마지막 노드 추가
        elif index == self.size:
            new_node.prev = self.tail
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node
        # 중간 노드 추가
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.prev = current_node
            new_node.next = current_node.next
            current_node.next = new_node
            current_node.next.prev = new_node
            
        if new_node.next is None:
            self.tail = new_node
        
        self.size += 1
    
    def insert_last(self, data):
        self.insert_at(self.size, data)
        
    def delete_at(self, index):
        if index < 0 or index > self.size:
            raise IndexError("삭제할 수 있는 범위를 넘어갔습니다.")
        
        # 첫 번째 노드 삭제
        if index == 0:
            deleted_node = self.head
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        # 마지막 노드 삭제
        elif index == self.size - 1:
            deleted_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        # 중간 노드 삭제
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            deleted_node = current_node.next
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
        self.size -= 1
        return deleted_node
    
    def delete_last(self):
        return self.delete_at(self.size - 1)
    
    def get_node_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("조회할 수 있는 범위를 넘어갔습니다.")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current