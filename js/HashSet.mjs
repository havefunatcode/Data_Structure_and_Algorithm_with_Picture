import { HashTable } from "./HashTable.mjs";

class HashSet {
    constructor() {
        this.hashTable = new HashTable();
    }

    add(data) {
        if(this.hashTable.get(data) === null) {
            // value는 사용하지 않기 때문에 임의이 값을 저장한다.
            this.hashTable.set(data, -1);
        }
    }

    isContain(data) {
        return this.hashTable.get(data) !== null;
    }

    remove(data) {
        this.hashTable.remove(value);
    }

    clear() {
        for(let i = 0; i < this.hashTable.arr.length; i++) {
            this.hashTable.arr[i].clear();
        }
    }

    isEmpty() {
        let empty = true;
        for(let i = 0; i < this.hashTable.arr.length; i++) {
            if(this.hashTable.arr[i].count > 0) {
                empty = false;
                break;
            }
        }
        return empty;
    }

    printAll() {
        for(let i = 0; i < this.hashTable.arr.length; i++) {
            let currentNode = this.hashTable.arr[i].head;
            while(currentNode !== null) {
                console.log(currentNode.data.key);
                currentNode = currentNode.next;
            }
        }
    }
    
}

export { HashSet };