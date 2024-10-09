def hanoi(count, source, target, temp):
    if count == 0:
        return
    hanoi(count - 1, source, temp, target)
    print(f"{count} : {source} -> {target}")
    hanoi(count - 1, temp, target, source)

hanoi(3, "A", "C", "B")