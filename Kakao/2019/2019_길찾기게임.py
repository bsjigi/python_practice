import sys

class Node:
    def __init__(self, id , x, y):
        self.id = id 
        self.x = x 
        self.y = y 
        self.left = None
        self.right = None

    def __lt__(self, other):
        if(self.y == other.y ):
            return self.x < other.x
        return self.y > other.y

def addNode(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            addNode(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child 
        else:
            addNode(parent.right, child)  

def preorder(ans, node):
    if node is None:
        return
    ans.append(node.id)
    preorder(ans, node.left)
    preorder(ans, node.right)

def postorder(ans, node):
    if node is None:
        return
    postorder(ans, node.left)
    postorder(ans, node.right)
    ans.append(node.id)

def solution(nodeinfo):
    sys.setrecursionlimit(1500)
    size = len(nodeinfo)
    nodelist = []
    for i in range(size):
        nodelist.append(Node(i+1, nodeinfo[i][0], nodeinfo[i][1]))
    nodelist.sort()
    root = nodelist[0]
    for i in range(1, size):
        addNode(root, nodelist[i])
    answer = [[],[]]

    preorder(answer[0], root)
    postorder(answer[1], root)

    return answer



# preorder = list() # 귀찮아서 전역으로
# postorder = list()
# def solution(nodeinfo):
#     import sys
#     sys.setrecursionlimit(10**6)
#     levels = sorted(list({x[1] for x in nodeinfo}),reverse=True) # 유효한 Y좌표
#     nodes = sorted(list(zip(range(1,len(nodeinfo)+1),nodeinfo)),key=lambda x:(-x[1][1],x[1][0])) # 노드 정렬
#     order(nodes,levels,0)
#     return [preorder,postorder]

# def order(nodes,levels,curlevel):
#     n = nodes[:] # copy
#     cur = n.pop(0) # VISIT
#     preorder.append(cur[0]) # PRE-ORDER
#     if n: # stop if leaf node
#         for i in range(len(n)): # find next floor
#             if n[i][1][1] == levels[curlevel+1]: # next floor
#                 if n[i][1][0] < cur[1][0]: # LEFT CHILD
#                     order([x for x in n if x[1][0] < cur[1][0]],levels,curlevel+1)
#                 else: # RIGHT CHILD
#                     order([x for x in n if x[1][0] > cur[1][0]],levels,curlevel+1)
#                     break
#     postorder.append(cur[0]) # POST-ORDER