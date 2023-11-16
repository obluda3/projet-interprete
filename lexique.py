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
            try:
                op.append(int(s[numStart:i]))
            except:
                op.append(s[numStart:i])
            numStart = i+1
    try:
        op.append(int(s[numStart:len(s)]))
    except:
        op.append(s[numStart:len(s)])
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

def analyse(lines):
    res = []
    i = 0
    while i < len(lines):
        temp = []
        line = lines[i].strip()
        if ":" in line:
            var = line[0:line.index(":")]
            val = line[line.index(":")+1:]
            tmp = []
            tmp.append("set")
            tmp.append(var)
            tmp.append(analyse_arith(val))
            res.append(tmp)
        if "output" in line:
            out = line[line.index("output")+7:]
            temp.append("output")
            temp.append(analyse_arith(out))
            res.append(temp)
        
        if "input" in line:
            out = line[line.index("input")+5:]
            temp.append("input")
            temp.append(analyse_arith(out))
            res.append(temp)

        if "if" in line:
            temp = []
            ind = line[0:line.index("if")]
            valid = True
            try:
                int(ind)
            except:
                valid = False
            if valid:
                cond = parse_opPrio(line[line.index("if")+2:])
                temp.append("if")
                temp.append(cond)
                lines2 = []
                j = i+1
                while ind+"endi" not in lines[j]:
                    line = lines[j].strip()
                    lines2.append(line)
                    j += 1
                out = analyse(lines2)
                temp.append([out[0]])
            res.append(temp)
            i = j

        if "while" in line:
            ind = line[0:line.index("while")]
            valid = True
            try:
                int(ind)
            except:
                valid = False
            if valid:
                cond = parse_opPrio(line[line.index("while")+6:])
                temp.append("while")
                temp.append(cond)
                j = i+1
                lines2 = []
                while ind+"endw" not in lines[j]:
                    line = lines[j].strip()
                    lines2.append(line)
                    j += 1
                out = analyse(lines2)
                temp.append(out)
            res.append(temp)
            i = j

        i += 1
    return res


# [if,[cond],[sequence]]

#print(analyse("1if 421*2421*13 = 2 1endif"))
