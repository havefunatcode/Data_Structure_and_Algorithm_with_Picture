function sumArray(arr) {
    // 기저 조건
    if (arr.length == 1) {
        return arr[0];
    }

    // 재ㅣ로 구현하기 위해 sumArray 함수의 구현이 완료되었다고 가정
    return sumArray(arr.slice(0, -1)) + arr[arr.length - 1];
}

let arr = [1, 2, 3, 4, 5];
let sum = sumArray(arr);
console.log(sum);