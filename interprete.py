class interprete:
    def __init__(self):
        self.op  = { 
                    "add": self.add,
                    "minus": self.minus,
                    "div": self.div,
                    "mult": self.times,
                    "while": self.while_sequence,
                    "if": self.if_sequence,
                    "set": self.set_variable,
                    "output": self.output_value,
                    "more": self.more_cond,
                    "equal": self.equal_cond,
                    "less": self.less_cond,
                    "call": self.call,
                    "func": self.func,
                }
        self.variables = {}
        self.functions = {}
    
    def eval(self,operand):
        if type(operand) == int:
            return operand
        if type(operand) == str:
            return self.variables[operand]
        return self.exec_inst(operand)

    def add(self,operands):
        return self.eval(operands[0]) + self.eval(operands[1])

    def minus(self,operands):
        return self.eval(operands[0]) - self.eval(operands[1])

    def call(self, operands):
        self.exec_sequence(self.functions[operands[0]])
    
    def func(self, operands):
        self.functions[operands[0]] = operands[1]

    def times(self,operands):
        return self.eval(operands[0]) * self.eval(operands[1])

    def div(self,operands):
        return self.eval(operands[0]) // self.eval(operands[1])

    def exec_inst(self,instruction):
        inst = instruction[0]
        f = self.op[inst]
        return f(instruction[1:])

    def exec_sequence(self,seq):
        for line in seq:
            self.exec_inst(line)

    def while_sequence(self,args):
        cond = args[0]
        seq = args[1]
        while self.eval(cond):
            self.exec_sequence(seq)

    def if_sequence(self,args):
        cond = args[0]
        seq = args[1]
        if self.eval(cond):
            self.exec_sequence(seq)

    def set_variable(self,args):
        name = args[0]
        value = self.eval(args[1])
        self.variables[name] = value

    def more_cond(self,args):
        return self.eval(args[0]) > self.eval(args[1])

    def less_cond(self,args):
        return self.eval(args[0]) < self.eval(args[1])

    def equal_cond(self,args):
        return self.eval(args[0]) == self.eval(args[1])

    def output_value(self,args):
        print(self.eval(args[0]))

