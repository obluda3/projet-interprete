# idees pour l'analyse lexicale
s = "221421421+241432*2/3"
['add', 'div', 'mult', 2, 241432, 3, 221421421]
op = []
d = 0
operations = {
    "+":"add",
    "*":"mult",
    "/":"div",
    "-":"minus"
}
for i in range(len(s)):
    c = s[i]
    if c in "+*/-":
        op.insert(0, operations[c])
        op.append(int(s[d:i]))
        d = i+1
op.append(int(s[d:len(s)]))

result = []
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
    print(op)
    