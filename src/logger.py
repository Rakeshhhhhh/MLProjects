# it is for any execution that occurs, we should log all those information in some file so that we will be able to track if there is any error

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # log file will save like this format
log_path = os.path.join(os.getcwd(), 'log', LOG_FILE)
os.makedirs(log_path,exist_ok=True) # tells even though therer is file keep on appending to log_path

# so whatever the logs get created it will with respect to current working directory and every logs folder will get created
# and every log file starts with "logs" as mentioned above

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE) # contain 

# when we want to create log and want to overwrite functionality of logging  we have to seup basic config
logging.basicConfig(
    filename= LOG_FILE_PATH, # where we want to save the log
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # what format you want to use for log
    level = logging.INFO, # for which level  
)


# ----------------------------------------------------------------
# this is for only checking purpose wheather correctly working or not
# if __name__ == "__main__": # used to test logging first
#     logging.info("Application started")
# ----------------------------------------------------------------
# ----------------------------------------------------------------