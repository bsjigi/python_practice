integrate = dict()

def time2min(str1):
    return int(str1.split(':')[0]) * 60 + int(str1.split(':')[1])

def min2time(min1):
    min1 = int(min1)
    return "%02d:%02d" %(min1//60, min1%60)

def crewTime(timetable):
   return [time2min(t) for t in timetable]

def shuttleTime(n, t, start = "09:00"):
    shuttle = [time2min(start)]
    for n1 in range(n-1):
        shuttle.append(shuttle[-1] + t)
    return shuttle

def DuplicateTime(time1):
    if not time1 in integrate.keys():
        return time1
    else:
        return DuplicateTime(time1 + 0.001)

def solution(n, t, m, timetable):
    global integrate
    answer = ''
    crew = sorted(crewTime(timetable))
    shuttle = shuttleTime(n, t)
    
    conTime = set(shuttle + crew)
    for c in set(crew):
        conTime.add(c - 1)

    for con in sorted(list(conTime))[::-1]:
        integrate = dict()
        for c in crew:
            integrate[DuplicateTime(c)] = 'crew'
        integrate[DuplicateTime(con)] = 'con'
        for sh in shuttle:
            integrate[DuplicateTime(sh)] = 'shuttle'
        waiting_line = []

        for time in sorted(integrate.keys()):
            if 'crew' == integrate[time]:
                waiting_line.append('crew')
            elif 'con' == integrate[time]:
                waiting_line.append('con')
            elif 'shuttle' == integrate[time]:
                waiting_line = waiting_line[m:]
        if not 'con' in waiting_line:
            return min2time(con)



# def solution(n,t,m,timetable):
#     timetable=[int(i[:2])*60+int(i[3:]) for i in timetable]
#     timetable.sort()
#     bustable=[9*60+t*i for i in range(n)]
#     for i in bustable:
#         passenger=[p for p in timetable if p<=i]
#         if i==bustable[-1]:
#             if len(passenger)>=m:
#                 answer=passenger[m-1]-1
#             elif len(passenger)<m:
#                 answer=i
#             else:
#                 answer=passenger[-1]
#         elif len(passenger)<m:
#             timetable=timetable[len(passenger):]
#         elif len(passenger)>=m:
#             timetable=timetable[m:]
#     answer= str(divmod(answer,60)[0]).rjust(2,'0')+':'+str(divmod(answer,60)[1]).rjust(2,'0')
#     return answer


   