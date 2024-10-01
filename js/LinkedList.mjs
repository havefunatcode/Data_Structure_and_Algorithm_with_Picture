class Node {
    constructor(data, next = null) {
        this.data = data;
        this.next = next;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.count = 0;
    }

    insertAt(index, data) {
        if (index < 0 || index > this.count) {
            throw new Error('범위를 넘어갔습니다.');
        }

        let newNode = new Node(data);

        if (index === 0) {
            newNode.next = this.head;
            this.head = newNode;
        } else {
            let current = this.head;

            for (let i = 0; i < index - 1; i++) {
                current = current.next;
            }

            newNode.next = current.next;
            current.next = newNode;
        }
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

        if (index === 0) {
            let deletedNode = current;
            this.head = current.next;
            this.count--;
            return deletedNode;
        } else {
            for (let i = 0; i < index - 1; i++) {
                current = current.next;
            }

            let deletedNode = current.next;
            current.next = current.next.next;
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

export { Node, LinkedList }