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


    def getAction(self, game_state):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a game_state and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = game_state.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(game_state, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentgame_state, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        game_states (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a game_state (pacman.py)
        successorgame_state = currentgame_state.generatePacmanSuccessor(action)
        newPos = successorgame_state.getPacmanPosition()
        newFood = successorgame_state.getFood()
        newGhostStates = successorgame_state.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorgame_state.getScore()

def scoreEvaluationFunction(currentgame_state):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentgame_state.getScore()

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

# MinimaxAgent class inherits from MultiAgentSearchAgent class

class MinimaxAgent(MultiAgentSearchAgent):
    # getAction method returns the best action for the agent at the current state
    def getAction(self, game_state):
        bestAction = None
        bestScore = float("-inf")
        legalActs = game_state.getLegalActions(0)
        for action in legalActs:
            score = self.minimax(game_state.generateSuccessor(0, action), self.depth, 1)
            if score > bestScore:
                bestAction = action
                bestScore = score

        return bestAction

# minimax method returns the best score for the agent at the current state
    def minimax(self, game_state, depth, agent_index):
        if depth == 0 or game_state.isWin() or game_state.isLose():
            return self.evaluationFunction(game_state)

        if agent_index == 0:
            bestScore = float("-inf")
            legalActs = game_state.getLegalActions(0)

            for action in legalActs:
                score = self.minimax(game_state.generateSuccessor(0, action), depth, agent_index + 1)
                bestScore = max(bestScore, score)

            return bestScore

        else:
            bestScore = float("inf")
            legalActs = game_state.getLegalActions(agent_index)

            for action in legalActs:
                if agent_index == game_state.getNumAgents() - 1:
                    score = self.minimax(game_state.generateSuccessor(agent_index, action), depth - 1, 0)
                else:
                    score = self.minimax(game_state.generateSuccessor(agent_index, action), depth, agent_index + 1)
                bestScore = min(bestScore, score)

            return bestScore

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        infinity = float('inf')  # Set Infinity to represent positive infinity.

        def minValue(state, agentInd, depth, a, b):
            # Minimize agent's evaluation function.
            legalActions = state.getLegalActions(agentInd)
            if not legalActions:
                return self.evaluationFunction(state)  # If no legal actions, return evaluation.

            v = infinity  # Initialize v to positive infinity.
            for action in legalActions:
                newState = state.generateSuccessor(agentInd, action)

                # If the last ghost, call maxValue; otherwise, continue with minValue.
                if agentInd == state.getNumAgents() - 1:
                    newValue = maxValue(newState, depth, a, b)
                else:
                    newValue = minValue(newState, agentInd + 1, depth, a, b)

                v = min(v, newValue)  # Update v to the minimum of v and newV.
                if v < a:
                    return v  # Alpha-beta pruning: if v < a, return v.
                b = min(b, v)  # Update b to the minimum of b and v.
            return v

        def maxValue(state, depth, a, b):
            # Maximize agent's evaluation function (Pac-Man).
            legalActions = state.getLegalActions(0)
            if not legalActions or depth == self.depth:
                return self.evaluationFunction(state)  # If no actions or max depth, return evaluation.

            v = -infinity  # Initialize v to negative infinity.

            # For enabling second-play pruning
            if depth == 0:
                bestAction = legalActions[0]  # Initialize bestAction if depth is 0.

            for action in legalActions:
                newState = state.generateSuccessor(0, action)
                newValue = minValue(newState, 0 + 1, depth + 1, a, b)

                if newValue > v:
                    v = newValue  # Update v to the new maximum value.
                    if depth == 0:
                        bestAction = action  # Update bestAction if depth is 0.

                if v > b:
                    return v  # Alpha-beta pruning: if v > b, return v.
                a = max(a, v)  # Update a to the maximum of a and v.

            if depth == 0:
                return bestAction  # Return the best action if depth is 0.
            return v  # Return the maximum value.

        bestAction = maxValue(gameState, 0, -infinity, infinity)  # Start the search with initial values.
        return bestAction


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        numberOfGhosts = gameState.getNumAgents() - 1

        #Used only for pacman agent hence agentindex is always 0.
        def maxLevel(gameState,depth):
            #current depth is 1 as we are starting from the root.
            currDepth = depth + 1
            #terminal test
            if gameState.isWin() or gameState.isLose() or currDepth==self.depth:   #Terminal Test
                return self.evaluationFunction(gameState)
            #set the max value to infinity.
            maxvalue = -999999
            #get the legal actions for pacman.
            actions = gameState.getLegalActions(0)
            #for each action of pacman, calculate the max of the successors.
            for action in actions:
                successor= gameState.generateSuccessor(0,action)
                #calculate max of the successors.
                maxvalue = max (maxvalue,chancenodes(successor,currDepth,1))
            return maxvalue
        #For all ghosts.
        #agentIndex indicates that the ghost is at that index.
        def chancenodes(gameState,depth,agentIndex):
            if gameState.isWin() or gameState.isLose():   #Terminal Test
                return self.evaluationFunction(gameState)
            actions = gameState.getLegalActions(agentIndex)
            #initialize the variable sum to 0.
            sum = 0
            #For each action of the ghost, calculate the sum of the successors.
            for action in actions:
                successor= gameState.generateSuccessor(agentIndex,action)
                #If the ghost is the last ghost, then the next level is a max level.
                if agentIndex == (gameState.getNumAgents() - 1):
                    #Calculate the sum of the successors.
                    sum += maxLevel(successor,depth)
                else:
                    #Calculate the sum of the successors.
                    sum += chancenodes(successor,depth,agentIndex+1)
            #Return the average of the sum of the successors.
            return sum/len(actions)

        #Root level action.
        actions = gameState.getLegalActions(0)
        currentScore = -999999
        returnAction = ''
        for action in actions:
            nextState = gameState.generateSuccessor(0,action)
            # Next level is a chance node level. Hence calling chance for successors of the root.
            score = chancenodes(nextState,0,1)
            # Choosing the action which is Maximum of the successors.
            if score > currentScore:
                returnAction = action
                currentScore = score
        return returnAction


def betterEvaluationFunction(currentgame_state):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
