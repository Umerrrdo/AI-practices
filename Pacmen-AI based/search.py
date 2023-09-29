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
import sys
import queue

from  collections import namedtuple

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
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def whateverFirstSearch(problem, frontier):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Implement the graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    Argument:
       problem -- an obj of type SearchProblem (or a subclass of) to solve.

       frontier - The object to use for holding the frontier.  This
       dictates the type of search performed.
    Returns
       A tuple containing:
         - list of actions that reach the goal or None if goal not found
         - cost of actions or None if goal not found
         - number of items removed from the frontier
         - number of items added to the frontier.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def depthFirstSearchStats(problem):
    """
        Call whateverFirstSearch and return results that
        will respect DFS behavior.
        Returns: the 4 tuple returned by whateverFirstSearch
    """
    util.raiseNotDefined()


def depthFirstSearch(problem):
    stack = util.Stack()
    visited_nodes = set()
    stack.push((problem.getStartState(), []))
    while True:
        popped_element = stack.pop()
        node = popped_element[0]
        node_path = popped_element[1]
        if problem.isGoalState(node):
            break
        else:
            if node not in visited_nodes:
                visited_nodes.add(node)
                successors = problem.getSuccessors(node)
                for successor in successors:
                    child_node = successor[0]
                    child_path = successor[1]
                    full_path = node_path + [child_path]
                    stack.push((child_node, full_path))
    return node_path


def breadthFirstSearchStats(problem):
    """ Search the shallowest nodes in the search tree first.
        Returns: the 4 tuple returned by whateverFirstSearch
    """

    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    q = util.Queue()
    visited_nodes = set()
    q.push((problem.getStartState(), []))
    while True:
        popped_element = q.pop()
        node = popped_element[0]
        path_till_node = popped_element[1]
        if problem.isGoalState(node):
            break
        else:
            if node not in visited_nodes:
                visited_nodes.add(node)
                successors = problem.getSuccessors(node)
                for successor in successors:
                    c_node = successor[0]
                    c_path = successor[1]
                    full_path = path_till_node + [c_path]
                    q.push((c_node, full_path))

    return path_till_node

def uniformCostSearchStats(problem):
    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return uniformCostSearchStats(problem)[0]


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearchStats(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def aStarSearch(problem, heuristic=nullHeuristic):
    """ Do not change this function"""
    return aStarSearchStats(problem, heuristic)[0]

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
