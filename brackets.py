s = input()

round = 0
curly = 0
square = 0

for i in s:
    if i == '(':
        round += 1
    if i == '{':
        curly += 1
    if i == '[':
        square += 1

    if i == ')':
        round -= 1
    if i == '}':
        curly -= 1
    if i == ']':
        square -= 1

if curly == 0 and square == 0 and round == 0:
    print(True)
else:
    print(False)