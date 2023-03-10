# Installing libraries
import logging
import sqlite3
import pandas as pd


# Global variables
dbPath = "../database"

# Collecting the data
# Specify the con
con = sqlite3.connect(f'{dbPath}/db.sqlite3')
# Convert to DataFrame
df = pd.read_sql('SELECT * FROM rest_api_netlify', con=con)





# transform





# Save df as new table
df.to_sql('new_table', con=con, index=False)

# close Connection
con.close()