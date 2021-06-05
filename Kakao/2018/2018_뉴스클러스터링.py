def solution(str1, str2):
    
    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    tlist = set(list1) | set(list2)
    res1 = [] #합집합
    res2 = [] #교집합

    if tlist:
        for i in tlist:
            res1.extend([i]*max(list1.count(i), list2.count(i)))
            res2.extend([i]*min(list1.count(i), list2.count(i)))

        answer = int(len(res2)/len(res1)*65536)
        return answer

    else:
        return 65536






# def solution(str1, str2):
#     strings = []
#     for string in [str1, str2]:
#         conv = string.upper()
#         convs = {}
#         for i in range(1, len(conv)):
#             word = conv[i-1] + conv[i]
#             if word.isalpha():
#                 convs[word] = convs.get(word, 0) + 1
#         strings.append(convs)

#     str1, str2 = strings 
#     interaction = []
#     for s1 in str1:
#         if s1 in str2:
#             interaction  += [s1 for _ in range(min(str1[s1], str2[s1]))]

#     union = []
#     jaccard_keys = list(str1.keys()) + list(str2.keys())
#     for j in set(jaccard_keys):
#         union += [j for _ in range(max(str1.get(j, 0), str2.get(j, 0)))]
    
#     n = len(interaction) / len(union) if len(union) != 0 else 1

#     return int(n * 65536)

