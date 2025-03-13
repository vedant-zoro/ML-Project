import sys 
from src.logger import logging

def error_msg(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = "error occured in script name[{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)    
    
    ) 
    return error_message


class customexcetption(Exception):
    def __inti__(self,error_message,error_detail:sys):
        super().__inti__(error_message)
        self.error_message =error_msg(error_message,error_detail=error_detail)
    

    def __str__(self):
        return self.error_message
    
    