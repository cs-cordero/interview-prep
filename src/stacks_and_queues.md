# Stacks and Queues

A *stack* is a one-ended linear data structure which models a real world stack
by having two primary operations: `push` and `pop`.

A *queue* is a two-ended linear data structure which models a real world queue
by having two primary operations: `enqueue` and `dequeue`.

## Stacks

### Basic Implementation (Python)
```python
stack = []  # just use a list
stack.append(3)
stack.append(6)
stack.pop()  # 6
stack.append(-1)
```

### Stack uses:
1. Used by undo mechanisms in text editors.
1. Used in compiler syntax checking for matching brackets and braces.
1. Can be used to model a pile of books or plates.
1. Used behind the scenes to support recursion by keeping trak of previous
   function calls.
1. Can be used to do a Depth First Search (DFS) on the stack.

### Complexities

| Operation | Complexity |
|:---:|:---:|
|Push|\\(O(1)\\)|
|Pop|\\(O(1)\\)|
|Peek|\\(O(1)\\)|
|Search|\\(O(N)\\)|
|Size|\\(O(1)\\)|

## Queues

### Basic Implementation (Python)
```python
from collections import deque
queue = deque([])  # a deque is a "double-ended queue"
queue.append(3)
queue.append(5)
queue.popleft()  # 3
```

### Queue uses:
1. Any waiting line models a queue, for example, a lineup at a movie theatre.
1. Can be used to efficiently keep track of the X most recently added elements.
1. Web server request management where you want first come first serve.
1. Breadth first search (BFS) graph traversal.

### Complexities

| Operation | Complexity |
|:---:|:---:|
|Enqueue|\\(O(1)\\)|
|Dequeue|\\(O(1)\\)|
|Peek|\\(O(1)\\)|
|Search|\\(O(N)\\)|
|Removal|\\(O(N)\\)|
|IsEmpty|\\(O(1)\\)|
