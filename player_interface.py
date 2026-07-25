"""
Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:
The Player class should have a method named make_move that:

Uses random.choice to get a random move from the moves attribute (defined in the concrete class).
Adds the values from the selected move to the current position and updates the position attribute.
Appends the new position tuple to the path attribute.
Returns the new position.
The Player class should have an abstract method named level_up to be implemented in concrete classes.

You should define a Pawn class that inherits from the Player class.

The Pawn class should use super() to call the parent's __init__ method and then set the moves attribute to a list of tuples representing x, y coordinates.

Each coordinate tuple should represent a movement of 1 unit in the following directions: up, down, left, right.

The Pawn class should implement a concrete level_up method by adding more moves to the moves attribute. The added moves should represent the four diagonal movements (for example, 1 unit down plus 1 unit left).

Note: Standard library modules should be imported without using aliases. Tests related to the Player class will fail until the Pawn class becomes instantiable.

Tests:
Waiting:11. The Player's make_move method should update the position attribute by adding to it the coordinates of the randomly selected move.
Waiting:12. The Player's make_move method should append the new position tuple to the path attribute.
Waiting:13. The Player's make_move method should return the updated position attribute.
Waiting:14. The Player class should have a level_up method.
Waiting:15. The Player's level_up method should have a single parameter self.
Waiting:16. The Player's level_up method should be an abstract method.
Waiting:17. The Player class should be an abstract class.
Waiting:18. You should have a class named Pawn.
Waiting:19. The Pawn class should inherit from the Player class.
Waiting:20. The Pawn class should have an __init__ method.
Waiting:21. The Pawn's __init__ method should have a single parameter self.
Waiting:22. The Pawn's __init__ method should call the parent's __init__ with using the super function.
Waiting:23. The Pawn's __init__ method should set the moves attribute to a list of tuples representing x, y coordinates, where each coordinate tuple represents a movement of 1 unit in the following directions: up, down, left, right.
Waiting:24. The Pawn class should have a level_up method.
Waiting:25. The Pawn's level_up method should add the four diagonal movement of 1 unit to the moves attribute.
"""
from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    def make_move(self):
        random_move = random.choice(self.moves)
        print(random_move)
        # add the values from random.choice to self.position
        new_position = (self.position[0] + random_move[0], self.position[1] + random_move[1])
        # update self.position attribute        
        self.position = new_position
        # append new position tuple to self.path
        self.path.append(self.position)
        return self.position
    
    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [self.position]
        print(self.moves)

    def level_up(self):
        move_up_left = (self.position[0] +1, self.position[1] -1)
        move_up_right = (self.position[0] +1, self.position[1] +1)
        move_down_left = (self.position[0] -1, self.position[1] -1)
        move_down_right = (self.position[0] -1, self.position[1] +1)

        self.moves.append(move_up_left)
        self.moves.append(move_up_right)
        self.moves.append(move_down_left)
        self.moves.append(move_down_right)

pawn = Pawn()
pawn.level_up()
pawn.make_move()