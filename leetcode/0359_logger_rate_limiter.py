class Logger:
    def __init__(self) -> None:
        self.logged_messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        last_seen = self.logged_messages.get(message)

        if last_seen is None or timestamp - last_seen >= 10:
            self.logged_messages[message] = timestamp
            return True
        return False
