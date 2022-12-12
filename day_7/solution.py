def check_if_in_path(path,file_name):
    path.split('/')
    cur_spot = file_struct["/"]
    for i in path.split('/'):
        if i != "":
            cur_spot = cur_spot[i]
            
    if file_name in cur_spot:
        return True
    else:
        cur_spot[file_name] = {"size":None,"contains":[]}

def add_file_to_struct(path,file_name,size):
    path.split('/')
    cur_spot = file_struct["/"]
    for i in path.split('/'):
        if i != "":
            cur_spot = cur_spot[i]
    cur_spot['contains'].append({file_name:size})


def size(cur_spot):
    if cur_spot['size'] == None:
        cur_spot['size'] = 0
        for i,j in cur_spot.items():
            if i == "contains":
                for a in j:
                    for k,v in a.items():
                        cur_spot['size'] += int(v)
            elif i == "size":
                pass
            else:
                if cur_spot[i]['size'] == None:
                    size(cur_spot[i])
                cur_spot['size'] += cur_spot[i]['size']
    return cur_spot['size']

def total_crawl(start):
    global total
    for i,j in start.items():
        if i == "contains":
            pass
        elif i == "size":
            if start['size'] < 100000:
                total += start['size']
        else:
            total_crawl(start[i])
def crawl_lowest(start):
    global c_lowest
    for i,j in start.items():
        if i == "contains":
            pass
        elif i == "size":
            if start['size'] > lowest and start['size'] < c_lowest:
                c_lowest = start['size']
        else:
            crawl_lowest(start[i])
with open("input-6.txt", "r") as f:
    data = f.read()
    data = data.split('\n')
    file_struct = {"/":{"size":None,"contains":[]}}
    current_path = ""
    current_command = ""
    for line in data:
        if line[0] == "$":
            if '$ cd' in line:
                if line.split(' ')[-1] == '..':
                    current_path = current_path.rsplit('/',1)[0]
                else:
                    check_if_in_path(current_path, line.split(' ')[-1])
                    current_path = current_path + "/" + line.split(' ')[-1]
        else:
            if "$ ls" not in line:
                if line.split()[0] == "dir":
                    check_if_in_path(current_path, line.split()[-1])
                else:
                    add_file_to_struct(current_path, line.split()[-1], line.split()[0])
    print(file_struct)
    size(file_struct["/"])
    total = 0
    print(file_struct['/']['size'])
    total_crawl(file_struct['/'])
    lowest = 30000000 - (70000000 - file_struct['/']['size'])
    c_lowest = 100000000000000
    crawl_lowest(file_struct['/'])
    print(lowest)
    print(c_lowest)







