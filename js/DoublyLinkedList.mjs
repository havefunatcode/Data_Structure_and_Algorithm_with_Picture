class Node {
    constructor(data, prev = null,next = null) {
        this.data = data;
        this.prev = prev;
        this.next = next;
    }
}

class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.count = 0;
    }

    insertAt(index, data) {
        if (index < 0 || index > this.count) {
            throw new Error('범위를 넘어갔습니다.');
        }

        let newNode = new Node(data);

        // head 추가
        if (index === 0) {
            newNode.next = this.head;
            if (this.head) {
                this.head.prev = newNode;
            }
            this.head = newNode;
        } else if (index === this.count) {
            // tail 추가
            newNode.prev = this.tail;
            this.tail.next = newNode;
            this.tail = newNode;
        } else {
            let current = this.head;

            for (let i = 0; i < index - 1; i++) {
                current = current.next;
            }
            newNode.next = current.next;
            current.next = newNode;
            newNode.prev = current;
            newNode.next.prev = newNode;
        }

        if (newNode.next == null) {
            this.tail = newNode;
        }

        this.count++;
    }

    printAll() {
        let current = this.head;
        let result = '[';

        while (current) {
            result += current.data;
            current = current.next;

            if (current != null) {
                result += ', ';
            }
        }

        result += ']';
        console.log(result);
    }

    clear() {
        this.head = null;
        this.count = 0;
    }

    insertLast(data) {
        this.insertAt(this.count, data);
    }

    deleteAt(index) {
        if (index < 0 || index > this.count) {
            throw new Error('제거할 수 없습니다.');
        }

        let current = this.head;

        // head 제거
        if (index === 0) {
            let deletedNode = current;

            if (this.head.next == null) {
                this.head = null;
                this.tail = null;
            } else {
                this.head = this.head.next;
                this.head.prev = null;
            }
            this.count--;
            return deletedNode;
        } else if (index === this.count - 1) {
            // tail 제거
            let deletedNode = this.tail;
            this.tail.prev.next = null;
            this.tail = this.tail.prev;
            this.count--;
            return deletedNode;
        } else {
            for (let i = 0; i < index - 1; i++) {
                current = current.next;
            }

            let deletedNode = current.next;
            current.next = current.next.next;
            current.next.prev = current;
            this.count--;
            return deletedNode;
        }
    }

    deleteLast() {
        this.deleteAt(this.count - 1);
    }

    getNodeAt(index) {
        if (index < 0 || index > this.count) {
            throw new Error('범위를 넘어갔습니다.');
        }

        let current = this.head;

        for (let i = 0; i < index; i++) {
            current = current.next;
        }
        return current;
    }
}

export { Node, DoublyLinkedList }