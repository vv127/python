import numpy as np
import matplotlib.pyplot as plt


n = 20 # n * n graph
graph = [[-1 for i in range(n)] for j in range(n)]

# ******** show the whole graph ********
def print_graph():
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end='')
        print()

# ******** DFS ********
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 4 directions
def dfs(x, y, id):
    graph[x][y] = id
    tx, ty = t[id]
    if [x, y] == [tx, ty]:
        return True
    d_val = [[0,0], [1,0], [2,0], [3,0]]
    if tx > x: d_val[0][1] += 1
    if tx < x: d_val[1][1] += 1
    if ty > y: d_val[2][1] += 1
    if ty < y: d_val[3][1] += 1
    d_val.sort(key=lambda x:-x[1]) #按分值从大到小排序
    seq = [d_val[i][0] for i in range(4)]
    for i in seq:
        vx = x + d[i][0]
        vy = y + d[i][1]
        if vx < 0 or vx > n or vy < 0 or vy > n:
            continue
        if graph[vx][vy] != -1:
            continue
        if dfs(vx, vy, id):
            return True
    else:
        return False



# ******** main ********
print("Please input number of point pair:")
num = int(input())
s = [[0, 0] for i in range(num)]  # Start point
t = [[0, 0] for i in range(num)]  # End point
print("Input 2 integers separated by space in each line, representing the x and y coordinates.")
for i in range(num):
    print("Start point of #%d:" % i, end='')
    s[i] = list(map(int, input().split()))
    graph[s[i][0]][s[i][1]] = i
    print("End point of #%d:" % i, end='')
    t[i] = list(map(int, input().split()))

plt.matshow(graph,  cmap=plt.cm.Blues)
plt.grid(which='major')
plt.show()

for i in range(num):
    print("#%d: " % i, s[i], "->", t[i])
    if dfs(s[i][0], s[i][1], i) == False:
        print("#%d: Failed" % i)
    else:
        #print_graph()
        print("#%d: successfully connected" % i)

print("Result:")
#print_graph()
plt.matshow(graph,  cmap=plt.cm.Blues)
plt.grid(which='major')
plt.show()