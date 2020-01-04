from collections import deque
from typing import List, Tuple


class SnakeGame:
    MOVE_DELTAS = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.snake = deque([(0, 0)])
        self.snake_locations = {(0, 0)}
        self.food = [tuple(location) for location in food]
        self.food_index = 0

    @property
    def head(self) -> Tuple[int, int]:
        return self.snake[-1]

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        delta_row, delta_col = SnakeGame.MOVE_DELTAS[direction]
        curr_row, curr_col = self.head
        next_row, next_col = curr_row + delta_row, curr_col + delta_col

        tail = self.snake.popleft()
        self.snake_locations.remove(tail)

        if (
            next_row < 0
            or next_col < 0
            or next_row >= self.height
            or next_col >= self.width
            or (next_row, next_col) in self.snake_locations
        ):
            return -1

        next_point = (next_row, next_col)
        self.snake.append(next_point)
        self.snake_locations.add(next_point)
        if (
            self.food_index < len(self.food)
            and next_point == self.food[self.food_index]
        ):
            self.food_index += 1
            self.snake.appendleft(tail)
            self.snake_locations.add(tail)
        return self.food_index
