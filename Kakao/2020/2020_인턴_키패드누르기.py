def solution(numbers, hand):
    left_key = [1, 4, 7]
    right_key = [3, 6, 9]
    hand_position = ['*', '#']

    position = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2),
    }
    result = ''
    for num in numbers:
        if num in left_key:
            result += 'L'
            hand_position[0] = num
        elif num in right_key:
            result += 'R'
            hand_position[1] = num
        else:
            near_hand = get_near_hand(position, hand_position[0], hand_position[1], num, hand)
            if near_hand == 'L':
                result += 'L'
                hand_position[0] = num
            else:
                result += 'R'
                hand_position[1] = num
    return result

def get_near_hand(pos, l,r, num, hand):
    ld = abs(pos[l][0] - pos[num][0]) + abs(pos[l][1]-pos[num][1])
    rd = abs(pos[r][0] - pos[num][0]) + abs(pos[r][1]-pos[num][1])

    if ld == rd:
        near_hand = 'L' if hand == 'left' else 'R'
    else:
        near_hand = 'L' if ld < rd else 'R'
    return near_hand
        