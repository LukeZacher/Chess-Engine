from typing import List, Tuple, Optional
from pieces import Piece
from move import Move

class Board:
    def __init__(self):
         """Initialize an empty chess board."""
         self.board: List[List[Optional[Piece]]] = [[None for _ in range(8)] for _ in range(8)]
         self.captured_pieces: List[Piece] = []
         self.white_to_move: bool = True
         
    def get_piece(self, position: Tuple[int, int]) -> Optional[Piece]:
        """Get the piece at the given position."""
        row, col = position
        return self.board[row][col]
    
    def place_piece(self, piece:Piece, position: Tuple[int, int]) -> None:
        """Place a piece at the given position."""
        row, col = position
        self.board[row][col] = piece
        piece.position = position
        
    def remove_piece(self, position: Tuple[int, int]) -> Optional[Piece]:
        """Remove and return the piece at the given position. For moving a piece and capturing a piece"""
        row, col = position
        piece = self.board[row][col]
        self.board[row][col] = None
        return piece
    
    def make_move(self, move: Move) -> bool:
        """
        Execute a move on the board.
        Returns True if move was successful, False otherwise.
        """
        
        #Make sure piece exists on the start square
        start_piece = self.get_piece(move.start)
        if not start_piece:
            return False
        
        # Make sure it's the piece's color's turn
        if(start_piece.color == 'white') != self.white_to_move:
            return False
        
        # Make sure the move is legal for the piece
        if move not in start_piece.get_possible_moves(self.board):
            return False
        
        # Handle capture
        end_piece = self.get_piece(move.end)
        if end_piece:
            self.captured_pieces.append(end_piece)
        
        # Move the piece
        self.remove_piece(move.start)
        self.place_piece(start_piece, move.end)
        start_piece.has_moved = True
        
        # Switch turns
        self.white_to_move = not self.white_to_move
        
        return True
    
    def __str__(self) -> str:
        """Create a string representation of the board"""
        result = []
        # Go through every row in the board
        for row in self.board:
            # List representing each square in the row
            row_str = []
            # For every square in the row, if there is no piece, add '..' to the list. If there is a piece, add the first letter of the piece's name to the list
            for piece in row:
                if piece is None:
                    row_str.append("..")
                else:
                    row_str.append(f"{piece.color[0]}{piece.__class__.__name__[0]}")
            # Separate each item in the list with a space, add to result
            result.append(" ".join(row_str))
        # Return the state of all 64 squares on the board, creating a new line for each row's result
        return "\n".join(result)
    
    def print_captured_pieces(self) -> str:
        """
        Returns a string showing all captured pieces, organized by color.
        """
        white_captures = []
        black_captures = []
        
        for piece in self.captured_pieces:
            if piece.color == "white":
                white_captures.append(piece.__class__.__name__[0])
            else:
                black_captures.append(piece.__class__.__name__[0])
        
        return (f"Black pieces captured by white: {' '.join(black_captures)}\n"
                f"White pieces captured by white: {' '.join(white_captures)}")
    
    
    def initialize_game(self) -> None:
        """Set up the initial chess board position."""
        # TODO: Create and place all pieces in their starting positions
        pass