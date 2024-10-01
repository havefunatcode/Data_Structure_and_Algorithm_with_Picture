from LinkedList import Node, LinkedList

# Node 테스트
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

print(node1.data)
print(node1.next.data)
print(node1.next.next.data)

# LinkedList 테스트
list = LinkedList()

print("------------- insert_at -------------")
list.insert_at(0, 1)
list.insert_at(1, 2)
list.insert_at(2, 3)
list.insert_at(3, 4)
list.print_all()

print("------------- clear -------------")
list.clear()
list.print_all()

print("------------- insert_last -------------")
list.insert_last(1)
list.insert_last(2)
list.insert_last(3)
list.insert_last(4)
list.print_all()

print("------------- delete_at -------------")
list.delete_at(0)
list.print_all()
list.delete_at(1)
list.print_all()

print("------------- delete_last -------------")
list.delete_last()
list.print_all()

print("------------- get_node_at -------------")
print(list.get_node_at(0).data)