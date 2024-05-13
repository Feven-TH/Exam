class Stack:
    def __init__(self):
        self.stack = []
    # Enqueue
Stack.append('A')
Stack.append('B')
Stack.append('C')
print("Queue: ", Stack)

# Dequeue
element = Stack.pop(0)
print("Dequeue: ", element)

# Peek
frontElement = Stack[0]
print("Peek: ", frontElement)

# isEmpty
isEmpty = not bool(Stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(Stack))
