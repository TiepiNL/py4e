'''
THE MAZE
Here is a sample maze:

    #######
    #.....#
    #.###.#
    #..@#.#
    #@#.@.#
    #######

# is a wall, . is a hallway, and @ is a Brussels sprout.

Here is the same maze with player1 - Jen - shown (J) in the upper-left corner at
row 1 and column 1, and player2 -Paul - (P) near the upper-right at row 1 and column 4:

    #######
    #J..P.#
    #.###.#
    #..@#.#
    #@#.@.#
    #######


CONTROLS
The players will move the rats around using the keyboard.
Here are the controls; both have the classic "inverted T" layout:

     player1   player2
up      w         i
down    s         k
left    a         j
right   d         l


GAME PLAY
The players move Jen and Paul around the maze. They cannot move into walls.
If the players try to move the rats into walls, the rats do not move.
Both Jen and Paul can occupy the same space, although if this happens only one
of them will be shown on the maze. (It doesn't matter which one.)

When they move over a Brussels sprout they eat it and the Brussels sprout character @
is replaced by the hallway character '.' . Each rat keeps track of how many Brussels sprouts
it has eaten. When there are no Brussels sprouts left, the game ends. The players can
still move the rats around the maze, but there will not be any more Brussels sprouts
to eat and so the scores will not change.

'''
# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.
# The visual representation of a wall.
WALL = '#'
# The visual representation of a hallway.
HALL = '.'
# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.
# The left direction.
LEFT = -1
# The right direction.
RIGHT = 1
# No change in direction.
NO_CHANGE = 0
# The up direction.
UP = -1
# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    '''
    A rat caught in a maze.
    '''
    def __init__(self, symbol, row, col, num_sprouts_eaten=0):
        ''' (Rat, str, int, int) -> NoneType

        symbol: the 1-character symbol for the rat
        row: the row where the rat is located
        col: the column where the rat is located
        num_sprouts_eaten: the number of sprouts that this rat has eaten,
                           which is initially 0.

        >>> paul = Rat('P', 1, 4)
        >>> paul.row
        1
        >>> jen = Rat('J', 3, 3)
        >>> jen.num_sprouts_eaten
        0
        '''
        # Initialize the rat's instance variables:
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = num_sprouts_eaten


    def set_location(self, row, col):
        ''' (Rat, int, int) -> NoneType

        Set the rat's row and col instance variables to the given row and column.

        >>> paul = Rat('P', 1, 4)
        >>> paul.set_location(2, 4)
        >>> paul.row
        2
        '''
        self.row = row
        self.col = col


    def eat_sprout(self):
        ''' (Rat) -> NoneType

        Add one to the rat's instance variable num_sprouts_eaten.

        >>> jen = Rat('J', 3, 3)
        >>> jen.eat_sprout()
        >>> jen.num_sprouts_eaten
        1
        '''
        self.num_sprouts_eaten += 1


    def __str__(self):
        ''' (Rat) -> str

        Return a string representation of the rat, in this format:
        symbol at (row, col) ate num_sprouts_eaten sprouts.

        >>> jen = Rat('J', 4, 3, 2)
        >>> str(jen)
        'J at (4, 3) ate 2 sprouts.'
        '''
        #return f"{self.symbol} at ({self.row}, {self.col}) ate {self.num_sprouts_eaten} sprouts."
        # Can't use f-string: autograder is python 3.5.
        #pylint: disable-next=consider-using-f-string
        return "{0} at ({1}, {2}) ate {3} sprouts.".format(
            self.symbol, self.row, self.col, self.num_sprouts_eaten)


class Maze:
    '''
    A 2D maze.
    '''
    def __init__(self, maze, rat_1, rat_2):
        ''' (Maze, list of list of str, Rat, Rat) -> NoneType

        maze: a maze with contents specified by the second parameter.
        rat_1: the first rat in the maze.
        rat_2: the second rat in the maze.
        num_sprouts_left: the number of uneaten sprouts in this maze.

        >>> paul = Rat('P', 1, 4)
        >>> jen = Rat('J', 3, 2)
        >>> maze = [['#', '#', '#', '#', '#', '#', '#'], \
                    ['#', '.', '.', '.', '.', '.', '#'], \
                    ['#', '.', '#', '#', '#', '.', '#'], \
                    ['#', '.', '.', '@', '#', '.', '#'], \
                    ['#', '@', '#', '.', '@', '.', '#'], \
                    ['#', '#', '#', '#', '#', '#', '#']]
        >>> board = Maze(maze, paul, jen)
        >>> board.num_sprouts_left
        3
        '''
        # Get the amount of sprouts on the maze.
        num_sprouts_left = 0
        for row in maze:
            num_sprouts_left += row.count(SPROUT)
        #Initialize the maze's instance variables:
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = num_sprouts_left


    def is_wall(self, row, col):
        ''' (Maze, int, int) -> bool

        Return True if and only if there is a wall at the given row and column of the maze.

        >>> paul = Rat('P', 1, 4)
        >>> jen = Rat('J', 3, 2)
        >>> maze = [['#', '#', '#', '#', '#', '#', '#'], \
                    ['#', '.', '.', '.', '.', '.', '#'], \
                    ['#', '.', '#', '#', '#', '.', '#'], \
                    ['#', '.', '.', '@', '#', '.', '#'], \
                    ['#', '@', '#', '.', '@', '.', '#'], \
                    ['#', '#', '#', '#', '#', '#', '#']]
        >>> board = Maze(maze, paul, jen)
        >>> board.is_wall(2, 3)
        True
        >>> board.is_wall(3, 5)
        False
        >>> board.is_wall(3, 3)
        False
        '''
        return self.maze[row][col] == WALL


    def get_character(self, row, col):
        ''' (Maze, int, int) -> str

        Return the character in the maze at the given row and column.

        >>> paul = Rat('P', 1, 4)
        >>> jen = Rat('J', 3, 2)
        >>> maze = [['#', '#', '#', '#', '#', '#', '#'], \
                    ['#', '.', '.', '.', '.', '.', '#'], \
                    ['#', '.', '#', '#', '#', '.', '#'], \
                    ['#', '.', '.', '@', '#', '.', '#'], \
                    ['#', '@', '#', '.', '@', '.', '#'], \
                    ['#', '#', '#', '#', '#', '#', '#']]
        >>> board = Maze(maze, paul, jen)
        >>> board.get_character(0, 0)
        '#'
        >>> board.get_character(1, 5)
        '.'
        >>> board.get_character(3, 3)
        '@'
        >>> board.get_character(3, 2)
        'J'
        '''
        # If there is a rat at the location, then its character should be returned.
        if self.rat_1.row == row and self.rat_1.col == col:
            return self.rat_1.symbol
        elif self.rat_2.row == row and self.rat_2.col == col:
            return self.rat_2.symbol
        else:
            return self.maze[row][col]


    def move(self, rat, vertical, horizontal):
        '''(Maze, Rat, int, int) -> bool

        Move the rat in the given direction (vertical: UP, NO_CHANGE, DOWN;
        horizontal: LEFT, NO_CHANGE< RIGHT), unless there is a wall in the way.
        Check for a Brussels sprout at that location and, if present have
        the rat eat the Brussels sprout.

        Return True if and only if there wasn't a wall in the way.

        >>> paul = Rat('P', 1, 4)
        >>> jen = Rat('J', 3, 2)
        >>> maze = [['#', '#', '#', '#', '#', '#', '#'], \
                    ['#', '.', '.', '.', '.', '.', '#'], \
                    ['#', '.', '#', '#', '#', '.', '#'], \
                    ['#', '.', '.', '@', '#', '.', '#'], \
                    ['#', '@', '#', '.', '@', '.', '#'], \
                    ['#', '#', '#', '#', '#', '#', '#']]
        >>> board = Maze(maze, paul, jen)
        >>> board.move(jen, NO_CHANGE, RIGHT)
        True
        >>> jen.num_sprouts_eaten
        1
        >>> jen.col
        3
        >>> board.maze[3][3]
        '.'
        >>> board.move(paul, UP, NO_CHANGE)
        False
        '''
        # Retrieve the character of the destination.
        new_row = rat.row + vertical
        new_col = rat.col + horizontal
        char = self.get_character(new_row, new_col)
        # Wall test
        if char == WALL:
            return False

        # If a Brussels sprout is found at the location:
        # - have the rat eat the Brussels sprout
        # - make that location a HALL
        # - decrease the value that num_sprouts_left refers to by one
        if char == SPROUT:
            rat.eat_sprout()
            self.maze[new_row][new_col] = HALL
            self.num_sprouts_left -= 1

        rat.set_location(new_row, new_col)

        return True


    def __str__(self):
        ''' (Maze) -> str

        Return a string representation of the maze, in the format:

        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.

        >>> paul = Rat('P', 1, 4)
        >>> jen = Rat('J', 3, 2)
        >>> maze = [['#', '#', '#', '#', '#', '#', '#'], \
                    ['#', '.', '.', '.', '.', '.', '#'], \
                    ['#', '.', '#', '#', '#', '.', '#'], \
                    ['#', '.', '.', '@', '#', '.', '#'], \
                    ['#', '@', '#', '.', '@', '.', '#'], \
                    ['#', '#', '#', '#', '#', '#', '#']]
        >>> board = Maze(maze, paul, jen)
        >>> print(str(board))
        #######
        #...P.#
        #.###.#
        #.J@#.#
        #@#.@.#
        #######
        P at (1, 4) ate 0 sprouts.
        J at (3, 2) ate 0 sprouts.
        '''
        string = ''
        maze_copy = self.maze[:]
        maze_copy[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        maze_copy[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol
        for row in maze_copy:
            string += ''.join(row) + '\n'
        string += str(self.rat_1) + '\n' + str(self.rat_2)
        return string
