# Log all the execution in this file to handle error, custom exception 
import logging
import os 
from datetime import datetime 

# Text file created with this naming convention
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Every file name should start with logs
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format   = "[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level    = logging.INFO,
)

# Create a logger instance for this module
logger = logging.getLogger(__name__)


# if __name__ == "__main__":
#     logging.info("Logging has started")