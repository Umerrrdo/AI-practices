import random

class AutonomousVehicle:
    def __init__(self, weight_time, weight_safety, weight_fuel):
        self.timeWeigth = weight_time
        self.safetyWeigth = weight_safety
        self.fuelWeight = weight_fuel

    def utilityFunction(self, action):
        travel_time_utility = self.calculateTravelTimeUtility(action)
        safety_utility = self.calculateSafetyUtility(action)
        fuel_utility = self.calculateFuelUtility(action)
        totalUtility = (
            self.timeWeigth * travel_time_utility +
            self.safetyWeigth * safety_utility +
            self.fuelWeight * fuel_utility
        )

        return totalUtility

    def calculateTravelTimeUtility(self, action):
        # The higher the estimated time, the lower the utility
        return 1.0 / (estimatedTime(action) + 1)

    def calculateSafetyUtility(self, action):
        # The higher the safety score, the higher the utility
        return safetyScore(action)

    def calculateFuelUtility(self, action):
        # The higher the fuel consumption, the lower the utility
        return 1.0 / (fuelConsumption(action) + 1)

    def chooseAction(self, available_actions):
        max=0
        for action in available_actions:
            if self.utilityFunction(action) > max:
                max = self.utilityFunction(action)
                chosenAction = action
        return chosenAction

def estimatedTime(action):
    return random.uniform(10, 60)

def safetyScore(action):
    return random.uniform(0.0, 1.0)

def fuelConsumption(action):
    return random.uniform(0.1, 2.0)

def main():
    # Input weights for time, safety, and fuel
    weight_time_input = 0.6
    weight_safety_input = 0.3
    weight_fuel_input = 0.1

    autonomous_vehicle = AutonomousVehicle(weight_time_input, weight_safety_input, weight_fuel_input)
    availableActions = ["Action1", "Action2", "Action3"]
    for action in availableActions:
        utility = autonomous_vehicle.utilityFunction(action)
        print(f"Action: {action}, Utility: {utility}")
    chosen_action = autonomous_vehicle.chooseAction(availableActions)
    print(f"The autonomous vehicle chooses action: {chosen_action}")

main()
