from move import Move

from abc import ABC, abstractmethod
from typing import List, Tuple, Optional

class Piece(ABC):
    def __init__(self, color: str, position: Tuple[int][int]):
        """
        Initialize a chess piece
        Args:
            color: 'white' or 'black'
            position: (row, col) on the board where (0,0) is top-left
        """
        self.color = color
        self.position = position
        self.has_moved = False
        
    @abstractmethod
    def get_possible_moves(self, board: List[List[Optional['Piece']]]) -> List[Move]:
        """
        Get all possible moves for this piece given the current board state.
        Must be implemented by each piece type.
        
        Args:
            board: 2D list representing the current board state
            
        Returns:
            List of move objects representing possible moves
        """
        pass
    
    @staticmethod
    def _is_valid_position(position: Tuple[int, int]) -> bool:
        """
        Check if a position is within the board boundaries
        
        Args:
            position: (row, col) position to check
            
        Returns:
            True if position is on board, False otherwise
        """
        row, col = position
        return 0 <= row < 8 and 0 <= col < 8
    
    def __repr__(self) -> str:
        """
        String representation of the piece (useful for debugging)
        """
        return f"{self.color} {self.__class__.__name__} at {self.position}"
    