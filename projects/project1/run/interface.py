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
logging.basicConfig(level=logging.INFO)

# Global path
Ppath = 'projects/project1/pickle/'

# Load my model (open with pickel)
logging.info('Loading model')
with open(f'{Ppath}lifespan_model.pkl', 'rb') as f:
    lr = pickle.load(f)

# Create function to collect data and make a prediction on set data
def main():

    """ Predict lifespan with custom input """

    # Create dictionairy with required keys of value 0
    life_quality = {'genetic':0, 'exercise':0, 'smoking':0, 'alcohol':0, 'sugar':0, 'bmi':0}
    # create number of tries that the user has
    nr_of_tries = 3
    i = 0
    
    # Create while loop to fill the keys
    logging.info('Generating questions to extract data')
    while i < nr_of_tries:
        # Use try function to intercept any errors that may occur
        try: 
            genetic = float(input('Enter genetic age: '))

        # Use except function to change error message and guide the program to redo the input statement.
        except:
            # adding a try to the number of tries the user has and checking if it hasn't reached the maximum
            i+=1
            if i == nr_of_tries:
                # IF number of tries are at the maximum communicate with user and shut down the program
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                # Communicate with the user to clarify the input needed and try again
                print('Please enter a number')
                continue

        # Give reasonable parameters for the users to input the data and check if the input is correct
        if 50 <= genetic <= 110:
            life_quality['genetic'] = round(genetic, 1)
            break
    
        # If wrong input, repeat the process for the exept function
        else:
            i+=1
            if i == nr_of_tries:
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                print('Please input a number between 50 and 110')
                continue
    logging.debug(life_quality['genetic'])


    # Repeat steps for excercise
    i = 0
    while i < nr_of_tries:
        try:
            exercise = float(input('Enter hours of excercise each day: '))
        except:
            i+=1
            if i == nr_of_tries:
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                print('Please enter a number')
                continue

        if 0 <= exercise <= 10:
            life_quality['exercise'] = round(exercise, 1)
            break
        else:
            i+=1
            if i == nr_of_tries:
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                print('Please input a number that is either 0 or between 0 and 10')
            continue
    logging.debug(life_quality['exercise'])

    # Repeat steps for sigarettes
    i = 0
    while i < nr_of_tries:
        try:
            smoking = float(input('Enter amount of sigarettes each day: '))
        except:
            i+=1
            if i == nr_of_tries:
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                print('Please enter a number')
                continue
    
        if 0 <= smoking <= 50 and smoking.is_integer() == True:
            life_quality['smoking'] = smoking
            break
        else:
            i+=1
            if i == nr_of_tries:
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                print('Please input a whole number that is either 0 or between 0 and 50')
                continue
    logging.debug(life_quality['smoking'])

    # Repeat steps for alcohol
    i = 0
    while i < nr_of_tries:
        try:
            alcohol = float(input('Enter glasses of alcohol each day: '))
        except:
            i+=1
            if i == nr_of_tries:
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                print('Please enter a number')
                continue

        if 0 <= alcohol <= 20 and alcohol.is_integer() == True:
            life_quality['alcohol'] = alcohol
            break
        else:
            i+=1
            if i == nr_of_tries:
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                print('Please input a whole number that is either 0 or between 0 and 20')
                continue
    logging.debug(life_quality['alcohol'])

    # Repeat steps for sugar
    i = 0
    while i < nr_of_tries:
        try:
            sugar = float(input('Enter amount of sugarcubes each day: '))
        except:
            i+=1
            if i == nr_of_tries:
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                print('Please enter a number')
                continue

        if 0 <= sugar <= 20 and sugar.is_integer() == True:
            life_quality['sugar'] = sugar
            break
        else:
            i+=1
            if i == nr_of_tries:
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                print('Please input a whole number that is either 0 or between 0 and 20')
                continue
    logging.debug(life_quality['sugar'])

    # Repeat steps, but put length in variable for later use (bmi calculation)
    i = 0
    while i < nr_of_tries:
        try:
            length_question = float(input('Enter your height in cm: '))
        except:
            i+=1
            if i == nr_of_tries:
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                print('Please enter a number')
                continue

        if 130 <= length_question <= 220:
            length = round(length_question, 1)
            break
        else:
            i+=1
            if i == nr_of_tries:
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                print('Please input a number between 130 and 220')
                continue
    logging.debug(length)

    # Repeat steps, but put mass in variable for later use (bmi calculation)
    i = 0
    while i < nr_of_tries:
        try:
            mass_question = float(input('Enter your weight in kg: '))
        except:
            i+=1
            if i == nr_of_tries:
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                print('Please enter a number')
                continue

        if 40 <= mass_question <= 250:
            mass = round(mass_question, 2)
            break
        else:
            i+=1
            if i == nr_of_tries:
                print('A wrong input was given to many times. Please try again and check your inputs carefully')
                logging.info('No more tries left, shutting down...')
                exit()
            else:
                print('Please input a number between 40 and 250')
                continue
    logging.debug(mass)

    # Calculate bmi and put it in the bmi key
    logging.info('Calculating bmi')
    life_quality['bmi'] = round(mass / (length/100)**2, 2)
    print(f'Your BMI is: ', life_quality['bmi'])
    logging.debug(life_quality['bmi'])

    # Convert to dataframe using pandas
    logging.info('Converting to dataframe')
    life_quality = pd.DataFrame(data=life_quality, index=[0])
    logging.debug(life_quality.head())

    # Predict lifespan using our model we saved with pickle
    logging.info('Making a prediction based on the dataframe')
    span = lr.predict(life_quality)

    # Put it into a variable for easy acces and round to 1 decimal
    span = round(span[0], 1)
    logging.debug(span)

    # Print the prediction
    print(f'Your predicted lifespan IF nothing changes in your lifestyle is:\n{span} years')

# Run the function to make the prediction
main()
