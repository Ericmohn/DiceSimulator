# Dice Simulator
# It rolls a value from 1 and 6.
import random
import PySimpleGUI as sg

class DiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.message = 'Would you like to roll the dice?'
        #Layout
        self.layout = [
            [sg.Text('Would you like to roll the dice?')],
            [sg.Button('yes'), sg.Button('no')]
        ]

    def Start(self):
        #Window
        self.window = sg.Window('Dice Simulator', layout=self.layout)
        #Read the values
        self.events, self.values = self.window.Read()
        #Use the Values
        try:
                if self.events == 'yes' or self.events == 'y' : 
                    self.RollDiceValue()
                elif self.events == 'no' or self.events == 'n' :
                    print('Goodbye!')
                else:
                    print('Please type "yes" or "no" ')
        except:
            print('There was an error while recieving your answer')
        
    def RollDiceValue(self):
        print(random.randint(self.min_value, self.max_value))

simulator = DiceSimulator()
simulator.Start()
