class MinStack() {
    // Design a stack that supports push, pop, top, and retrieving the minimum
    // element in constant time.
    //
    //    push(x) -- Push element x onto stack.
    //    pop() -- Removes the element on top of the stack.
    //    top() -- Get the top element.
    //    getMin() -- Retrieve the minimum element in the stack.

    private val stack: MutableList<Pair<Int, Int>> = mutableListOf()

    fun push(x: Int) {
        val currentMin = getMin()
        val newMin = if (currentMin == null || currentMin > x) x else currentMin
        stack.add(Pair(x, newMin))
    }

    fun pop() {
        // stack.removeLastOrNull()  // Kotlin 1.3 not supported in LeetCode
        if (stack.isNotEmpty()) stack.removeAt(stack.lastIndex)
    }

    fun top(): Int? = stack.lastOrNull()?.first
    fun getMin(): Int? = stack.lastOrNull()?.second
}
