import sys
import re


def open_stock(path, filename, stock_code):
    # check date format
    pattern = "[12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])"
    match re.match(pattern, filename)
    if match:
        print("Match: ", filename)
    else:
        print("Invalid file name!:.")
    
    
    
    
    
if __name__ == __main__: # only executes when this file runs
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))
    filename = sys.argv[1]
    path = "
    open_stock()
    