# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    #Implement depthFirstSearch with Stack
    stack = util.Stack()
    stack.push([(problem.getStartState(), None, 0)])
    
    while not stack.isEmpty():
        #Pop node from frontier
        frontier = stack.pop() 
        currstate = frontier[-1][0]

        pActions = []
        if problem.isGoalState(currstate):
            for i in frontier:
                    pActions.append(i[1])
            return pActions[1:]

        #implement path checking to prune cyclic paths during search
        path = []
        for successor in problem.getSuccessors(currstate):
            for i in frontier:
                path.append(i[0])
            if successor[0] not in path:
                stack.push(frontier + [successor])
    return False
    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()
    queue.push([(problem.getStartState(), None, 0)])
    seen = {problem.getStartState() : 0}

    while not queue.isEmpty():
        #Pop node from frontier
        frontier = queue.pop() 
        currstate = frontier[-1][0]

        pActions = []
        if problem.getCostOfActions(pActions) <= seen[currstate]:
            if problem.isGoalState(currstate):
                for i in frontier:
                    pActions.append(i[1])
                return pActions[1:]

            #Full Cycle Checking
            for successor in problem.getSuccessors(currstate):
                if (successor[0] not in seen) or ((problem.getCostOfActions(pActions) + successor[2])  < seen[successor[0]]):
                    queue.push(frontier + [successor])
                    seen[successor[0]] = problem.getCostOfActions(pActions) + successor[2]
    return False

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    pQueue = util.PriorityQueue()
    pQueue.push([(problem.getStartState(), None, 0)], 0)
    seen = {problem.getStartState() : 0}
    while not pQueue.isEmpty():
        #Pop node from frontier
        frontier = pQueue.pop() 
        currstate = frontier[-1][0]

        pActions = []
        if problem.getCostOfActions(pActions) <= seen[currstate]:
            if problem.isGoalState(currstate):
                for i in frontier:
                    pActions.append(i[1])
                return pActions[1:]

            #Full Cycle Checking
            for successor in problem.getSuccessors(currstate):
                cost = sum([c for a,b,c in (frontier + [successor])]) 
                if (successor[0] not in seen) or (cost  < seen[successor[0]]):
                    pQueue.push(frontier + [successor], cost)
                    seen[successor[0]] = cost
    return False

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    pQueue = util.PriorityQueue()
    pQueue.push([(problem.getStartState(), None, 0)], heuristic(problem.getStartState(), problem))
    seen = {problem.getStartState() : 0}
    while not pQueue.isEmpty():
        #Pop node from frontier
        frontier = pQueue.pop() 
        currstate = frontier[-1][0]

        pActions = []
        if problem.getCostOfActions(pActions) <= seen[currstate]:
            if problem.isGoalState(currstate):
                for i in frontier:
                    pActions.append(i[1])
                return pActions[1:]

            #Full Cycle Checking
            for successor in problem.getSuccessors(currstate):
                cost = sum([c for a,b,c in (frontier + [successor])]) 
                if (successor[0] not in seen) or (cost  < seen[successor[0]]):
                    pQueue.push(frontier + [successor], cost + heuristic(successor[0], problem))
                    seen[successor[0]] = cost 
    return False


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
