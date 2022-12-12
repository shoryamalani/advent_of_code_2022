with open("input-5.txt", "r") as f:
    data = f.read()
    init_state = data.split("\n\n")[0].split("\n")
    num_of_columns = init_state[-1].split(" ")[-2]
    num_of_columns = int(num_of_columns)
    init_state.pop()
    init_state = [x.replace("        ","]]") for x in init_state]
    init_state = [x.replace("    ","]") for x in init_state]
    init_state = [x.split("]") for x in init_state][::-1]
    final_init_state = []
    # for a in init_state:
    #     temp = []
    #     for b in a:
    #         if len(temp):
    #             if temp[-1] == "" and b == "":
    #                 pass
    #             else:
    #                 temp.append(b)
    #         else:
    #             temp.append(b)
    #     final_init_state.append(temp)

    # init_state = final_init_state
    movements = data.split("\n\n")[1].split("\n")
    full_init = [[] for i in range(num_of_columns)]
    print(init_state)
    for i in range(num_of_columns):
        for j in range(len(init_state)):
            full_init[i].append(init_state[j][i])
    for i in range(len(full_init)):
        while "" in full_init[i]:
            full_init[i].remove("")
    print(full_init)
    for i in movements:
        i = i.split(" ")
        num_move = int(i[1])
        from_c = int(i[3])
        to = int(i[5])
        for j in range(num_move):
            full_init[to-1].append(full_init[from_c-1].pop())
    print(full_init)
    for i in full_init:
        print(i[-1], end=" ")


with open("input-5.txt", "r") as f:
    data = f.read()
    init_state = data.split("\n\n")[0].split("\n")
    num_of_columns = init_state[-1].split(" ")[-2]
    num_of_columns = int(num_of_columns)
    init_state.pop()
    init_state = [x.replace("        ","]]") for x in init_state]
    init_state = [x.replace("    ","]") for x in init_state]
    init_state = [x.split("]") for x in init_state][::-1]
    final_init_state = []
    # for a in init_state:
    #     temp = []
    #     for b in a:
    #         if len(temp):
    #             if temp[-1] == "" and b == "":
    #                 pass
    #             else:
    #                 temp.append(b)
    #         else:
    #             temp.append(b)
    #     final_init_state.append(temp)

    # init_state = final_init_state
    movements = data.split("\n\n")[1].split("\n")
    full_init = [[] for i in range(num_of_columns)]
    print(init_state)
    for i in range(num_of_columns):
        for j in range(len(init_state)):
            full_init[i].append(init_state[j][i])
    for i in range(len(full_init)):
        while "" in full_init[i]:
            full_init[i].remove("")
    print(full_init)
    for i in movements:
        i = i.split(" ")
        num_move = int(i[1])
        from_c = int(i[3])
        to = int(i[5])
        #move all at once
        temp = full_init[from_c-1][-num_move:]
        for a in temp:
            full_init[to-1].append(a)
            full_init[from_c-1].pop()
        # for j in range(num_move):
            # full_init[to-1].append(full_init[from_c-1].pop())
    print(full_init)
    for i in full_init:
        print(i[-1], end=" ")


