from functools import cmp_to_key
def compare(a, b):
    x = bin(a).count('1')
    y = bin(b).count('1')
    return x - y 
    # 비트 1의 갯수에 따라 오름차순

def check(relation, rowsize, colsize, subset):
    for a in range(rowsize - 1):
        for b in range(a+1, rowsize):
            isSame = True
            for k in range(colsize):
                if (subset & 1 << k) == 0:
                    continue
                if relation[a][k] != relation[b][k]:
                    isSame = False
                    break
            if isSame:
                return False
    return True

#  부분집합 function


def solution(relation):
    answer = 0
    rowsize = len(relation)
    colsize = len(relation[0])
    candidates = []

    for i in range(1, 1 << colsize):
        if check(relation, rowsize, colsize, i):
            candidates.append(i)

    candidates = sorted(candidates, key=cmp_to_key(compare))

    while len(candidates) != 0:
        n = candidates.pop(0)
        answer += 1
        candidates = [x for x in candidates if (n & x) != n]

    return  answer