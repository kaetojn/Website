# Copyright 2014 Dustin Wehr
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
ConsoleController: User interface for manually solving Anne Hoy's problems 
from the console.

move: Apply one move to the given model, and print any error message 
to the console. 
"""

from TOAHModel import TOAHModel, Cheese, IllegalMoveError
import pep8
pep8.Checker('ConsoleController.py', ignore=('W2', 'W3')).check_all()


def move(model: TOAHModel, origin: int, dest: int):
    '''
    Module method to apply one move to the given model, and print any
    error message to the console. 
    
    model - the TOAHModel that you want to modify
    origin - the stool number (indexing from 0!) of the cheese you want 
             to move
    dest - the stool number that you want to move the top cheese 
            on stool origin onto.        
    '''    
    if model.top_cheese[dest].size > model.top_cheese[origin].size: 
        try:
            model.move(origin, dest)
        except IllegalMoveError():
            print('You made a mistake, please try again')


class ConsoleController:
    
    def __init__(self: 'ConsoleController', 
                 number_of_cheeses: int, number_of_stools: int):
        """
        Initialize a new 'ConsoleController'.

        number_of_cheeses - number of cheese to tower on the first stool                            
        number_of_stools - number of stools
        """
        self.number_of_stools = TOAHModel(number_of_stools)
        self.number_of_cheeses = \
            self.number_of_stools.fill_first_stool(number_of_cheeses)
                
    def play_loop(self: 'ConsoleController'):
        '''    
        Console-based game. 
        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've 
        provided to print a representation of the current state of the game.
        '''
        
        print('You will have a number of Cheeses stacked on each other in \
        order of size.\n')
        print('You also have a number of stools and the the goal of the game\
        is to get all the Cheeses from one stool to the final stool.\n')
        print('In the process of this you are not allowed to stack a Cheese\
        that is bigger than another.\n') 
        
        user_string = ''
        while user_string != 'Exit Game':
            first_move = input('What is the orgin of the Cheese?:')
            second_move = input('What is the destination of the Cheese?:')
            
            try:
                self.number_of_stools.move(int(first_move), int(second_move)) 
            except IllegalMoveError:
                print('You made a mistake, please try again')
            except ValueError:
                print('You made a mistake, please change your input to an int')
            
            print(self.number_of_stools)
            print(self.number_of_cheeses)
            
            user_string = input('To exit, type Exit Game. Anything 2 continue')
            
if __name__ == '__main__':
     
    number_of_stools = int(input('How many stools are you using?:'))
    number_of_cheeses = int(input('How many Cheeses are you using?:'))
    try:
        number_of_stools
        number_of_cheeses
    except ValueError:
        print('You made a mistake, please change your input to a number')
    
    c = ConsoleController(number_of_cheeses, number_of_stools)
    
    c.play_loop()