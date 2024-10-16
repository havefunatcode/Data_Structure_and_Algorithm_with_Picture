// 배열의 시작 Index : leftIndex
// 배열의 마지막 Index : rightIndex
// leftIndex == rightIndex 까지 재귀를 호출한다.(= 배열의 원소가 1개인 경우)
function MergeSort(arr, leftIndex, rightIndex) {
    if(leftIndex < rightIndex) {
        let midIndex = parseInt((leftIndex + rightIndex) / 2);
        MergeSort(arr, leftIndex, midIndex);
        MergeSort(arr, midIndex + 1, rightIndex);
        Merge(arr, leftIndex, midIndex, rightIndex);
    }
}

function Merge(arr, leftIndex, midIndex, rightIndex) {
    let leftAreaIndex = leftIndex;
    let rightAreaIndex = midIndex + 1;
    
    let tempArr = [];
    tempArr.length = rightIndex + 1;
    tempArr.fill(0, 0, rightIndex + 1)

    let tempArrIndex = leftIndex;
    while(leftAreaIndex <= midIndex && rightAreaIndex <= rightIndex) {
        if(arr[leftAreaIndex] <= arr[rightAreaIndex]) {
            tempArr[tempArrIndex] = arr[leftAreaIndex++];
        } else {
            tempArr[tempArrIndex] = arr[rightAreaIndex++];
        }
        tempArrIndex++;
    }

    if(leftAreaIndex > midIndex) {
        for(let i = rightAreaIndex; i <= rightAreaIndex; i++) {
            tempArr[tempArrIndex++] = arr[i];
        }
    } else {
        for (let i = leftAreaIndex; i <= midIndex; i++) {
            tempArr[tempArrIndex++] = arr[i];
        }
    }

    for(let i = leftIndex; i <= rightIndex; i++) {
        arr[i] = tempArr[i];
    }
}

let arr = [3, 11, 6, 1, 2, 9, 20, 16, 31, 13]

console.log("=======정렬 전========")
console.log(arr);

MergeSort(arr);

console.log("=======정렬 후========")
console.log(arr);