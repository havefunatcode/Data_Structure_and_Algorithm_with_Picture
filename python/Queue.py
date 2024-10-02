from DoublyLinkedList import DoublyLinkedList

class Queue:
    def __init__(self):
        self.list = DoublyLinkedList()
        
    def enqueue(self, data):
        self.list.insert_at(0, data)
        
    def dequeue(self):
        try:
            return self.list.delete_last()
        except IndexError:
            return None
    
    def front(self):
        return self.list.tail
    
    def is_empty(self):
        return self.list.size == 0