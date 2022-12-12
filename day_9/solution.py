
def move_grace(head,tail):
    if head[0] == tail[0] and head[1] == tail[1]:
        pass
    if head[0] - tail[0] == 2 and head[1] - tail[1] == 0:
        tail[0] += 1
    elif head[0] - tail[0] == -2 and head[1] - tail[1] == 0:
        tail[0] -= 1
    elif head[0] - tail[0] == 0 and head[1] - tail[1] == 2:
        tail[1] += 1
    elif head[0] - tail[0] == 0 and head[1] - tail[1] == -2:
        tail[1] -= 1
    elif head[0] - tail[0] == 2 and head[1] - tail[1] == 1:
        tail[0] += 1
        tail[1] += 1
    elif head[0] - tail[0] == 2 and head[1] - tail[1] == -1:
        tail[0] += 1
        tail[1] -= 1
    elif head[0] - tail[0] == -2 and head[1] - tail[1] == 1:
        tail[0] -= 1
        tail[1] += 1
    elif head[0] - tail[0] == -2 and head[1] - tail[1] == -1:
        tail[0] -= 1
        tail[1] -= 1
    elif head[0] - tail[0] == 1 and head[1] - tail[1] == 2:
        tail[0] += 1
        tail[1] += 1
    elif head[0] - tail[0] == -1 and head[1] - tail[1] == 2:
        tail[0] -= 1
        tail[1] += 1
    elif head[0] - tail[0] == 1 and head[1] - tail[1] == -2:
        tail[0] += 1
        tail[1] -= 1
    elif head[0] - tail[0] == -1 and head[1] - tail[1] == -2:
        tail[0] -= 1
        tail[1] -= 1
    elif head[0] - tail[0] == 2 and head[1] - tail[1] == 2:
        tail[0] += 1
        tail[1] += 1
    elif head[0] - tail[0] == 2 and head[1] - tail[1] == -2:
        tail[0] += 1
        tail[1] -= 1
    elif head[0] - tail[0] == -2 and head[1] - tail[1] == 2:
        tail[0] -= 1
        tail[1] += 1
    elif head[0] - tail[0] == -2 and head[1] - tail[1] == -2:
        tail[0] -= 1
        tail[1] -= 1
    
    return head, tail
    
with open("input-8.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
    head = [0, 0]
    knots = [[0,0] for i in range(9)]
    places_tail_visited = {}
    for i in data:
        i = i.split(" ")
        for a in range(int(i[1])):
            if i[0] == "U":
                head[1] += 1
            elif i[0] == "D":
                head[1] -= 1
            elif i[0] == "R":
                head[0] += 1
            elif i[0] == "L":
                head[0] -= 1
            for j in range(9):
                # knots[j][0],knots[j][1] = move_grace(knots[j][0],knots[j][1])
                if j == 0:
                    k,knots[j] = move_grace(head,knots[j])
                else:
                    knots[j-1],knots[j] = move_grace(knots[j-1],knots[j])
            print(knots)
                

            
            places_tail_visited[str(knots[8][0]) + "," + str(knots[8][1])] = 1
    print(len(places_tail_visited))



