# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Fall 2013.
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
from TOAHModel import TOAHModel

import pep8
pep8.Checker('Tour.py', ignore=('W2', 'W3')).check_all()

import time


def move_cheeses(model: TOAHModel, n: int, source: int, intermediate: int,
                 destination: int) -> None:
    """Print moves to get n cheeses from source to destination, possibly
    using intermediate"""
    if n > 1:
        move_cheeses(model, n - 1, source, destination, intermediate)
        move_cheeses(model, 1, source, intermediate, destination)
        move_cheeses(model, n - 1, intermediate, source, destination)
    else:
        model.move(source, destination)
        if animate is True:
            print(model)
            time.sleep(delay)
        

def minimum_M(n: int):
    
    M = []
    if n > 1: 
        for i in range(1, n):
            m = 2 * minimum_M(n - i) + 2 ** i - 1
            M.append(m)
    else:
        m = 1
        M.append(m)
    
    return min(M)


def index_of_M(n: int):
    
    M = []
    if n > 1: 
        for i in range(1, n):
            m = 2 * minimum_M(n - i) + 2 ** i - 1
            M.append(m)
    else:
        return 0    
    
    return M.index(min(M)) + 1


def move_four_stools(model: TOAHModel, n: int, source: int, intermediate1: int, 
                     intermediate2: int, destination: int):
    i = index_of_M(n)
    if n > 1:
        move_four_stools(model, n - i, source, destination, intermediate1,
                         intermediate2)
        move_cheeses(model, i, source, intermediate1, destination)
        move_four_stools(model, n - i, intermediate2, source, intermediate1,
                         destination)
    else:
        model.move(source, destination)
        if animate is True:
            print(model)
            time.sleep(delay)
            

def tour_of_four_stools(model: TOAHModel, delay_btw_moves: float=0.5, 
                        console_animate: bool=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

       model - a TOAHModel with a tower of cheese on the first stool
                and three other empty stools
       console_animate - whether to animate the tour in the console
       delay_btw_moves - time delay between moves in seconds IF 
                         console_animate == True
                         no effect if console_animate == False
    """
    global animate, delay
    animate = console_animate
    delay = delay_btw_moves

    move_four_stools(model, model.number_of_cheeses(), 0, 1, 2, 3)
    
if __name__ == '__main__':
    NUM_CHEESES = 8
    DELAY_BETWEEN_MOVES = .5
    CONSOLE_ANIMATE = False
    
    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)    
    four_stools.fill_first_stool(number_of_cheeses=NUM_CHEESES)
    
    tour_of_four_stools(four_stools, 
                        console_animate=CONSOLE_ANIMATE,
                        delay_btw_moves=DELAY_BETWEEN_MOVES)
    
    print(four_stools.number_of_moves())
