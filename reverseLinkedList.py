class Node:
    def __init__(self, value: int, next):
        self._value = value
        self._next = next
    
    @property 
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value: int):
        self._value = new_value

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, new_next):
        self._next = new_next

ll = []
for i in range(9):
    node = Node(i, None)
    if i - 1 >= 0:
        ll[i-1].next = node
    ll.append(node)

print(f"Initial: {[f'c{n.value},n{n.next.value}' for n in ll if n.next != None]}")

# Standard Setup per Iteration
curr = ll[0]
next = curr.next
next_next = curr.next.next

# Change Direction
next.next = curr

# Only Necessary for First Time
curr.next = None

while True:
    curr = next
    next = next_next
    if next.next == None:
        next.next = curr
        break
    else:
        next_next = next.next
        next.next = curr

print(f"Reversed: {[f'c{n.value},n{n.next.value}' for n in ll if n.next != None]}")