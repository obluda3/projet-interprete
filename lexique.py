def parseNumOrVar(s):
    try:
        return int(s)
    except:
        if s == "input":
            return ["input"]
        return s

def analyse_arith(s):
    op = []
    operations = {
        "+":"add",
        "*":"mult",
        "/":"div",
        "-":"minus",
    }
    numStart = 0
    for i in range(len(s)):
        c = s[i]
        if c in operations.keys():
            op.insert(0, operations[c])
            op.append(parseNumOrVar(s[numStart:i]))
            numStart = i+1

    op.append(parseNumOrVar(s[numStart:len(s)]))
    cnt = 0
    for a in op:
        if a in operations.values():
            cnt += 1
        else:
            break
    for i in range(cnt-1, 0, -1):
        a = op[i:i+3]
        op.pop(i+2)
        op.pop(i+1)
        op.pop(i)
        op.insert(i, a)
    if len(op) == 1:
        return op[0]
    return op

def parse_opPrio(line):
    operations = {
        "=":"equal",
        ">":"more",
        "<":"less",
    }
    operator = ""
    for op in operations:
        if op in line:
            operator = op
            break
    left = line[0:line.index(operator)]
    right = line[line.index(operator)+1:]
    return [operations[operator], analyse_arith(left), analyse_arith(right)]

def getBlockLines(lines, ind, expr):
    result = []
    for j in range(len(lines)):
        if ind+expr in lines[j]:
             return result, j
        result.append(lines[j])

def analyse(lines):
    res = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if "#" in line:
            line = line[0:line.index("#")]
        line = line.strip()

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
                valid = False
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
                valid = False
            if valid:
                cond = parse_opPrio(line[line.index("while")+6:])
                temp.append("while")
                temp.append(cond)
                scope, blockLen = getBlockLines(lines[i+1:], ind, "endw")
                out = analyse(scope)
                temp.append(out)
            i += blockLen + 1
        
        if "func" in line:
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


# [if,[cond],[sequence]]

#print(analyse("1if 421*2421*13 = 2 1endif"))
