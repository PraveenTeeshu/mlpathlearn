import os
import sys
from src.mlpathlearn.exception import CustomException
from src.mlpathlearn.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host=os.getenv("host")
User=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Reading sql Database Started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=User,
            password=password,
            db=db
        )
        logging.info("connection Estiblished",mydb)
        df=pd.read_sql_query('Select * from student',mydb)
        print(df.head())
        
        return df
        
    except Exception as ex:
        raise CustomException(ex)