# program = "line"
# flag_rules =  ["-s STRING", "-n NUMBER", "-e NULL"]
# commands = ["line -n 100 -s hi -e", "lien -s Bye"]

program = "line"
flag_rules =  ["-s STRING", "-n NUMBER", "-e NULL"]
commands = ["line -s 123 -n HI", "line fun"]

# program = "line"
# flag_rules =  	["-s STRINGS", "-n NUMBERS", "-e NULL"]
# commands = ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]


# program = "trip"
# flag_rules =  	["-days NUMBERS", "-dest STRING"]
# commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]


names = []
args = []
for row in flag_rules:
    temp = row.split()
    names.append(temp[0])
    temp.remove(temp[0])
    args.append(temp)

answer = []
for cm in commands:
    print("cm: ", cm)
    temp = cm.split()

    if temp[0] != program:
        print("program false")
        answer.append(False)
        continue
    temp.remove(temp[0])

    if temp[0].startswith('-') == False:
        print("- false")
        answer.append(False)
        continue
    string = str()

    for t in temp:
        if t.startswith('-'):
            string = string+'/'+t
        else:
            string = string + '*'+ t
    row = string.split('/')

    innerFlag = False

    for i in range(1, len(row)):
        if innerFlag == True:
            break
        temp = row[i].split('*')
        name = temp[0]
        if name not in names:
            answer.append(False)
            innerFlag = True
            break
        
        idx = names.index(name)
        arg = args[idx]

        temp.remove(temp[0])
        vals = temp
        print("arg : ", arg)
        print("vals: ", vals)
        print(arg)
        for j in range(len(vals)):
            if 'NUMBER' == arg[0] and (len(vals)>=2 or vals[j].isnumeric() == False):
                print("?? false")
                answer.append(False)
                innerFlag = True
                break 

            elif 'STRING' == arg[0] and (len(vals)>=2 or str(vals[j]).isalpha() == False):
                print("STRING false")
                answer.append(False)
                innerFlag = True
                break

            elif 'NUMBERS' == arg[0] and (len(vals)<1 or vals[j].isnumeric() == False):
                print("NUMBERS false")
                answer.append(False)
                innerFlag = True
                break

            elif 'STRINGS' == str(arg) and (len(vals)<1 or str(vals[j]).isalpha() == False):
                print("STRINGS false")
                answer.append(False)
                innerFlag = True
                break

    print(cm)
    if innerFlag == False:
        answer.append(True)
            
print(answer)