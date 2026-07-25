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
        new_position = (self.position[0] + random_move[0], self.position[1] + random_move[1])        
        self.position = new_position
        self.path.append(self.position)
        return self.position
    
    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(1,0), (-1, 0), (0, -1), (0, 1)]
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