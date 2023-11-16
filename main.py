from interprete import *
def main():
    code =  [["func", "fibo", 
                [
                    ["if", ["equal", "n", 0], [["return", 0]]],
                    ["if", ["equal", "n", 1], [["return", 1]]],
                    ["set", "a", ["call", "fibo", [["n", ["minus", "n", 1]]]]],
                    ["set", "b", ["call", "fibo", [["n", ["minus", "n", 2]]]]],
                    ["return", ["add", "b", "a"]],
                ]
            ],
            ["output", ["call", "fibo", [["n", 10]]]]]

    test = interprete()
    #with open("shell",encoding = 'utf-8') as file: 
    test.exec_sequence(code)

if __name__== '__main__' :
    main()




