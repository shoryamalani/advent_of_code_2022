with open("input-5.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
    totals = []
    last_input = True
    i = 0
    cycles_to_run = 0 
    val = 1
    num_to_add = [0]
    command_num = 0
    while last_input:
        

        if i==20:
            totals.append(val*i)
            print(num_to_add[20])
            print(val)
        elif (i-20) % 40 == 0:
            totals.append(val*i)
        val += num_to_add[i]
        if cycles_to_run == 0:
            if data[command_num] == "noop":
                cycles_to_run = 1
                num_to_add.append(0)
            else:
                cycles_to_run = 2
                num_to_add.append(0)
                num_to_add.append(int(data[command_num].split()[-1]))
            command_num += 1
        
        cycles_to_run -= 1
        i += 1
        if command_num == len(data):
            last_input = False
    print(i)
    print(totals)
    print(sum(totals))
        
with open("input-9.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
    totals = []
    last_input = True
    i = 0
    cycles_to_run = 0 
    val = 1
    num_to_add = [0]
    command_num = 0
    while last_input:
        if abs(((i-1)%40)-val) <=1:
            print("#",end="")
        else:
            print(".",end="")
        if i%40 == 0:
            print()
        

        if i==20:
            totals.append(val*i)
        elif (i-20) % 40 == 0:
            totals.append(val*i)
        val += num_to_add[i]
        if cycles_to_run == 0:
            if data[command_num] == "noop":
                cycles_to_run = 1
                num_to_add.append(0)
            else:
                cycles_to_run = 2
                num_to_add.append(0)
                num_to_add.append(int(data[command_num].split()[-1]))
            command_num += 1
        
        cycles_to_run -= 1
        i += 1
        if command_num == len(data):
            last_input = False
    print(i)
    print(totals)
    print(sum(totals))
        