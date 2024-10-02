from Queue import Queue
queue = Queue()

print("------------- enqueue -------------")
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.front().data)

print("------------- dequeue -------------")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(f"isEmpty: {queue.is_empty()}")
