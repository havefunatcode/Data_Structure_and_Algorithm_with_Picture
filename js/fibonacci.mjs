function fibonacci(n) {
    if(n == 0 || n == 1) {
        return n;
    }

    return fibonacci(n - 2) + fibonacci(n - 1);
}

function fibonacci_memoization(n, memo) {
    if(n == 0 || n ==1) {
        return n;
    }

    if(memo[n] == null) {
        memo[n] = fibonacci_memoization(n - 2, memo) + fibonacci_memoization(n - 1, memo);
    }

    return memo[n];
}

function fibonacci_tabulation(n) {
    if (n <= 1) {
        return n;
    }

    let table = [0, 1];
    for(let i = 2; i <= n; i++) {
        table[i] = table[i - 2] + table[i - 1];
    }

    return table[n];
}

let start = new Date();
console.log(fibonacci(40));
let end = new Date();
console.log(`fibonacci 함수 실행시간 : ${end - start}ms`)

start = new Date();
console.log(fibonacci_memoization(40, {}));
end = new Date();
console.log(`fibonacci_memoization 함수 실행시간 : ${end - start}ms`)

start = new Date();
console.log(fibonacci_tabulation(40));
end = new Date();
console.log(`fibonacci_tabulation 함수 실행시간 : ${end - start}ms`)