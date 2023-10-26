

def eval(operand):
    if type(operand) == int:
        return operand
    if type(operand) == str:
        return variables[operand]
    return exec_inst(operand)

def add(operands):
    return eval(operands[0]) + eval(operands[1])

def minus(operands):
    return eval(operands[0]) - eval(operands[1])

def times(operands):
    return eval(operands[0]) * eval(operands[1])

def div(operands):
    return eval(operands[0]) // eval(operands[1])

def exec_inst(instruction):
    inst = instruction[0]
    f = d[inst]
    return f(instruction[1:])

def exec_sequence(seq):
    for line in seq[1:]:
        exec_inst(line)

def while_sequence(args):
    cond = args[0]
    seq = args[1]
    while eval(cond):
        exec_sequence(seq)

def if_sequence(args):
    cond = args[0]
    seq = args[1]
    if eval(cond):
        exec_sequence(seq)

def set_variable(args):
    name = args[0]
    value = eval(args[1])
    variables[name] = value

def more_cond(args):
    return eval(args[0]) > eval(args[1])

def less_cond(args):
    return eval(args[0]) < eval(args[1])

def equal_cond(args):
    return eval(args[0]) == eval(args[1])

def output_value(args):
    print(eval(args[0]))

d = { 
    "add": add,
    "minus": minus,
    "div": div,
    "mult": times,
    "while": while_sequence,
    "if": if_sequence,
    "set": set_variable,
    "output": output_value,
    "more": more_cond,
    "equal": equal_cond,
    "less": less_cond
}

variables = {}
code = ["sequence", 
        ["set", "i", 500000],
        ["set", "fizz", 100000],
        ["if", ["less", ["div", "i", 1000], "fizz"], ["sequence", ["output", "i"]]]
    ]

exec_sequence(code)