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
                    "return": self.exit,
                    }
        self.stacks = [{}]
        self.functions = {}
        self.returnval = 0
        self.shouldReturn = False
    
    def eval(self,operand):
        if type(operand) == int:
            return operand
        if type(operand) == str:
            if operand == "rval":
                return self.returnval
            return self.stacks[-1][operand]
        
        return self.exec_inst(operand)

    def add(self,operands):
        return self.eval(operands[0]) + self.eval(operands[1])

    def minus(self,operands):
        return self.eval(operands[0]) - self.eval(operands[1])

    def call(self, operands):
        vars = {}
        args = operands[1]
        for i in range(len(args)):
            vars["arg"+str(i)] = self.eval(args[i])
        self.exec_sequence(self.functions[operands[0]], vars, True)
        return self.returnval;

    def exit(self, operands):
        self.returnval = self.eval(operands[0]);
    
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

    def exec_sequence(self, seq, vars = {}, func = False):
        # Mise en place des paramètres de la fonction
        if func:
            self.stacks.append(vars)
        
        for line in seq:
            if self.shouldReturn:
                self.shouldReturn = not func # il faut continuer de return tant qu'on est dans notre fonction (si on est dans un if, ou un while, func = False)
                break
            self.exec_inst(line)
            if line[0] == "return":
                self.shouldReturn = True

        if self.shouldReturn:
            self.shouldReturn = not func

        if func:
            self.stacks.pop()
            
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
        self.stacks[-1][name] = value

    def more_cond(self,args):
        return self.eval(args[0]) > self.eval(args[1])

    def less_cond(self,args):
        return self.eval(args[0]) < self.eval(args[1])

    def equal_cond(self,args):
        return self.eval(args[0]) == self.eval(args[1])

    def output_value(self,args):
        print(self.eval(args[0]))

