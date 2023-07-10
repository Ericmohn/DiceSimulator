# Dice Simulator
# It rolls a value from 1 and 6.
import random

class DiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.message = 'Would you like to roll the dice?'

    def Start(self):
        answer = input(self.message)
        try:
            if answer == 'yes' or answer == 'y' : 
                self.RollDiceValue()
            elif answer == 'no' or answer == 'n' :
                print('Goodbye!')
            else:
                print('Please type "yes" or "no" ')
        except:
            print('There was an error while recieving your answer')
    
    def RollDiceValue(self):
        print(random.randint(self.min_value, self.max_value))

simulator = DiceSimulator()
simulator.Start()