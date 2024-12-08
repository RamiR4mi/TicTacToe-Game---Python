def check_game(matrix, sign):
    """Takes a length-3 Matrix representing an XO game as an input and return the sign
    of the winning player. If no player won yet."""
    
    # Checking rows
    for list in matrix: 
        if list == [sign, sign, sign]:
            return sign
    
    # Checking columns
    for i in range(3):
        if matrix[0][i] == sign and matrix[1][i] == sign and matrix[2][i] == sign:
            return sign
    
    # Checking diagonals
    if matrix[0][0] == sign and matrix[1][1] == sign and matrix[2][2] == sign:
        return sign
    elif matrix[0][2] == sign and matrix[1][1] == sign and matrix[2][0] == sign:
        return sign
    
    #Nobody is winning
    return "N"