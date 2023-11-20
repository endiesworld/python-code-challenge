import logging

import os

# Get the current directory where the script is located
current_directory = os.path.dirname(__file__)

# Specify the relative path to your file
filename = 'output.log'  # Change to your database file name

# Combine the current directory and the relative path to create the full path
complete_file_path = os.path.join(current_directory, filename)

def my_function():
    logging.debug('This is a debug-level function', extra=ext_data)

ext_data = {
    'user': 'endiesworld@gmail.com',
}

def main():
    
    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s: Line: %(lineno)d %(message)s"
    
    datestr = "%d/%m/%Y %H:%M:%S %p"
    # The default mode for writing to the log file is 'append', which could be changed
    logging.basicConfig(level=logging.DEBUG, 
                        filename=complete_file_path,
                        filemode='w',
                        format=fmtstr,
                        datefmt=datestr)
    
    logging.debug('This is a debug message', extra=ext_data)
    logging.info('This is an info message', extra=ext_data)
    logging.warning('This is a warning message', extra=ext_data)
    logging.error('This is an error message', extra=ext_data)
    logging.critical('This is a critical message', extra=ext_data)
    my_function()
    

if __name__ == '__main__':
    main()