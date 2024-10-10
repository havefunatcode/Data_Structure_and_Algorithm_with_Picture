function SelectionSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        // i부터 시작하는 이유
        // 반복문을 진행할 때마다 최소값이 하나씩 정렬되기 때문에 정렬된 영역은 반복에서 제외하기 위함
        let minValueIndex = i;

        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[minValueIndex]) {
                minValueIndex = j;
            }
        }

        let temp = arr[i];
        arr[i] = arr[minValueIndex];
        arr[minValueIndex] = temp;
    }
}

let arr = [4, 2, 3, 1];

console.log("=======정렬 전========")
console.log(arr);

BubbleSort(arr);

console.log("=======정렬 후========")
console.log(arr);