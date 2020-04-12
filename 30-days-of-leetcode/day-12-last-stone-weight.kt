class MinHeap<T : Comparable<T>>() {
    private var heap: MutableList<T> = mutableListOf()

    fun push(item: T) {
        heap.add(item)
        siftUp(heap.lastIndex)
    }

    fun pop(): T? {
        if (heap.isEmpty()) return null

        swap(0, heap.lastIndex)
        val poppedElement = heap.removeAt(heap.lastIndex)
        if (heap.isNotEmpty()) siftDown(0)
        return poppedElement
    }

    fun peek(): T? = heap.getOrNull(0)

    fun size(): Int = heap.size

    private fun siftUp(i: Int) {
        var currentIndex = i
        val currentElement = heap.elementAt(i)
        while (currentIndex > 0) {
            val parentIndex = parent(currentIndex)
            val parentElement = heap.elementAt(parentIndex)
            if (currentElement < parentElement) {
                swap(currentIndex, parentIndex)
                currentIndex = parentIndex
            } else {
                break
            }
        }
    }

    private fun siftDown(i: Int) {
        var currentIndex = i
        val currentElement = heap.elementAt(i)
        while (true) {
            val indexOfSmallerChild = children(currentIndex)
                .toList()
                .filter { it <= heap.lastIndex }
                .sortedBy { heap.elementAt(it) }
                .firstOrNull()
            if (indexOfSmallerChild == null) break
            if (currentElement > heap.elementAt(indexOfSmallerChild)) {
                swap(currentIndex, indexOfSmallerChild)
                currentIndex = indexOfSmallerChild
            } else {
                break
            }
        }
    }

    private fun parent(child: Int) = (child - 1) / 2

    private fun children(parent: Int) = Pair(parent * 2 + 1, parent * 2 + 2)

    private fun swap(i: Int, j: Int) {
        val elementI = heap.elementAt(i)
        val elementJ = heap.elementAt(j)
        heap.set(i, elementJ)
        heap.set(j, elementI)
    }
}

class Solution {
    fun lastStoneWeight(stones: IntArray): Int {
        val minheap = MinHeap<Int>()
        stones.forEach { minheap.push(-it) }

        while (minheap.size() > 1) {
            val nextElement = minheap.pop() ?: 0 - minheap.pop() ?: 0
            if (nextElement != 0) {
                minheap.push(nextElement)
            }
        }

        val result = minheap.pop()
        return if (result == null) 0 else result * -1
    }
}
