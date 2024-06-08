from src.mlpathlearn.logger import logging
from src.mlpathlearn.exception import CustomException
from src.mlpathlearn.components.data_ingestion import DataIngestion
from src.mlpathlearn.components.data_ingestion import DataIngestionConfig
import sys




if __name__=="__main__":
    logging.info("The excution started")
    
    try:
        ##data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
   
    except Exception as e:
        logging.info("custom Exception")
        raise CustomException(e,sys)