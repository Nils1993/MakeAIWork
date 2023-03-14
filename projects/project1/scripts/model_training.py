#!/usr/bin/env python

# installing libraries
import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import sqlite3
import pickle

# LOG LEVELS
# DEBUG		Detailed information, useful during bugfixing
# INFO		Just enough information to be able to understand the flow
# WARNING	Information about unexpected conditions that might be solved later
# ERROR		Reporting that the program can perform some task
# CRITICAL	Reporting that the program can not continue

# Global variables
logging.basicConfig(level=logging.DEBUG)

# Global variables
dbPath = 'projects/project1/database/'
Ppath = 'projects/project1/pickle/'
tablename = 'iqr'


# Collecting the data
logging.info('Collecting the data from the database and converting it to a dataframe')
# Specify the connection
con = sqlite3.connect(f'{dbPath}db.sqlite3')
# Convert to DataFrame
df = pd.read_sql(f'SELECT * FROM {tablename}', con=con)
logging.debug(df.head())


# create x and y
logging.info('Creating x (all columns without lifespan) and y (lifespan)')
x = df.drop(columns='lifespan')
y = df['lifespan']
logging.debug(x.head(), y.head())


# split the data 30%(test) - 70%(train)
logging.info('Splitting the data for training and testing')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)


# apply linear regression
logging.info('Applying linear regression and fitting the data')
lr = LinearRegression()


# fit the training data
lr.fit(x_train, y_train)


# train the model
logging.info('Training model')
y_pred_train = lr.predict(x_train)
logging.debug(y_pred_train)
logging.info(f'Scoring model: {r2_score(y_train, y_pred_train)}')


# test the model with the testing data
logging.info('Testing model with the testing data')
y_pred_test = lr.predict(x_test)
logging.debug(y_pred_test)
logging.info(f'Scoring model: {r2_score(y_test, y_pred_test)}')


# save model using pickle
logging.info('Saving model')
with open(f'{Ppath}lifespan_model.pkl', 'wb') as f:
    pickle.dump(lr, f)
logging.info(f'Model trained and saved at {Ppath}lifespan_model.pkl')


# close connection
logging.info('Closing connection')
con.close()