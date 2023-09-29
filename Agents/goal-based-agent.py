#A delivery bot is a very good example of showing that
#how a goal-based agent works


class DeliveryRobot:
    def __init__(self, initial_location):
        self.location = initial_location
        self.goals = []

    def setGoal(self, goalLoaction):
        self.goals.append(goalLoaction)

    def is_goalAchieved(self, goalLoaction):
        return goalLoaction == self.location

    def move_to(self, destination):
        self.location = destination

    def planAction(self, goalLoaction):
        current_x, current_y = self.location
        goal_x, goal_y = goalLoaction

        if current_x < goal_x:
            return (current_x + 1, current_y)
        elif current_x > goal_x:
            return (current_x - 1, current_y)
        elif current_y < goal_y:
            return (current_x, current_y + 1)
        elif current_y > goal_y:
            return (current_x, current_y - 1)
        else:
            return self.location

    def deliver_packages(self):
        if not self.goals:
            print("No delivery goals set.")
            return

        while self.goals:
            goalLoaction = self.goals[0]

            while not self.is_goalAchieved(goalLoaction):
                next_location = self.planAction(goalLoaction)
                self.move_to(next_location)

                print(f"Delivering to {goalLoaction}. Current location: {self.location}")

            print(f"Package delivered to {goalLoaction}.")
            self.goals.pop(0)

def main():
    robot = DeliveryRobot(initial_location=(0, 0))
    robot.setGoal((2, 3))
    robot.setGoal((1, 1))

    robot.deliver_packages()
