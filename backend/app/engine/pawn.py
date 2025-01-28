from pieces import Piece
from move import Move

from typing import List, Tuple, Optional

class Pawn(Piece):
    def __init__(self, color:str, position: Tuple[int, int]):
        super().__init__(color, position)
        self.en_passant_vulnerable = False
        
    def get_possible_moves(self, board: List[List[Optional['Piece']]]) -> List[Move]:
        """
        Get all possible moves for a pawn including:
        - Moving forward one square
        - Moving forward two squares on first move
        - Diagonal captures
        - (En passant will be implemented later)
        
        Args:
            board: 2D list representing the current board state
            
        Returns:
            List of move objects where pawn can move
        """
        possible_moves = []
        row, col = self.position
        
        # Determine direction based on color (white moves up, black moves down)
        direction = -1 if self.color == 'white' else 1
        
        # Forward Move
        forward_pos = (row + direction, col)
        # Make sure the move is on the board and is not occupied by another piece. If it is, add it to possible_moves
        if (self._is_valid_position(forward_pos) and board[forward_pos[0]][forward_pos[1]] is None):
            possible_moves.append(Move(start=self.position, end=forward_pos, promotion=self._is_promotion_move(forward_pos)))
            
            # First move can be two squares forward
            if not self.has_moved:
                double_forward = (row + direction * 2, col)
                # Make sure the move is on the board and is not occupied by another piece. If it is, add it to possible_moves
                if (self._is_valid_position(double_forward) and board[double_forward[0]][double_forward[1]] is None):
                    possible_moves.append(Move(start=self.position, end=double_forward))
                
        # Diagonal capturing
        # Check both left and right
        for col_offset in [-1, 1]:
            capture_pos = (row + direction, col + col_offset)
            # Make sure the move is on the board
            if self._is_valid_position(capture_pos):
                target_piece = board[capture_pos[0]][capture_pos[1]]
                # If there is a piece and it's a different color, pawn can move there and capture ( WIP )
                if(target_piece is not None and target_piece.color != self.color):
                    possible_moves.append(Move(start=self.position, end=capture_pos, promotion=self._is_promotion_move(capture_pos)))
                         
        return possible_moves
        
    def _is_promotion_move(self, position: Tuple[int, int]) -> bool:
        """Determines if a move results in pawn promotion."""
        return (self.color == 'white' and position[0] == 0) or \
               (self.color == 'black' and position[0] == 7)
               

            