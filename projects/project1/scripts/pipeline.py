#!/usr/bin/env python

# Installing libraries
import logging
import sqlite3
import pandas as pd

# LOG LEVELS
# DEBUG		Detailed information, useful during bugfixing
# INFO		Just enough information to be able to understand the flow
# WARNING	Information about unexpected conditions that might be solved later
# ERROR		Reporting that the program can perform some task
# CRITICAL	Reporting that the program can not continue

# Global variables
logging.basicConfig(level=logging.DEBUG)

dbPath = "projects/project1/database/"
tablename = 'rest_api_netlify'



# Collecting the data
logging.info("Loading data from the database and converting to dataframe")

# Specify the connection
con = sqlite3.connect(f'{dbPath}db.sqlite3')
# Convert to DataFrame
df = pd.read_sql(f'SELECT * FROM {tablename}', con=con)
# Remove unwanted column
df = df.drop('id', axis=1)

logging.debug(df.head())


# Remove missing values (if there are any)
logging.info('Removing potential null-values')

df = df.dropna()

logging.debug(df.isnull().sum())


# Remove duplicates (if there are any)
logging.info('Removing potential duplicates')

df = df.drop_duplicates()
duplicate_rows_df = df[df.duplicated()]

logging.debug(f'Amount of duplicate rows per column:{duplicate_rows_df.shape}')


# Add a new column called BMI
logging.info('Converting columns length and mass to bmi')


for i in df['length']:
    if i > 0:
        df['bmi'] = round(df['mass'] / (df['length']/100)**2, 2)
    else:
        None

# Remove the columns that now make up the bmi column
df = df.drop(columns=['length','mass'])

logging.debug(df.head())


# Remove outliers
logging.info('Calculating IQR and creating second dataframe without outliers')

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df2 = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]

logging.debug(f'Second dataframe: {df2.describe()}')


# Save df and df2(without outliers) as new tables into the database
logging.info('Saving both dataframes as new tables into the database')
df.to_sql('clean', con=con, index=False, if_exists='replace')

df2.to_sql('iqr', con=con, index=False, if_exists='replace')

logging.info('Data has been transformed and saved for further use')




# close Connection
logging.info('Closing connection to database')
con.close()



