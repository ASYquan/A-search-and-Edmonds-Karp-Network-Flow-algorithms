import numpy as np
import heapq
from typing import TypeVar
_Self = TypeVar('_Self', bound='PuzzleState') #Created for Syntax-reasons


def manhattan_distance(board : str) -> float:
    """help-method which implements Manhattan-Heuristic
    """
    n = board.shape[0]
    distance = 0
    for x in range(n):
        for y in range(n):
            value = board[x, y]
            if value == 0:
                continue  # Skip the blank tile
            target_x, target_y = divmod(value - 1, n)
            distance += abs(x - target_x) + abs(y - target_y)
    return distance


class PuzzleState:
    def __init__(self, board, moves="", cost=0):
        self.board = np.copy(board)
        self.moves = moves
        self.cost = cost
        self.blank_x, self.blank_y = np.argwhere(self.board == 0)[0]
        self.dimension = self.board.shape[0]

        self.distance = manhattan_distance(self.board)

        # The priority for the priority queue is the total cost: cost so far + heuristic
        self.priority = self.cost + self.distance

    def __lt__(self, other) -> bool:
        return self.priority < other.priority

    def possible_moves(self) -> list[str]:
        """Creates a list of potential moves for the current state
        """
        moves = []

        # Move the blank tile left, right, up, down if possible
        if self.blank_y > 0:
            moves.append("L")
        if self.blank_y < self.dimension - 1:
            moves.append("R")
        if self.blank_x > 0:
            moves.append("U")
        if self.blank_x < self.dimension - 1:
            moves.append("D")

        return moves

    def generate_child(self, move: str) -> _Self:
        """Generates a new instance of our class which
        represents a possible solution as a Node in our graph of solutions

        Returns:
            _Self: An instance of PuzzleState-class
        
        """
        x, y = self.blank_x, self.blank_y

        if move == "L":
            self.board[x, y], self.board[x, y - 1] = self.board[x, y - 1], self.board[x, y]
        elif move == "R":
            self.board[x, y], self.board[x, y + 1] = self.board[x, y + 1], self.board[x, y]
        elif move == "U":
            self.board[x, y], self.board[x - 1, y] = self.board[x - 1, y], self.board[x, y]
        elif move == "D":
            self.board[x, y], self.board[x + 1, y] = self.board[x + 1, y], self.board[x, y]

        child_state = PuzzleState(self.board, self.moves + move, self.cost + 1)

        # Move the blank tile back to its position to restore the current state
        if move == "L":
            self.board[x, y - 1], self.board[x, y] = self.board[x, y], self.board[x, y - 1]
        elif move == "R":
            self.board[x, y + 1], self.board[x, y] = self.board[x, y], self.board[x, y + 1]
        elif move == "U":
            self.board[x - 1, y], self.board[x, y] = self.board[x, y], self.board[x - 1, y]
        elif move == "D":
            self.board[x + 1, y], self.board[x, y] = self.board[x, y], self.board[x + 1, y]

        return child_state


def solve(initial_board: np.ndarray) -> str:
    """Uses A*-search to solve the 8-puzzle in a general way for np.ndarrays

    Returns:
        "" : An empty-string if no solution is found
    """
    start_state = PuzzleState(initial_board)

    open_set = []
    heapq.heappush(open_set, start_state)

    while open_set:
        current_state = heapq.heappop(open_set)
        if current_state.distance == 0:  # Puzzle is solved
            return current_state.moves

        for move in current_state.possible_moves():
            child_state = current_state.generate_child(move)
            heapq.heappush(open_set, child_state)

    return ""  # No solution found



