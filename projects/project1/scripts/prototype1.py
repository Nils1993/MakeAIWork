#!/usr/bin/env python
# PROJECT 1: Creating a program that can predict someone's maximum age.

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

# logging info
logging.basicConfig(level=logging.DEBUG)

# Global path
Ppath = 'projects/project1/pickle/'

# Load my model
with open(f'{Ppath}lifespan_model.pkl', 'rb') as f:
    lr = pickle.load(f)

# Create the function
def lifespan():

    """ Predict lifespan with custom input """

    life_quality = {'genetic':0, 'exercise':0, 'smoking':0, 'alcohol':0, 'sugar':0, 'bmi':0}
    
    while True:
        genetic = float(input('Enter genetic age'))
        if 50 <= genetic <= 110 and genetic.is_integer() == True:
            life_quality['genetic'] = genetic
            break
        else:
            print('Please input a whole number between 50 and 110')
            continue

    while True:
        exercise = float(input('Enter hours of excercise each day'))
        if 50 <= exercise <= 110 and exercise.is_integer() == True:
            life_quality['exercise'] = exercise
            break
        else:
            print('Please input a whole number that is either 0 or between 0 and 10')
            continue

    while True:
        smoking = float(input('Enter amount of sigarettes each day'))
        if 50 <= smoking <= 110 and smoking.is_integer() == True:
            life_quality['smoking'] = smoking
            break
        else:
            print('Please input a whole number that is either 0 or between 0 and 50')
            continue

    while True:
        alcohol = float(input('Enter glasses of alcohol each day'))
        if 50 <= alcohol <= 110 and alcohol.is_integer() == True:
            life_quality['alcohol'] = alcohol
            break
        else:
            print('Please input a whole number that is either 0 or between 0 and 20')
            continue

    while True:
        sugar = float(input('Enter amount of sugarcubes each day'))
        if 50 <= sugar <= 110 and sugar.is_integer() == True:
            life_quality['sugar'] = sugar
            break
        else:
            print('Please input a whole number that is either 0 or between 0 and 20')
            continue

    while True:
        bmi = float(input('enter bmi'))
        if 50 <= bmi <= 110 and bmi.is_integer() == True:
            life_quality['bmi'] = bmi
            break
        else:
            print('Please input a whole number between 0 and 60')
            continue

    life_quality = pd.DataFrame(data=life_quality, index=[0])

    span = lr.predict(life_quality)
    span = round(span[0], 1)

    print(f'Your predicted age IF nothing changes in your lifestyle is {span} years')

# Run the function to make the prediction
lifespan()

# logging
