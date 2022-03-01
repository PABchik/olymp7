nodes = [1, -5, -20, -5, -200, -2, -700]

rel = [[1, 5, 6],
       [0, 2],
       [1, 3],
       [2, 4],
       [3, 5, 6],
       [0, 4],
       [0, 4]]

for a in range(1, 100):
       nodesTemp = nodes.copy()
       for i in range(len(rel)):
              if nodes[i] > 0:
                     for r in rel[i]:
                            nodesTemp[r] += nodes[i]
       nodes = nodesTemp.copy()
       print(f'{a}) ', end="")
       print(*nodes)
       flag = True
       for i in nodes:
              if i <= 0:
                     flag = False
                     break
       if flag:
              print(a)
              break