import { DoublyLinkedList } from './DoublyLinkedList.mjs';

class Queue {
    constructor() {
        this.list = new DoublyLinkedList();
    }
    
    enqueue(data) {
        this.list.insert(0, data);
    }

    dequeue() {
        try {
            return this.list.deleteLast();
        } catch (error) {
            return null;
        }
    }
    
    front() {
        return this.list.tail;
    }

    isEmpty() {
        return (this.list.count === 0);
    }
    
}

export { Queue }