from collections import defaultdict, deque
from typing import List


def can_construct(originalSeq: List[int], sequences: List[List[int]]) -> bool:
    graph = defaultdict(list)
    ingraph = defaultdict(int)
    sources = set()
    for sequence in sequences:
        for i in range(len(sequence) - 1):
            from_node = sequence[i]
            to_node = sequence[i + 1]
            sources |= {from_node, to_node}
            graph[from_node].append(to_node)
            ingraph[to_node] += 1

    sources -= set(ingraph.keys())
    order = []
    queue = deque(sources)
    while queue:
        if len(queue) > 1:
            # not unique
            return False

        source = queue.popleft()
        order.append(source)
        for child in graph[source]:
            ingraph[child] -= 1
            if ingraph[child] == 0:
                queue.append(child)

    return order == originalSeq


def main():
    print(
        "Can construct: " + str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]]))
    )
    print(
        "Can construct: " + str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]]))
    )
    print(
        "Can construct: "
        + str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]]))
    )


main()
