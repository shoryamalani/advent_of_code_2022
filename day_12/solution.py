from collections import deque
def find_shortest_path_len(coords_start, coords_end, data):
    queue = [coords_start]
    visited = []
    path_len = 0
    # height of next coord can be at most one higher than current coord
    # so we can use a BFS
    queue = [coords_start]
    # queue = deque()
    depth_queue = [0]
    queue_depth = 0
    cnt = 1
    visited_dict = {}
    while queue:
        current_coord = queue.pop(0)
        cnt -= 1
        # current_depth = depth_queue.pop(0)
        if current_coord in queue:
            continue
        if cnt == 0:
            queue_depth +=1
            visited.append(current_coord)
            visited_dict[current_coord] = 1
            
            if current_coord == coords_end:
                return queue_depth
            if len(visited) == 1:
                possible_next = find_possible_next(current_coord, None, data)
            else:
                possible_next = find_possible_next(current_coord, visited[-2], data)
            for p in possible_next:
                if p not in visited_dict:
                    queue.append(p)
            cnt = len(queue)
        else:
            visited.append(current_coord)
            visited_dict[current_coord] = 1
            if len(visited) > 100:
                visited = visited[len(visited)-90:]
            if current_coord == coords_end:
                return queue_depth
            if len(visited) == 1:
                possible_next = find_possible_next(current_coord, None, data)
            else:
                possible_next = find_possible_next(current_coord, visited[-2], data)
            for p in possible_next:
                if p not in visited_dict:
                    queue.append(p)
        #handle the case where we arent adding length just traversing a different branch
        # if len(visited) > 1:
        #     if current_coord[0] != visited[-2][0] or current_coord[1] != visited[-2][1]:
    return -1
    

def find_possible_next(current_coord,last_coord,data):
    possible_next = []
    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_coord = (current_coord[0] + d[0], current_coord[1] + d[1])
        if new_coord[0] < 0 or new_coord[1] < 0:
            continue
        try:
            data[new_coord[0]][new_coord[1]]
        except IndexError:
            continue
        if new_coord != last_coord:
            # if data[current_coord[0]][current_coord[1]] == "S":
            #     if ALPHA.index(data[new_coord[0]][new_coord[1]]) < 2 :
            #         possible_next.append(new_coord)
            # elif data[new_coord[0]][new_coord[1]] == "S":
            #     pass
            # elif data[new_coord[0]][new_coord[1]] == "E" and ALPHA.index(data[new_coord[0]][new_coord[1]]) <= ALPHA.index(data[current_coord[0]][current_coord[1]]) + 1 :
            #     possible_next.append(new_coord)
            # else:
                if data[new_coord[0]][new_coord[1]] <= data[current_coord[0]][current_coord[1]] + 1:
                    possible_next.append(new_coord)
    return possible_next
from sys import argv
print(argv)
if len(argv) != 1:
    file = "input-5.txt"
else:
    file = "input-11.txt"
with open(file, "r") as f:
    ALPHA = "abcdefghijklmnopqrstuvwxyzE"
    data = f.read()
    data = data.split("\n")
    data = [list(l) for l in data]
    coords_start = []
    coords_end = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                coords_start.append((i, j))
            elif data[i][j] == "a":
                coords_start.append((i, j))
            elif data[i][j] == "E":
                coords_end = (i, j)
    final_data = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data[i])):
            try:
                temp.append(ALPHA.index(data[i][j]))
                if data[i][j] == "E":
                    temp.pop()
                    temp.append(25)
            except ValueError:
                temp.append(1)
        final_data.append(temp)
    final_distances = []
    for i in range(len(coords_start)):
        final_distances.append(find_shortest_path_len(coords_start[i], coords_end, final_data))
    print(final_distances)
    distances_with_1 = []
    for a in final_distances:
        if a != -1:
            distances_with_1.append(a)
    print(min(distances_with_1))
     
    
