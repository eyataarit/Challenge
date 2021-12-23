import pandas as pd 
from sqlalchemy import create_engine 

df = pd.read_excel('../Book.xlsx')
#print(df.head())
#this will show the excel file rows in the console

DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
                                    user='root', password='', server='localhost', database='usersdb')

engine = create_engine(DATABSE_URI)
df.to_sql('users', con =engine)
#create table users thanks to the excel file
