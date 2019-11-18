class SnapshotArray:
    def __init__(self, length: int) -> None:
        self.snap_id = 0
        self.data = [{self.snap_id: 0} for _ in range(length)]
        self.last_used_snap = [0 for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.data[index][self.snap_id] = val
        self.last_used_snap[index] = self.snap_id

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        while snap_id >= 0:
            result = self.data[index].get(snap_id)
            if result is not None:
                return result
            snap_id -= 1
        return 0


array = SnapshotArray(2)
print(array.snap())  # 0
print(array.get(1, 0))  # 0
print(array.get(0, 0))  # 0
print(array.set(1, 8))  # null
print(array.get(1, 0))  # 0

array = SnapshotArray(4)
print(array.snap())  # 0
print(array.snap())  # 0
print(array.get(2, 1))  # 0
print(array.set(2, 3))  # null
print(array.get(2, 1))  # 0
