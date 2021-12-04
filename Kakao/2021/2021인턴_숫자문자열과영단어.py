Word = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

def solution(s):
    result = ''

    pos = 0

    while pos < len(s):
        if s[pos] >= '0' and s[pos] <= '9':
            result += s[pos]
            pos += 1
        else:
            for i in range(10):
                if s.find(Word[i], pos, pos + 5) != -1:
                    result += str(i)
                    pos += len(Word[i])
                    break

    answer = int(result)
    return answer
