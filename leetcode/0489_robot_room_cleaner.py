from enum import Enum
from typing import Tuple


class Robot:
    def move(self) -> bool:
        ...

    def turnLeft(self) -> None:
        ...

    def turnRight(self) -> None:
        ...

    def clean(self) -> None:
        ...


class Direction(Enum):
    UP = (-1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    DOWN = (1, 0)

    def turn_right(self) -> "Direction":
        if self == Direction.UP:
            return Direction.RIGHT
        elif self == Direction.RIGHT:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.LEFT
        elif self == Direction.LEFT:
            return Direction.UP

    def turn_left(self) -> "Direction":
        if self == Direction.UP:
            return Direction.LEFT
        elif self == Direction.LEFT:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.RIGHT
        elif self == Direction.RIGHT:
            return Direction.UP


class Solution:
    def cleanRoom(self, robot: "Robot") -> None:
        visited = set()

        def visit(current_position: Tuple[int, int], direction: Direction) -> None:
            robot.clean()
            visited.add(current_position)
            for _ in range(4):
                next_position = get_next_position(current_position, direction)
                if next_position not in visited and robot.move():
                    visit(next_position, direction)
                direction = direction.turn_right()
                robot.turnRight()
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        visit((0, 0), Direction.UP)


def get_next_position(start: Tuple[int, int], direction: Direction) -> Tuple[int, int]:
    return tuple(sum(values) for values in zip(start, direction.value))
