#!/usr/bin/env python

# PROJECT 1: Creating a program that can predict someone's lifespan.

# Installing libraries
import logging
import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# LOG LEVELS
# DEBUG		Detailed information, useful during bugfixing
# INFO		Just enough information to be able to understand the flow
# WARNING	Information about unexpected conditions that might be solved later
# ERROR		Reporting that the program can perform some task
# CRITICAL	Reporting that the program can not continue

# logging
logging.basicConfig(level=logging.DEBUG)

# Global path
Ppath = 'projects/project1/pickle/'

# Load my model (open with pickel)
with open(f'{Ppath}lifespan_model.pkl', 'rb') as f:
    lr = pickle.load(f)

# Create function to collect data and make a prediction on set data
def lifespan():

    """ Predict lifespan with custom input """

    # Create dictionairy with required keys of value 0
    life_quality = {'genetic':0, 'exercise':0, 'smoking':0, 'alcohol':0, 'sugar':0, 'bmi':0}
    
    # Create while true loop to fill the keys
    while True:

        # Use try function to intercept any errors that may occur
        try: 
            genetic = float(input('Enter genetic age: '))

        # Use except function to change error message and guide the program to redo the input statement
        except:
            print('Please enter a number')
            continue

        # Give reasonable parameters for the users to input the data and check if the input is correct
        if 50 <= genetic <= 110:
            life_quality['genetic'] = round(genetic, 1)
            break

        # If wrong input, give user more info on the parameters
        else:
            print('Please input a number between 50 and 110')
            continue
    logging.debug(life_quality['genetic'])

    # Repeat
    while True:
        try:
            exercise = float(input('Enter hours of excercise each day: '))
        except:
            print('Please enter a number')
            continue

        if 0 <= exercise <= 10:
            life_quality['exercise'] = round(exercise, 1)
            break
        else:
            print('Please input a number that is either 0 or between 0 and 10')
            continue
    logging.debug(life_quality['exercise'])

    # Repeat
    while True:
        try:
            smoking = float(input('Enter amount of sigarettes each day: '))
        except:
            print('Please enter a number')
            continue
    
        if 0 <= smoking <= 50 and smoking.is_integer() == True:
            life_quality['smoking'] = smoking
            break
        else:
            print('Please input a whole number that is either 0 or between 0 and 50')
            continue
    logging.debug(life_quality['smoking'])

    # Repeat
    while True:
        try:
            alcohol = float(input('Enter glasses of alcohol each day: '))
        except:
            print('Please enter a number')
            continue

        if 0 <= alcohol <= 20 and alcohol.is_integer() == True:
            life_quality['alcohol'] = alcohol
            break
        else:
            print('Please input a whole number that is either 0 or between 0 and 20')
            continue
    logging.debug(life_quality['alcohol'])

    # Repeat
    while True:
        try:
            sugar = float(input('Enter amount of sugarcubes each day: '))
        except:
            print('Please enter a number')
            continue

        if 0 <= sugar <= 20 and sugar.is_integer() == True:
            life_quality['sugar'] = sugar
            break
        else:
            print('Please input a whole number that is either 0 or between 0 and 20')
            continue
    logging.debug(life_quality['sugar'])

    # Repeat, but put length in variable for later use (bmi calculation)
    while True:
        try:
            length_question = float(input('Enter your height in cm: '))
        except:
            print('Please enter a number')
            continue

        if 130 <= length_question <= 220:
            length = round(length_question, 1)
            break
        else:
            print('Please input a number between 130 and 220')
            continue
    logging.debug(length)

    # Repeat, but put mass in variable for later use (bmi calculation)
    while True:
        try:
            mass_question = float(input('Enter your weight in kg: '))
        except:
            print('Please enter a number')
            continue

        if 40 <= mass_question <= 250:
            mass = round(mass_question, 2)
            break
        else:
            print('Please input a number between 40 and 250')
            continue
    logging.debug(mass)

    # Calculate bmi and put it in the bmi key
    life_quality['bmi'] = round(mass / (length/100)**2, 2)
    print(f'Your BMI is: ', life_quality['bmi'])
    logging.debug(life_quality['bmi'])

    # Convert to dataframe using pandas
    life_quality = pd.DataFrame(data=life_quality, index=[0])
    logging.debug(life_quality.head())

    # Predict lifespan using our model we saved with pickle
    span = lr.predict(life_quality)

    # Put it into a variable for easy acces and round to 1 decimal
    span = round(span[0], 1)
    logging.debug(span)

    # Print the prediction
    print(f'Your predicted lifespan IF nothing changes in your lifestyle is:\n{span} years')

# Run the function to make the prediction
lifespan()
