
# AI Practices

I created this repo so I can practice whatsoever I learned about AI theoratically within my lectures and lab and I commit my all implemetations and understanding of all the AI practices that I have learnt so far in this repo.

Here is the breakdown, working and usage of each folder inside my repo.

Enjoy learning guys!!





# Levenshtein Distance

In this section, I have implemented the levenshtein distance formula.

Levenshtein/Edit distance gives us a measure of similarity between two strings/sequences. Going by formal definition it is minimum number of single character edits required to transform one string into another.
Single character edits include:-
-	Insertion
-	Deletion
-	Substitution

## Mathematically:

Mathematically Levenshtein/Edit distance between two strings ‘a’ and ‘b’ is defined as:-



![App Screenshot](https://miro.medium.com/v2/resize:fit:720/format:webp/1*o9k-pcrM-4NUrMNAqQbH9A.png)

- Basic Implementation: It is the basic implementation of how levenshhtein distance works on characters of a word and calculates the distance between the words through the matrix

- Comparison of files: In this implementation, the files are read and instead of characters the distance formula is implemented on words

- With Skipped Words: In this implementation, I made a little change to show how this formula would workk if we have to exempt some of the words in a file. 


# Agents

Agents are important concept in AI fundamentals. An agent is a computer program or system that is designed to perceive its environment, make decisions and take actions to achieve a specific goal or set of goals

I have implemented some of the agents through examples

## Reflexive Agent

Simple reflex agents ignore the rest of the percept history and act only on the basis of the current percept. Percept history is the history of all that an agent has perceived to date. The agent function is based on the condition-action rule. A condition-action rule is a rule that maps a state i.e., a condition to an action. If the condition is true, then the action is taken, else not. 

- ### Mood Detector:
I have implemented a simple example of Simple Reflexive agent throgh a mood detector which makes it easy to understand. You just give the unput that how the percept is feeling and it will give you the its sudden action or (reaction).

## Utlity-Based Agent
The agents which are developed having their end uses as building blocks are called utility-based agents. When there are multiple possible alternatives, then to decide which one is best, utility-based agents are used. They choose actions based on a preference (utility)for each state. 

- ### Autonomous Vehicle
#### Problem Scenario: 
Within a metropolis, passengers must be transported by an autonomous vehicle. It must choose how to drive to reduce fuel use, maximize trip time, and protect passengers.

#### Agent's Goal: 
Autonomous vehicles are decided using a utility-based strategy. By changing weights for trip duration, safety, and fuel efficiency, it strikes a balance amongst the objectives.

#### Solution Method:
-	The agent determines a utility value for each action, considering travel time, safety, and fuel efficiency.
-	This information is combined with weights in a utility function. Goals can be prioritized by the agent by changing weights.
-	To maximize projected overall utility, the agent chooses the action with the highest utility.
-	The agent can modify weightings in response to shifting situations. For instance, it might put safety first when bad weather is present.
-	In each run, different situations are produced by random variables including estimated time, safety score, and fuel usage.

This strategy strives to offer effective, secure, and environmentally friendly transportation in metropolitan areas.

## Goal-Based Agent

These kinds of agents take decisions based on how far they are currently from their goal(description of desirable situations). Their every action is intended to reduce their distance from the goal. This allows the agent a way to choose among multiple possibilities, selecting the one which reaches a goal state. The knowledge that supports its decisions is represented explicitly and can be modified, which makes these agents more flexible.

- ### Delivery Bot
#### Problem Scenario: 
An intelligent agent is tasked with inventory management in a warehouse with lanes and storage shelves, which includes replenishing stock, looking for perishable goods, and organizing shelves. To handle these duties effectively, the agent uses a goal-based methodology.

#### Agent's Method for Solving Issues:

1.	Goal Setting: The agent establishes objectives, such as rearranging shelves or replenishing low-demand commodities.
2.	Monitoring: It continuously keeps track of the expiration dates and item quantities in the warehouse.
3.	Action Planning: The agent plans activities, such as finding objects, moving them, or getting rid of outdated goods, for each goal.
4.	Execution: The agent carries out premeditated activities to accomplish its objectives.
5.	Goal Achievement: It determines whether the goal's requirements are satisfied and marks goals as accomplished when they are.
6.	Adaptation: The agent adjusts to challenges or changes by changing plans and activities as necessary.
####

With this strategy, inventory is managed well, the warehouse is kept clean, and the products are always current.


