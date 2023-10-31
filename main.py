from interprete import *
def main():
    code =  ["sequence", 
            ["set", "i", 500],
            ["set", "fizz", 100],
            ["if", ["less", ["div", "i", 1000], "fizz"], 
                ["sequence", ["output", "i"]]]
            ]
    test = interprete()
    #with open("shell",encoding = 'utf-8') as file: 
    test.exec_sequence(code)

if __name__== '__main__' :
    main()




