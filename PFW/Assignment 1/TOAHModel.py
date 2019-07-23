# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2014.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""
TOAHModel:  Model a game of Towers of Anne Hoy
Cheese:   Model a cheese with a given (relative) size
IllegalMoveError: Type of exceptions thrown when an illegal move is attempted
MoveSequence: Record of a sequence of (not necessarily legal) moves. You will 
need to return MoveSequence object after solving an instance of the 4-stool 
Towers of Anne Hoy game, and we will use that to check the correctness of your
algorithm.
"""
import pep8
pep8.Checker('TOAHModel.py', ignore=('W2', 'W3')).check_all()


class TOAHModel:
    
    def __init__(self: 'TOAHModel', number_of_stools: int):
        """Model a game of Towers Of Anne Hoy.
    
        Model stools holding stacks of cheese, enforcing the constraint
        that a larger cheese may not be placed on a smaller one.
    
        fill_first_stool -put an existing model in the standard starting config
        move - move cheese from one stool to another
        add - add a cheese to a stool        
        top_cheese - top cheese on a non-empty stool    
        cheese_location - index of the stool that the given cheese is on
        number_of_cheeses - number of cheeses in this game
        number_of_moves - number of moves so far
        number_of_stools - number of stools in this game
        get_move_seq - MoveSequence object that records the moves used so far
         
        """
        self._move_seq = MoveSequence([])
        
        self.stools = []
        
        for i in range(number_of_stools):
            self.stools.append([])
            
    def fill_first_stool(self: 'TOAHModel', number_of_cheeses: int):
        """
        Precondition: The value Put in must be a positive integer 
        
        Put number_of_cheeses cheeses on the first (i.e. 0-th) stool, in order 
        of size, with a cheese of size == number_of_cheeses on bottom and 
        a cheese of size == 1 on top.
        
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.stools[0][-1] == Cheese(1)
        True
        """
        for i in range(number_of_cheeses, 0, -1):
            self.stools[0].append(Cheese(i))
            
    def _cheese_at(self: 'TOAHModel', stool_index, 
                   stool_height: int) -> 'Cheese':
        """
        Precondiciton: The index of the stool (stool_index) must exist. 
        Same goes for stool height.
        
        If there are at least stool_height+1 cheeses 
        on stool stool_index then return the (stool_height)-th one.
        Otherwise return None.
        
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M._cheese_at(0,3).size
        2
        >>> M._cheese_at(0,0).size
        5
        """
        if len(self.stools[stool_index]) >= stool_height + 1:
            return self.stools[stool_index][stool_height]
        
    def move(self: 'TOAHModel', old_stool: int, new_stool: int):
        """
        Precondition: The index of the stool (old_stool and new_stool) must 
        exist.
        
        This fuction moves the current top cheese at the index of the old
        stool and then moves the cheese to the index of the new stool. It only
        works if there is the no cheese at the new stool or the cheese at the 
        new stool is bigger than the cheese being moved.
        
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.move(0,1)
        >>> M.cheese_location(Cheese(1))  == 1
        True
        """
        if self.stools[new_stool] == [] or \
           self.stools[new_stool][-1].size > self.stools[old_stool][-1].size:
            self.stools[new_stool].append(self.stools[old_stool].pop())
            
            self._move_seq.add_move(old_stool, new_stool)
    
    def add(self: 'TOAHModel', stool_index: int, cheese: 'Cheese'):
        """
        Precondtion: The stool_index must exist.
        
        This fuction adds the specified cheese the specified stool_index. 
        stool and then moves the cheese to the index of the new stool. It only
        works if there is the no cheese at the stool_index or the cheese at the  
        stool_index is bigger than the cheese being added.
        
        >>> M = TOAHModel(4)
        >>> M.add(0, Cheese(1))
        >>> M.cheese_location(Cheese(1)) == 0
        True
        """
        if self.stools[stool_index] == [] or (self.stools[stool_index][-1].size
                                              < cheese.size):
            self.stools[stool_index].append(cheese)
        
    def top_cheese(self: 'TOAHModel', stool_index: int) -> 'Cheese':
        """
        Precondtion: The stool_index must exist.
        
        Returns the cheese at the top of that specified stool.
        
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(3)
        >>> M.move(0, 1)
        >>> M.top_cheese(0)
        Cheese(2)
        """
        if self.stools[stool_index] != []:
            return self.stools[stool_index][-1]
        
    def cheese_location(self: 'TOAHModel', cheese: 'Cheese') -> int:
        """
        Precondtion: Cheese must exist.
        
        Returns the location of the specified cheese.
        
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(3)
        >>> M.cheese_location(Cheese(1))
        0
        """
        for i in range(len(self.stools)):
            if cheese in self.stools[i]:
                return i
    
    def number_of_moves(self: 'TOAHModel') -> int:
        """
        Returns number of moves in the game.
        
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(3)
        >>> M.move(0, 2)
        >>> M.move(0, 1)
        >>> M.number_of_moves()
        2
        
        """
        return self._move_seq.length()
    
    def number_of_cheeses(self: 'TOAHModel') -> int:
        """
        Returns number of cheeses in the game.
        
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(3)
        >>> M.number_of_cheeses()
        3
        """ 
        total_cheese = 0
        
        for i in range(len(self.stools)):
            for i in range(len(self.stools[i])):
                total_cheese += 1
        return total_cheese
    
    def number_of_stools(self: 'TOAHModel') -> int:
        """
        Returns number of cheeses in the stools.
        
        >>> M = TOAHModel(4)
        >>> M.number_of_stools()
        4
        """  
        return len(self.stools)
        
    def get_move_seq(self: 'TOAHModel') -> 'MoveSequence':
        return self._move_seq    
                
    def __eq__(self: 'TOAHModel', other: 'TOAHModel') -> bool:
        """
        We're saying two TOAHModels are equivalent if their current 
        configurations of cheeses on stools look the same. 
        More precisely, for all h,s, the h-th cheese on the s-th 
        stool of self should be equivalent the h-th cheese on the s-th 
        stool of other
        
        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0,1)
        >>> m1.move(0,2)
        >>> m1.move(1,2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0,3)
        >>> m2.move(0,2)
        >>> m2.move(3,2)
        >>> m1 == m2
        True
        """
        
        if self.stools[0] == other.stools[0]:
            for i in range(len(self.stools)):
                if self.stools[i] != other.stools[i]:
                    return False
            return True    
    
    def __str__(self: 'TOAHModel') -> str:       
        """
        Depicts only the current state of the stools and cheese.
        """
        all_cheeses = []
        for height in range(self.number_of_cheeses()):
            for stool in range(self.number_of_stools()):   
                if self._cheese_at(stool, height) is not None:
                    all_cheeses.append(self._cheese_at(stool, height))        
        max_cheese_size = max([c.size for c in all_cheeses]) \
                            if len(all_cheeses) > 0 else 0
        stool_str = "=" * (2 * max_cheese_size + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.number_of_stools()
        
        def cheese_str(size: int):            
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler
        
        lines = ""
        for height in range(self.number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = cheese_str(int(c.size))
                else:
                    s = cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str
        
        return lines
    
    
class Cheese:
    def __init__(self: 'Cheese', size: int):
        """
        Initialize a Cheese to diameter size.

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = size

    def __repr__(self: 'Cheese') -> str:
        """
        Representation of this Cheese
        """
        return "Cheese(" + str(self.size) + ")"

    def __eq__(self: 'Cheese', other: 'Cheese') -> bool:
        """Is self equivalent to other? We say they are if they're the same 
        size."""
        return isinstance(other, Cheese) and self.size == other.size
    
       
class IllegalMoveError(Exception):
    pass

       
class MoveSequence:
    def __init__(self: 'MoveSequence', moves: list):
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves
            
    def get_move(self: 'MoveSequence', i: int):
        # Exception if not (0 <= i < self.length)
        return self._moves[i]
        
    def add_move(self: 'MoveSequence', src_stool: int, dest_stool: int):
        self._moves.append((src_stool, dest_stool))
        
    def length(self: 'MoveSequence') -> int:
        return len(self._moves)
    
    def generate_TOAHModel(self: 'MoveSequence', number_of_stools: int, 
                           number_of_cheeses: int) -> 'TOAHModel':
        """
        An alternate constructor for a TOAHModel. Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in this move sequence.
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model
        
    def __repr__(self: 'MoveSequence') -> str:
        return "MoveSequence(" + repr(self._moves) + ")"


#if __name__ == '__main__':
    #import doctest
    #doctest.testmod(verbose=True)
