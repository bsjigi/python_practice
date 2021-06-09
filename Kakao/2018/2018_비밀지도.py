def solution(n, arr1, arr2):
    answer = []
    for a1,a2 in zip(arr1, arr2):
        a = str(bin(a1 | a2))[2:]
        a = '0'*(n - len(a)) + a
        a = a.replace('1', '#')
        a = a.replace('0', ' ')
        answer.append(a)
    return answer