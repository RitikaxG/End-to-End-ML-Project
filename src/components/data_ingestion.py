# Code related to reading the data
import os 
import sys 

from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split

from dataclasses import dataclass 
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig



# Get the current directory of this script
current_dir = os.path.dirname(os.path.realpath(__file__))
# Add the 'src' directory to the Python path
src_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(src_dir)


# enables us to directly define our class variable
@dataclass
class DataIngestionConfig:
    # Data Ingestion component will save all the output in this path
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path : str = os.path.join('artifacts','test.csv')
    raw_data_path  : str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        # Consists of 3 values train,test,raw data_path
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)


            logging.info('Train test split initiated')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of the data is completed')

            return(
                # Required for data transformation
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException

if __name__ == '__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)




