# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        curPos = currentGameState.getPacmanPosition()
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        fdist = 100000000
        value = 0
        old = 0
        new = 0

        for x in range(newFood.width):
          for y in range(newFood.height):
            if newFood[x][y] == True:
              dist = manhattanDistance(newPos, (x, y))

              #fdist = distance of closest food
              if fdist > dist:
                fdist = dist
                old =  manhattanDistance((x, y), (curPos[0], curPos[1]))
                new =  manhattanDistance((x, y), (newPos[0], newPos[1]))

        #if the "new" distance between the closest food is greater than the "old" distance (no favorable)
        if new > old:
            value -= 10

        for i in range(len(newGhostStates)):
            gdist = manhattanDistance(newPos, newGhostStates[i].getPosition())

            if gdist < 2:
               value -= 100

            if fdist < gdist:
                value += 15

            if fdist > 2 and gdist < 2:
                value -= 15
            
            if gdist < newScaredTimes[i]:
                value += 30

        if newFood[newPos[0]][newPos[1]] != True:
            value -= 5
        else:
            value += 5


        
        return successorGameState.getScore() + value

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def Max(self, gameState, d, agentIndex):
        if gameState.isLose() or gameState.isWin() or d == self.depth:
            return self.evaluationFunction(gameState)

        legalMoves = gameState.getLegalActions(agentIndex)
        maxUtility = float('-inf')

        for action in legalMoves:
            successorGameState = gameState.generateSuccessor(agentIndex, action)
            maxUtility = max(maxUtility, self.Min(successorGameState, d, 1))

        return maxUtility


    def Min(self, gameState, d, agentIndex):
        if gameState.isLose() or gameState.isWin() or d == self.depth:
            return self.evaluationFunction(gameState)

        legalMoves = gameState.getLegalActions(agentIndex)
        minUtility = float('inf')

        for action in legalMoves:
            if agentIndex + 1 > gameState.getNumAgents()-1:
                successorGameState = gameState.generateSuccessor(agentIndex, action)
                minUtility = min(minUtility, self.Max(successorGameState, d+1, 0))
            else:
                successorGameState = gameState.generateSuccessor(agentIndex, action)
                minUtility = min(minUtility, self.Min(successorGameState, d, agentIndex+1))

        return minUtility
            
    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        temp = float('-inf')

        for action in gameState.getLegalActions(0):
            successorGameState = gameState.generateSuccessor(0, action)

           
            m = self.Min(successorGameState, 0, 1)

            if m > temp:
                temp = m 
                answer = action

        return answer

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    def Max(self, gameState, d, agentIndex, alpha, beta):
        if gameState.isLose() or gameState.isWin() or d == self.depth:
            return self.evaluationFunction(gameState)

        legalMoves = gameState.getLegalActions(agentIndex)
        maxUtility = float('-inf')

        for action in legalMoves:
            successorGameState = gameState.generateSuccessor(agentIndex, action)
            maxUtility = max(maxUtility, self.Min(successorGameState, d, 1, alpha, beta))

            if maxUtility >= beta:
                return maxUtility

            if maxUtility > alpha:
                alpha = maxUtility

        return maxUtility


    def Min(self, gameState, d, agentIndex, alpha, beta):
        if gameState.isLose() or gameState.isWin() or d == self.depth:
            return self.evaluationFunction(gameState)

        legalMoves = gameState.getLegalActions(agentIndex)
        minUtility = float('inf')

        if agentIndex + 1 > gameState.getNumAgents()-1:
            for action in legalMoves:
                successorGameState = gameState.generateSuccessor(agentIndex, action)
                minUtility = min(minUtility, self.Max(successorGameState, d+1, 0, alpha, beta))

                if beta > minUtility:
                    beta = minUtility

                if minUtility <= alpha:
                    return minUtility
        else:
            for action in legalMoves:
                successorGameState = gameState.generateSuccessor(agentIndex, action)
                minUtility = min(minUtility, self.Min(successorGameState, d, agentIndex+1, alpha, beta))

                if beta > minUtility:
                    beta = minUtility

                if minUtility <= alpha:
                    return minUtility

        return minUtility

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """

        alpha = float('-inf')
        beta = float('inf')
        temp = float('-inf')

        for action in gameState.getLegalActions(0):
            successorGameState = gameState.generateSuccessor(0, action)

            m = self.Min(successorGameState, 0, 1, alpha, beta)

            if alpha < m:
                alpha = m

            if m > temp:
                temp = m
                answer = action

        return answer

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    def Max(self, gameState, d, agentIndex):
        if gameState.isLose() or gameState.isWin() or d > self.depth:
            return self.evaluationFunction(gameState), None

        legalMoves = gameState.getLegalActions(agentIndex)
        maxUtility = []

        for action in legalMoves:
            successorGameState = gameState.generateSuccessor(agentIndex, action)
            maxUtility.append((self.AverageValue(successorGameState, d, 1)[0], action))
 
        return max(maxUtility)

    def AverageValue(self, gameState, d, agentIndex):
        if gameState.isLose() or gameState.isWin() or d > self.depth:
            return self.evaluationFunction(gameState), None

        legalMoves = gameState.getLegalActions(agentIndex)
        averageUtility = []

        for action in legalMoves:
            successorGameState = gameState.generateSuccessor(agentIndex, action)
            if agentIndex + 1 > gameState.getNumAgents()-1:
                averageUtility.append(self.Max(successorGameState, d+1, 0))
            else:
                averageUtility.append(self.AverageValue(successorGameState, d, agentIndex+1))
        
        value = 0
        for chance in averageUtility:
            value += float(chance[0])

        value /= len(averageUtility)

        return (value, None)

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        return self.Max(gameState, 1, 0)[1]

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """

    curPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood().asList()
    food = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    dist = [1.0/manhattanDistance(x, curPos) for x in newFood]+[0]
    value = max(dist)
    
    for i in range(len(newGhostStates)):
        gdist = manhattanDistance(curPos, newGhostStates[i].getPosition())

        if gdist < 2:
           value -= 100
        
        if gdist < newScaredTimes[i]:
            value += 30
    
    if food[curPos[0]][curPos[1]] != True:
        value -= 5
    else:
        value += 5
    return currentGameState.getScore() + value
    
# Abbreviation
better = betterEvaluationFunction

