def solution(inputString):
    answer = 0
    count = 0
    pairs = {'(':')', '{':'}', '[': ']', '<' : '>'}
    new_list = []
    
    for i in inputString:
        if i in pairs:
            new_list.append(i)
        else:
            if len(new_list) and i == pairs.get(new_list[-1]):
                new_list.pop()
                count = count + 1
                
    if len(new_list) == 0:
        answer = count   
    elif new_list[-1] == '(':
        if ")" in inputString:
            answer = inputString.index(')')
            answer = answer*(-1)
        else: 
            answer = (len(inputString) - 1)*(-1)
    elif new_list[-1] == '<':
        if ">" in inputString:
            answer = inputString.index('>')
            answer = answer*(-1)
        else: 
            answer = (len(inputString) - 1)*(-1)
    elif new_list[-1] == '[':
        if "]" in inputString:
            answer = inputString.index(']')
            answer = answer*(-1)
        else: 
            answer = (len(inputString) - 1)*(-1)
    elif new_list[-1] == '{':
        if "}" in inputString:
            answer = inputString.index('}')
            answer = answer*(-1)
        else: 
            answer = (len(inputString) - 1)*(-1)
    else: 
        answer = 0
            
        
    return answer