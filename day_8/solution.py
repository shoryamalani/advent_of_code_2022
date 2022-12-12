def visible(a,b):
    visible = False
    # if everything to the top of it is higher
    if any([data_grid[i][b] >= data_grid[a][b] for i in range(a)]):
        pass
    else:
        return False
    # if anything to the bottom of it is higher
    if any([data_grid[i][b] >= data_grid[a][b] for i in range(a+1, len(data_grid[0]))]):
        pass
    else:
        return False
    # if anything to the left of it is higher
    if any([data_grid[a][i] >= data_grid[a][b] for i in range(b)]):
        pass
    else:
        return False
    # if anything to the right of it is higher
    if any([data_grid[a][i] >= data_grid[a][b] for i in range(b+1, len(data_grid[0]))]):
        pass
    else:
        return False
    return True
    # for i in range(a):
    #     if data_grid[i][b] > data_grid[a][b] :
    #         vis_top = False
    #         break
    #     else:
    #         vis_top = True
    # if everything to the bottom of it is higher
    vis_bottom = True
    for i in range(a+1, len(data_grid[0])):
        if data_grid[i][b] > data_grid[a][b]:
            vis_bottom = False
            break
        else:
            vis_bottom = True
    # if everything to the left of it is higher
    vis_left = True
    for i in range(b):
        if data_grid[a][i] > data_grid[a][b] :
            vis_left = False
            break
        else:
            vis_left = True
    # if everything to the right of it is higher
    vis_right = True
    for i in range(b+1, len(data_grid[0])):
        if data_grid[a][i] > data_grid[a][b] :
            vis_left = False
            break
        else:
            vis_left = True
    if all([vis_top, vis_bottom, vis_left, vis_right]):
        return True
    else:
        return False

def scenic(a,b):
    #look up from tree
    up = 0
    highest_up = 0
    for i in range(a):
        if data_grid[a-i-1][b] >= data_grid[a][b]:
            up += 1
            break
        else:
            up += 1
            # if int(data_grid[a-i-1][b]) >= highest_up:
            #     up += 1
            #     highest_up = int(data_grid[a-i-1][b])
            # else:
            #     continue
    #look down from tree
    down = 0
    highest_down = 0
    for i in range(a+1, len(data_grid[0])):
        if data_grid[i][b] >= data_grid[a][b]:
            down += 1
            break
        else:
            down += 1
            # if int(data_grid[i][b]) >= highest_down:
            #     down += 1
            #     highest_down = int(data_grid[i][b])
            # else:
            #     continue
    #look left from tree
    left = 0
    highest_left = 0
    for i in range(b):
        if data_grid[a][b-i-1] >= data_grid[a][b]:
            left += 1
            break
        else:
            left += 1
            # if int(data_grid[a][b-i-1]) >= highest_left:
            #     left += 1
            #     highest_left = int(data_grid[a][b-i-1])
            # else:
            #     continue
    #look right from tree
    right = 0
    highest_right = 0
    for i in range(b+1, len(data_grid[0])):
        if data_grid[a][i] >= data_grid[a][b]:
            right += 1
            break
        else:
            right += 1
            # if int(data_grid[a][i]) >= highest_right:
            #     right += 1
            #     highest_right = int(data_grid[a][i])
            # else:
            #     continue

    return up * down * left * right


with open("input-7.txt", "r") as f:
    data = f.read()
    data_grid = data.split("\n")
    total = 0
    for a in range(len(data_grid)):
        for b in range(len(data_grid[0])):
            if not visible(a,b):
                total += 1
    print(total)
    print((a+1)*(b+1) - total)
    highest = 0
    for a in range(len(data_grid)):
        for b in range(len(data_grid[0])):
            if a == 3 and b == 2:
                a = 3
            if scenic(a,b) > highest:
                highest = scenic(a,b)
                print(a,b)
                
    print(highest)