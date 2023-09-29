percepts = ['Hussain', 'Rakha', 'Afaq','Adnan','Talha']
states = ['sad', 'happy', 'angry', 'hungry', 'thirsty']
actions = ['cry', 'smile', 'yell', 'eat', 'drink']

class SimpleReflexAgent:
    def __init__(self):
        self.state = states
        self.action = actions
        self.percept = percepts


    def __getactions__(self, state):
        return self.action[state]

def main():
    agent = SimpleReflexAgent()
    print("Select a percept from the list: ")
    for x in range(len(agent.percept)):
        print(x+1, ":", agent.percept[x])
    val = int(input("Enter a percept: "))

    print("Select a state from the list: ")
    for x in range(len(agent.state)):
        print(x+1, ":", agent.state[x])
    state = int(input("Enter a state: "))
    action = agent.__getactions__(state-1)
    print("Action: ", action)

main()
