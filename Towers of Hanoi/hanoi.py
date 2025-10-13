from typing import TypeVar, Generic, List, Tuple

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


def solve_hanoi(num_disks: int) -> List[Tuple[str, str]]:
    moves = []

    def _generate_moves(n: int, source: str, destination: str, auxiliary: str):
        if n == 1:
            moves.append((source, destination))
            return

        _generate_moves(n - 1, source, auxiliary, destination)
        moves.append((source, destination))
        _generate_moves(n - 1, auxiliary, destination, source)

    _generate_moves(num_disks, "A", "C", "B")

    return moves
