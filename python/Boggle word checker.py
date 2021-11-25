""" 
Write a function that determines whether a string is a valid guess in a Boggle board, as per the rules of Boggle. 
A Boggle board is a 2D array of individual characters, e.g.:

[ ["I","L","A","W"],
  ["B","N","G","E"],
  ["I","U","A","O"],
  ["A","S","R","L"] ]

Valid guesses are strings which can be formed by connecting adjacent cells (horizontally, vertically, or diagonally) without re-using any previously used cells.

For example, in the above board "BINGO", "LINGO", and "ILNBIA" would all be valid guesses, while "BUNGIE", "BINS", and "SINUS" would not.

Your function should take two arguments (a 2D array and a string) and return true or false depending on whether the string is found in the array as per Boggle rules.

Test cases will provide various array and string sizes (squared arrays up to 150x150 and strings up to 150 uppercase letters). You do not have to check whether the string is a real word or not, only if it's a valid guess.v
 """

def find_word(board, word):
    # first create a grid with extra row and collumn contain ''
    grid = [l + [''] for l in board] + [[''] * (len(board[0]) + 1)]

    """ this rc function start at position x, y and the first value of i
        if the value of i equals to length of word -> return True
        or if the element at position x,y in the grid equal to the ith character of the word -> return True
        if the above condition is true then 
            - set the element at posistion x,y in the grid to '' as a way to mark this position is visited
            - we will then apply rc to all the adjacent position of x,y in the grid and bind the return value to a variable called 'r' -> if any of them return true -> continue checking neighbor
              at last, if r is true -> that means starting at x,y, we can form the desire word by connecting adjacent cellsf
            - return value of r
    """
    def rc(x, y, i):
        if i == len(word):
            return True
        if grid[x][y] != word[i]:
            return False
        grid[x][y] = ''
        # The any() function returns True if any item in an iterable are true
        r = any(rc(x + u, y + v, i + 1) 
                for u in range(-1, 2) 
                for v in range(-1, 2))
        grid[x][y] = word[i]
        return r

    return any(rc(x, y, 0)
                for x in range(len(board))
                for y in range(len(board[x])))

testBoard = [
      ["E","A","R","A"],
      ["N","L","E","C"],
      ["I","A","I","S"],
      ["B","Y","O","R"]
    ]

print(find_word(testBoard, "CEREAL"))
