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

# logging info
logging.basicConfig(level=logging.DEBUG)

# Global variables
dbPath = "../database"

# Collecting the data
# Specify the con
con = sqlite3.connect(f'{dbPath}/db.sqlite3')
# Convert to DataFrame
df = pd.read_sql('SELECT * FROM rest_api_netlify', con=con)
# Remove unwanted column
df = df.drop('id', axis=1)


# Remove missing values (if there are any)
df = df.dropna()


# Remove duplicates (if there are any)
df = df.drop_duplicates()
# Add a new column called BMI
df['bmi'] = round(df['mass'] / (df['length']/100)**2, 2)
# Remove the columns that now make up the bmi column
df = df.drop(columns=['length','mass'])


# Remove outliers
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(Q1)
print()
print(Q3)
print()
print(IQR)
df2 = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]


# Save df and df2(without outliers) as new databases
df.to_sql('clean', con=con, index=False, if_exists='replace')

df2.to_sql('iqr', con=con, index=False, if_exists='replace')


logging.info("Logging to file..")


# close Connection
con.close()



