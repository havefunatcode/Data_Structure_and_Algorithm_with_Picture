from DoublyLinkedList import DoublyLinkedList

class Deque:
    def __init__(self):
        self.list = DoublyLinkedList()

    def print_all(self):
        self.list.print_all()
    
    def add_first(self, data):
        self.list.insert_at(0, data)
        
    def remove_first(self):
        return self.list.delete_at(0)
    
    def add_last(self, data):
        self.list.insert_last(data)
    
    def remove_last(self):
        return self.list.delete_last()
        
    def is_empty(self):
        return self.list.size == 0
