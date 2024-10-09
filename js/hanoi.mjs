function hanoi(count, from, to, temp) {
    if (count == 0) {
        return;
    }
    
    hanoi(count - 1, from, temp, to);
    console.log(`원반 ${count}를 ${from}에서 ${to}로 이동`)
    hanoi(count - 1, temp, to, from);
}

// 원반 개수, 각 기둥
hanoi(3, "A", "B", "C")