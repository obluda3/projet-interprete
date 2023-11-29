def parseNumOrVar(s):
    try:
        return int(s)
    except:
        if s == "input":
            return ["input"]
        return s

def analyse_arith(s):
    res = []
    operations = {
        "+":"add",
        "*":"mult",
        "/":"div",
        "-":"minus",
    }
    s = s.replace(" ", "")
    operand = ""

    N = len(s)
    i = N - 1
    while i > -1:
        c = s[i]
        if c in operations.keys():
            res.append(operations[c])
            res.append(analyse_arith(s[0:i]))
            res.append(parseNumOrVar(operand[::-1]))
            operand = ""
            break
        else:
            operand += c
        i -= 1
    if operand != "":
        return parseNumOrVar(operand[::-1])
    return res

def parse_opPrio(line):
    operations = {
        "=":"equal",
        ">":"more",
        "<":"less",
    }
    line = line.replace(" ", "")
    operator = ""
    for op in operations:
        if op in line:
            operator = op
            break
    if operator == "":
        raise Exception("No logical operator found in test: \'" + line + "\'")
    left = line[0:line.index(operator)]
    right = line[line.index(operator)+1:]
    return [operations[operator], analyse_arith(left), analyse_arith(right)]

def getBlockLines(lines, ind, expr):
    result = []
    for j in range(len(lines)):
        line = sanatizeLine(lines[j])
        if line.startswith(ind+expr):
             return result, j
        result.append(lines[j])
    raise Exception("\'"+ind+expr+"\' not found.")

def sanatizeLine(line):
    if "#" in line:
        line = line[0:line.index("#")]
    line = line.strip()
    return line

def analyse(lines):
    res = []
    i = 0
    while i < len(lines):
        line = sanatizeLine(lines[i])

        temp = []
        if ":" in line:
            var = line[0:line.index(":")]
            val = line[line.index(":")+1:]
            temp.append("set")
            temp.append(var)
            temp.append(analyse_arith(val))
            
        if "output" in line:
            out = line[line.index("output")+7:]
            temp.append("output")
            temp.append(analyse_arith(out))

        if "if" in line:
            temp = []
            ind = line[0:line.index("if")]
            valid = True
            blockLen = 0
            try:
                int(ind)
            except:
                valid = ind == ""
            if valid:
                cond = parse_opPrio(line[line.index("if")+3:])
                temp.append("if")
                temp.append(cond)
                scope, blockLen = getBlockLines(lines[i+1:], ind, "endi")
                out = analyse(scope)
                temp.append(out)
            else:
                print("error line")
            i += blockLen + 1

        if "while" in line:
            ind = line[0:line.index("while")]
            valid = True
            blockLen = 0
            try:
                int(ind)
            except:
                valid = ind == ""
            if valid:
                cond = parse_opPrio(line[line.index("while")+6:])
                temp.append("while")
                temp.append(cond)
                scope, blockLen = getBlockLines(lines[i+1:], ind, "endw")
                out = analyse(scope)
                temp.append(out)
            i += blockLen + 1
        
        if "func" in line:
            splt = line[line.index("func")+5:].split()
            if len(splt) != 2:
                raise Exception("Invalid function definition: \'" + lines[i].strip() + "\'" )
            name, cnt = line[line.index("func")+5:].split()
            temp.append("func")
            temp.append(name)
            scope, blockLen = getBlockLines(lines[i+1:], "", "endf")
            out = analyse(scope)
            temp.append(out)
            temp.append(int(cnt))
            i += blockLen + 1

        if "return" in line:
            temp.append("return")
            temp.append(analyse_arith(line[line.index("return")+7:]))
        
        if "call" in line:
            line = line[line.index("call")+5:]
            name, args = line.split(" ")
            temp.append("call")
            temp.append(name)
            argList = [analyse_arith(arg) for arg in args.split(",")]
            temp.append(argList)
        
        if len(temp) > 0:
            res.append(temp)
    
        i += 1
    return res
