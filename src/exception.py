import sys # any exception that is controlled, then sys library will contain that information
import logging

def error_message_detail(error,error_detail:sys): # custom exception message, error detail is inside sys library
    _,_, exc_tb = error_detail.exc_info() # tells on which file,on which line number error has occured during execution
    file_name = exc_tb.tb_frame.f_code.co_filename
    # error_message = "error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    #     file_name,exc_tb.tb_lineno,str(error)
    # )
    error_message = f"Error occurred in Python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{error}]"

    return error_message

class CustomException(Exception): # this is custom exception class which inherit from Exception class
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message) # since we are inheriting from exception so we need to inherit init fun
        self.error_message = error_message_detail(error_message,error_detail = error_details) # function will return error message detail

    def __str__(self): # whenever we try to print we will get all the error message
        return self.error_message
    
# ----------------------------------------------------------------
# this is for only checking purpose
if __name__ == '__main__': 
    try:
        a = 1/0
    except Exception as e:
        logging.info("divide by zero error message")
        raise CustomException(e,sys)
# ----------------------------------------------------------------