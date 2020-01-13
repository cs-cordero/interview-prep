from dataclasses import dataclass
from typing import Optional


@dataclass
class Booking:
    start: int  # inclusive
    end: int  # non-inclusive
    left: Optional["Booking"] = None
    right: Optional["Booking"] = None

    def conflicts_with(self, other: "Booking") -> bool:
        return self.start < other.end and self.end > other.start


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        prev, node = None, self.root
        booking = Booking(start, end)

        while node is not None:
            if booking.conflicts_with(node):
                return False

            prev = node
            if booking.start > node.start:
                node = node.right
            else:
                node = node.left

        if prev is None:
            self.root = booking
        else:
            self.insert(prev, booking)
        return True

    def insert(self, node: Optional[Booking], booking: Booking) -> None:
        if node is None:
            return booking
        elif node.start < booking.start:
            node.right = self.insert(node.right, booking)
        else:
            node.left = self.insert(node.left, booking)
        return node


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
