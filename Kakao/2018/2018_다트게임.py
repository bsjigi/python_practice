import re

db = {'S': '**1', 'D': '**2', 'T': '**3', '#':'*-1'}

def solution(dartResult):
    answer = ''
    for i in re.sub('[SDT][*#]?', '\g<1> ', dartResult).split():
        if i[-1] == '*':
            if answer:
                answer = answer[:-1] + '*2+'
            i += '2'
        for j in db.key():
            i = i.replace(j, db[j])
        answer += i + '+'

    answer = answer[:-1]
    return eval(answer)