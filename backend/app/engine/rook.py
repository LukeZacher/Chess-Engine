from pieces import Piece
from move import Move
from typing import List, Tuple, Optional

class Rook(Piece):
    def __init__(self, color:str, position: Tuple[int, int]):
        super.__init__(color, position)
    
    def get_possible_moves(self, board: List[List[Optional[Piece]]]) -> List[Move]:
        """
        Get all possible moves for a rook by checking all four directions:
        up, down, left, and right until reaching the board edge or another piece.
        
        Args:
            board: 2D list representing the current board state
            
        Returns:
            List of valid moves for the rook
        """
        possible_moves = []
        row, col = self.position
        
        # Define the four directions a rook can move:
        # (row direction, column direction)
        directions = [
            (-1, 0), # up
            (1, 0), # down
            (0, -1), # left
            (0, 1), # right
        ]
        
        #Check each direction
        for row_dir, col_dir in directions:
            current_row = row + row_dir
            current_col = col + col_dir
            
            #Make sure the next square in the direction is a valid location on the board
            while self._is_valid_position((current_row, current_col)):
                current_pos = (current_row, current_col)
                target_piece = board[current_row][current_col]
                
                # If the square is empty
                if target_piece is None:
                    #It's a valid move, add it to possible_moves
                    possible_moves.append(Move(start=self.position, end=current_pos))
                # Otherwise the square is occupied by a piece
                else:
                    # Can capture a piece if it's a different color (WIP)
                    if target_piece.color != self.color:
                        possible_moves.append(Move(start=self.position, end=current_pos))
                    #Stop checking the direction after running into a piece
                    break
                
                # Move to next square in the current direction if no piece was ran into
                current_row += row_dir
                current_col += row_dir
                    
        return possible_moves