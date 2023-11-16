from interprete import *
from lexique import *
def main():
    with open("shell.txt",encoding = 'utf-8') as file: 
        code = analyse(file.readlines())
    print(code)
    test = interprete()
    test.exec_sequence(code)
    
   
 
if __name__== '__main__' :
    main()




