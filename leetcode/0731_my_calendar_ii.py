class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        for db_start, db_end in self.double_bookings:
            if start < db_end and end > db_start:
                return False

        for b_start, b_end in self.bookings:
            if start < b_end and end > b_start:
                self.double_bookings.append((max(start, b_start), min(end, b_end)))
        self.bookings.append((start, end))
        return True
