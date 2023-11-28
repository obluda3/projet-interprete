from interprete import *
from lexique import *

def main():
    with open("code.txt",encoding = 'utf-8') as file: 
        code = analyse(file.readlines())
    test = interprete()
    test.exec_sequence(code)   
 
if __name__== '__main__' :
    main()
