from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()
        
    def push(self, data):
        self.list.insert_at(0, data)
        
    def pop(self):
        try:
            return self.list.delete_at(0)
        except IndexError:
            return None
    
    def peek(self):
        return self.list.head.data
    
    def is_empty(self):
        return self.list.size == 0