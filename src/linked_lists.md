# Singly and Doubly Linked Lists

## Linked Lists
A *linked list* is a sequential list of nodes that hold data and which point to
other nodes, which also contain data.

Data -> Data -> None

A *singly linked list* will only hold a reference to the next node.  In the
implementation, you always maintian a reference to the `head`, and sometimes
also the `tail` for faster additions/removals.

A *doubly linked list* is the same as a singly linked list, except that it also
maintains a second pointer pointing back to the previous node before it.

### Basic Implementation (Python)
```python
class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None
```

### Linked List uses:
1. Used in many List, Queue and Stack implementation.
1. Great for creating circular lists.
1. Can easily model real world objects such as trains.
1. Used in separate chaining, which is present in certain Hashtable
   implementations to deal with hashing collisions.
1. Often used in the implementation of adjacency lists for graphs.

### Terminology
| Term | Definition |
|:---:|:---|
| Head | The first node in a linked list. |
| Tail | The last node in a linked list. |
| Pointer | Reference to another node. |
| Node | An object containing data and pointer(s). |

### Pros and Cons
* Singly Linked List
    * Pro:  Uses less memory
    * Pro:  Simpler implementation
    * Con:  Cannot easily access previous elements.
* Doubly Linked List
    * Pro:  Can be traversed backwards
    * Con:  Takes 2x the memory of Singly Linked List.

### Complexities
| | Singly Linked List | Doubly Linked List |
|:---:|:---:|:---:|
|Search|\\(O(N)\\)|\\(O(N)\\)|
|Insert at head|\\(O(1)\\)|\\(O(1)\\)|
|Insert at tail|\\(O(1)\\)|\\(O(1)\\)|
|Remove at head|\\(O(1)\\)|\\(O(1)\\)|
|Remove at tail|\\(O(N)\\)|\\(O(1)\\)|
|Remove from middle|\\(O(N)\\)|\\(O(N)\\)|
