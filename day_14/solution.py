from sys import argv
filename = 'input-5.txt'
if len(argv) == 2:
    filename = 'input-13.txt'
def dimensions(data):
    max_x = 0
    max_y = 0
    for a in data:
        a = a.split(" ")
        for b in a:
            if "," in b:
                b = b.split(",")
                if int(b[0]) > max_x:
                    max_x = int(b[0])
                if int(b[1]) > max_y:
                    max_y = int(b[1])
    return [["" for x in range(max_x + 100)] for y in range(max_y + 3)]
    return max_x, max_y

def  add_lines_to_dim(dimensions, data):
    for a in data:
        a = a.split("->")
        i = 0
        while i < len(a) -1:
            first_x = int(a[i].split(",")[0]) 
            first_y = int(a[i].split(",")[1]) 
            second_x = int(a[i+1].split(",")[0]) 
            second_y = int(a[i+1].split(",")[1]) 
            if first_x > second_x:
                first_x, second_x = second_x, first_x
            if first_y > second_y:
                first_y, second_y = second_y, first_y
            for x in range(first_x, second_x + 1):
                for y in range(first_y, second_y + 1):
                    dimensions[y][x] = "#"
            i += 1
    for i in range(len(dimensions[0])):
        dimensions[-1][i] = "#"
    return dimensions

def add_sand(dimensions):
    ## add sand from 0, 500 and drop it down
    ## if it hits a wall, it will go left and right
    if dimensions[0][500] == "#":
        return False
    else:
        i = 1
        x = 500
        while i < len(dimensions):
            if dimensions[i][x] == "#":
                # try left
                if dimensions[i][x-1] == "#":
                    # try right
                    if dimensions[i][x+1] == "#":
                        dimensions[i-1][x] = "#"
                        return dimensions
                    else:
                        x += 1
                        i += 1
                else:
                    x -= 1
                    i += 1
            else:
                i += 1
        return False


with open(filename, "r") as f:
    data = f.read()
    data = data.split("\n")
    set_up_dimensions = dimensions(data)
    print(set_up_dimensions)
    add_lines = add_lines_to_dim(set_up_dimensions, data)
    i = 0
    while True:
        add_lines = add_sand(add_lines)
        if add_lines != False:
            i += 1
        else:
            break
    print(i)


    