from interprete import *
from lexique import *
import sys
def main(path):
    with open(path,encoding = 'utf-8') as file: 
        code = analyse(file.readlines())
    test = interprete()
    test.exec_sequence(code)   
 
if __name__== '__main__' :
    if len(sys.argv) < 2:
        print("Veuillez spécifier le chemin du programme a exécuter.")
    else:
        main(sys.argv[1])
