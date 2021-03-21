# program = "line"
# flag_rules =  ["-s STRING", "-n NUMBER", "-e NULL"]
# commands = ["line -n 100 -s hi -e", "lien -s Bye"]

# program = "line"
# flag_rules =  ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"]
# commands = ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]

program = "line"
flag_rules =  	["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"]
commands = ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]


# program = "trip"
# flag_rules =  	["-days NUMBERS", "-dest STRING"]
# commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]


names = []
args = []
alias = dict()
for row in flag_rules:
    temp = row.split()
    if temp[1] == 'ALIAS':
        alias[temp[0]] = [temp[2], 0]
        alias[temp[2]] = [temp[0], 0]
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
        elif name in list(alias.keys()):
            if alias[name][1] == 1:
                answer.append(False)
                innerFlag = True
                break
            else:
                idx = names.index(alias[name][0])
                partner = alias[name][0]
                alias[name] = [partner, 1]
                alias[partner] = [name, 1]

        else:
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

# def solution(program, flag_rules, commands):
    
#     names = []
    # args = []
    # # alias인 flag 조회를 위한 dict
    # alias = dict()
    # for row in flag_rules:
    #     temp = row.split()
    #     if temp[1] == 'ALIAS':
    #         # dict의 value[0]은 서로의 flag 이름
    #         # dict의 value[1]은 사용 여부
    #         alias[temp[0]] = [temp[2], 0]
    #         alias[temp[2]] = [temp[0], 0]
    #     names.append(temp[0])
    #     temp.remove(temp[0])
    #     args.append(temp)

    # answer = []
    # for cm in commands:
    #     temp = cm.split()

    #     if temp[0] != program:
    #         answer.append(False)
    #         continue
    #     temp.remove(temp[0])

    #     if temp[0].startswith('-') == False:
    #         answer.append(False)
    #         continue
    #     string = str()

    #     for t in temp:
    #         if t.startswith('-'):
    #             string = string+'/'+t
    #         else:
    #             string = string + '*'+ t
    #     row = string.split('/')

    #     innerFlag = False

    #     for i in range(1, len(row)):
    #         if innerFlag == True:
    #             break
    #         temp = row[i].split('*')
    #         name = temp[0]
    #         if name not in names:
    #             answer.append(False)
    #             innerFlag = True
    #             break
    #         elif name in list(alias.keys()):
    #             if alias[name][1] == 1:
    #                 answer.append(False)
    #                 innerFlag = True
    #                 break
    #             else:
    #                 idx = names.index(alias[name][0])
    #                 partner = alias[name][0]
    #                 #alias가 있는 flag 사용 체크 - 중복 허용 안됨
    #                 alias[name] = [partner, 1]
    #                 alias[partner] = [name, 1]

    #         else:
    #             idx = names.index(name)

    #         arg = args[idx]

    #         temp.remove(temp[0])
    #         vals = temp
            
    #         for j in range(len(vals)):
    #             if 'NUMBER' == arg[0] and (len(vals)>=2 or vals[j].isnumeric() == False):
    #                 answer.append(False)
    #                 innerFlag = True
    #                 break 

    #             elif 'STRING' == arg[0] and (len(vals)>=2 or str(vals[j]).isalpha() == False):
    #                 answer.append(False)
    #                 innerFlag = True
    #                 break

    #             elif 'NUMBERS' == arg[0] and (len(vals)<1 or vals[j].isnumeric() == False):
    #                 print("NUMBERS false")
    #                 answer.append(False)
    #                 innerFlag = True
    #                 break

    #             elif 'STRINGS' == str(arg) and (len(vals)<1 or str(vals[j]).isalpha() == False):
    #                 answer.append(False)
    #                 innerFlag = True
    #                 break

    #     if innerFlag == False:
    #         answer.append(True)
            
    # return answer

    문제 설명
CLI Flag Validator - 3
주의사항: 본 문제는 2번 문제의 답안 코드를 기반으로 합니다. 만약 아직 2번 문제를 풀지 않았다면, 2번 문제를 먼저 풀어주세요.

flag에는 별칭(alias)이 있는 경우가 있습니다. 예를 들어 압축 명령어인 'tar'의 '--help'와 '-h'는 모두 도움말을 나타내는 flag입니다.

이제 별칭을 지정하는 새로운 flag_rule을 처리해야 합니다. 그 외 조건은 2번 문제와 동일하며, 변경된 조건은 굵은 글씨로 강조되어 있습니다.

2번 문제의 답안을 수정해 새로운 요구사항을 처리하세요.

입력 형식
program: string
1 <= program의 길이 <= 10
실행할 프로그램의 이름입니다.
공백처리는 하지 않아도 됩니다.
flag_rules: [flag_rule]
1 <= flag_rules의 길이 <= 100
flag_rule: "<flag_name> <flag_argument_type>" | "<flag_name_1> ALIAS <flag_name_2>"
flag_name: string
2 <= flag_name의 길이 <= 10
flag_name은 '-'(dash)로 시작하고, 영어 대소문자로만 이루어져 있습니다.
동일한 flag_name에 대한 처리는 하지 않아도 됩니다.
flag_argument_type: "NULL" | "NUMBER" | "NUMBERS" | "STRING" | "STRINGS"
"NULL": flag argument를 받지 않습니다.
"NUMBER": 0부터 9까지의 숫자로만 이루어진 flag argument를 받습니다.
"NUMBERS": 1개 이상의 "NUMBER"로 이루어져 있습니다. 각 "NUMBER"는 공백으로 구분됩니다.
"STRING": 알파벳 대소문자로만 이루어진 flag argument를 받습니다.
"STRINGS": 1개 이상의 "STRING"으로 이루어져 있습니다. 각 "STRING"은 공백으로 구분됩니다.
ALIAS
flag_name_1은 flag_name_2의 ALIAS입니다. 따라서 flag_argument_type도 같고, flag_name_1과 flag_name_2는 동시에 입력할 수 없습니다.
원래 이름인 flag_name_2의 flag_argument_type을 정의한 flag_rule은 항상 flag_rules에 존재합니다.
ALIAS의 ALIAS는 존재하지 않습니다.
하나의 flag는 최대 하나의 ALIAS만 가집니다.
commands: [command]
1 <= commands의 길이 <= 100
1 <= command의 길이 <= 100
command는 하나의 program과 여러 flag가 string 형태로 이어져 있고, 이들은 공백으로 구분됩니다.
연속되는 공백도 공백처리를 하지 않아도 됩니다.
출력 형식
answer: boolean[]
commands의 순서대로 각 command를 판단하여 boolean 배열을 반환합니다.
command가 아래 조건을 모두 만족하면 True, 만족하지 않으면 False를 반환합니다.
program으로 시작합니다.
각 flag argument는 대응하는 flag의 flag_argument_type과 일치합니다.
각 flag는 0번이나 1번 나타납니다.
flag_rules에 존재하는 flag만 나타납니다.
입출력 예제
번호	program	flag_rules	commands	answer
1	"line"	["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"]	["line -n 100 -s hi -e", "line -n 100 -e -num 150"]	[True, False]
2	"bank"	["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"]	["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]	[False, False]
입출력 예제에 대한 해설
[True, False]
주어진 조건을 만족합니다.
flag의 원래 이름과 별칭이 동시에 등장합니다.
[False, False]
flag의 원래 이름과 별칭이 동시에 등장합니다.
flag "-a"는 "-amount"의 별칭이므로, "NUMBERS" flag argument를 입력 값으로 받아야 합니다.