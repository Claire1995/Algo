def solution(s):
    replace_t1 = s.replace(",", " ")
    replace_t2 = replace_t1.replace("} {", "/")
    replace_t3 = replace_t2.replace("}", "")
    replace_t4 = replace_t3.replace("{", "")
    tuples = replace_t4.split('/')
    sortedTuples = sorted(tuples, key=len)
    answer = []
    
    for i in range(len(sortedTuples)):
        temp = sortedTuples[i].split()
        if len(temp) == 1:
            answer.append(temp[i])
        else:
            for j in range(len(answer)):
                temp.remove(answer[j])
            answer.append(temp[0])
    return list(map(int, answer))