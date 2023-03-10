# PROJECT 1: Creating a program that can predict someone's maximum age.

# Installing libraries
import pickle
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load my model
with open('C:/Users/nilsm/MakeAIWork/projects/project1/pickle/lifespan_model.pkl', 'rb') as f:
    lr = pickle.load(f)

# Create the function
def lifespan():

    """ Predict lifespan with custom input """
    
    life_quality = {
        'genetic': input('Enter genetic age')
        ,
        'exercise': input('Enter hours of excercise each day')
        ,
        'smoking': input('Enter amount of sigarettes each day')
        ,
        'alcohol': input('Enter glasses of alcohol each day')
        ,
        'sugar': input('Enter amount of sugarcubes each day')
        ,
        'bmi': input('enter bmi')
    }

    life_quality = pd.DataFrame(data=life_quality, index=[0])

    span = lr.predict(life_quality)
    span = round(span[0], 1)

    print(f'Your predicted age IF nothing changes in your lifestyle is {span} years')

lifespan()