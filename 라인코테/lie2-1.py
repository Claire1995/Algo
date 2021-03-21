program = "line"
flag_rules =  ["-s STRING", "-n NUMBER", "-e NULL"]
commands = ["line -n 100 -s hi -e", "lien -s Bye"]


# program = "line"
# flag_rules =  ["-s STRING", "-n NUMBER", "-e NULL"]
# commands = ["line -s 123 -n HI", "line fun"]

names = []
args = []
for row in flag_rules:
    temp = row.split()
    names.append(temp[0])
    temp.remove(temp[0])
    args.append(temp)

answer = []
for cm in commands:
    print("cm", cm)
    temp = cm.split()

    if temp[0] != program:
        answer.append(False)
        continue
    temp.remove(temp[0])

    if temp[0].startswith('-') == False:
        answer.append(False)
        continue
    string = str()
    for t in temp:
        if t.startswith('-'):
            string = string+'/'+t
        else:
            string = string + t
    row = string.split('/')

    innerFlag = False

    for i in range(1, len(row)):
        if innerFlag == True:
            break
        name = row[i][0:2]
        if name not in names:
            answer.append(False)
            break
        
        idx = names.index(name)
        arg = args[idx]
        if 'NUMBER' in str(arg) and str(row[i][2:]).isnumeric() == False:
            print("NUMBER false")
            answer.append(False)
            innerFlag = True
            break 

        elif 'STRING' in str(arg) and str(row[i][2:]).isalpha() == False:
            print("STRING false")
            answer.append(False)
            innerFlag = True
            break

    print(cm)
    if innerFlag == False:
        answer.append(True)
            
print(answer)