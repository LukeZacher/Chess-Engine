from dataclasses import dataclass
from typing import Tuple

@dataclass
class Move:
    """
    Represents a chess move with its properties.
    
    Attributes:
        start: Starting position as (row, col)
        end: Ending position as (row, col)
        promotion: Indicates if this move results in pawn promotion
        en_passant: Indicates if this is an en passant capture
    """
    start: Tuple[int, int]
    end: Tuple[int, int]
    promotion: bool = False
    en_passant: bool = False
    
    def __str__(self) -> str:
        """Provides a readable string representation of the move."""
        base = f"Move from {self.start} to {self.end}"
        if self.promotion:
            base += " (Promotion)"
        if self.en_passant:
            base += " (En Passant)"
        return base