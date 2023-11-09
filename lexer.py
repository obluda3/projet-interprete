# idees pour l'analyse lexicale
['add', 'div', 'mult', 2, 241432, 3, 221421421]

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
            op.append(int(s[numStart:i]))
            numStart = i+1
    op.append(int(s[numStart:len(s)]))
    cnt = 0
    for a in op:
        if a in operations.values():
            cnt += 1
        else:
            break
    print(op)
    for i in range(cnt-1, 0, -1):
        a = op[i:i+3]
        op.pop(i+2)
        op.pop(i+1)
        op.pop(i)
        op.insert(i, a)
    return op

def parse_opPrio(line):
    operations = {
        "=":"add",
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

def analyse(line):
    line.remove(" ")
    statements = ["if", "while", ]
    res = []
    if ":" in line:
        var = line[0:line.index(":")]
        val = line[line.index(":")+1:]
        res.append("set")
        res.append(var)
        res.append(analyse_arith(val))
        print(res)

    
print(parse_opPrio("421*21<421*13"))