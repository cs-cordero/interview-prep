class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        value = self.cache.get(key)
        if not value:
            return -1

        self.put(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        existing_value = self.cache.get(key)
        if existing_value:
            del self.cache[key]
        self.cache[key] = value
        while len(self.cache) > self.capacity:
            oldest_key = next(iter(self.cache.keys()))
            del self.cache[oldest_key]
