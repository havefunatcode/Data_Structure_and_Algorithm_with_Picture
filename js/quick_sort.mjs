function quickSort(arr, left, right) {
    if(left <= right) {
        // 정렬되는 pivot의 Index를 반환
        let pivot = divide(arr, left, right);
        quickSort(arr, left, pivot - 1);
        quickSort(arr, pivot + 1, right);
    }
}

function divide(arr, left, right) {
    let pivot = arr[left];
    let leftStartIndex = left + 1;
    let rightStartIndex = right;

    while(leftStartIndex <= rightStartIndex) {
        while(leftStartIndex <= right && pivot >= arr[leftStartIndex]) {
            leftStartIndex++;
        }

        while(rightStartIndex >= (left + 1) && pivot <= arr[rightStartIndex]) {
            rightStartIndex--;
        }

        if(leftStartIndex <= rightStartIndex) {
            swap(arr, leftStartIndex, rightStartIndex);
        }
    }

    swap(arr, left, rightStartIndex)
    return rightStartIndex;
}

function swap(arr, index1, index2) {
    let temp = arr[index1];
    arr[index1] = arr[index2];
    arr[index2] = temp;
}

let arr = [3, 11, 6, 1, 2, 9, 20, 16, 31, 13]

console.log("=======정렬 전========")
console.log(arr);

quickSort(arr, 0, arr.length - 1);

console.log("=======정렬 후========")
console.log(arr);