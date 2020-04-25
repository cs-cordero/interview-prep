class LRUCache(val capacity: Int) {
    private val linkedHashMap = LinkedHashMap<Int, Int>(capacity, 1f, false)

    fun get(key: Int): Int {
        return linkedHashMap.remove(key)?.let {
            linkedHashMap.put(key, it)
            it
        } ?: -1
    }

    fun put(key: Int, value: Int) {
        linkedHashMap.remove(key)
        linkedHashMap.put(key, value)
        while (linkedHashMap.size > capacity) {
            linkedHashMap.remove(linkedHashMap.iterator().next().key)
        }
    }
}
