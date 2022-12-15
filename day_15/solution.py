import time
from sys import argv
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import freeze_support, Pool, active_children
filename = 'input-5.txt'
if len(argv) == 2:
    filename = 'input-14.txt'

def recursive_merge(inter, start_index = 0):
    for i in range(start_index, len(inter) - 1):
        if inter[i][1] >= inter[i+1][0] -1:
            new_start = inter[i][0]
            new_end = inter[i+1][1]
            inter[i] = [new_start, new_end]
            del inter[i+1]
            return recursive_merge(inter.copy(), start_index=i)
    return inter 

def find_taken_in_y(y,values,max_size):
    freeze_support()
    taken = {}
    taken_ranges = []
    for value in values:
        #manhattan distance
        max_distance = abs(value[0][0]-value[1][0]) + abs(value[0][1]-value[1][1])
        if max_distance >= abs(y - value[0][1]):
            #find number of vals at height y that are within manhattan distance
            origin = value[0]
            lowest_x = (max_distance - abs(y - origin[1])) * -1 + origin[0]
            highest_x = max_distance - abs(y - origin[1]) + origin[0]
            taken_ranges.append([lowest_x,highest_x])
            # for x in range(lowest_x,highest_x+1):
            #     taken[(x,y)] = 1
                # else:
                #     taken[(x,y)] += 1
    taken_ranges.sort()
    start = 0
    i = 0
    while start < max_size :
        if i >= len(taken_ranges):
            print(start,y)
            return 0
        if start >= taken_ranges[i][0] and start <= taken_ranges[i][1]:
            start = taken_ranges[i][1] + 1
            i+=1
            continue
        i+=1
    return 1

        
    # last_val = 0
    # final_arr = []
    # merge all ranges
    # find if there is a gap between ranges
    # return
    taken_ranges = recursive_merge(sorted(taken_ranges))
    if len(taken_ranges) == 1:
        return 0
    else:
        for a in taken_ranges:
            if a[0] > 0 and a[1] < max_size:
                print(taken_ranges,y)
                return 1
        return 0
    print(taken_ranges,y)
    if taken_ranges[0] > 0 and taken_ranges[1] < max_size:
        print(taken_ranges,y)
        return 1
    return 0


        
    for val in taken:
        final_arr.append(list(val))
    
    return get_arr(final_arr,max_size)
    # print(len(taken))
    # vals = [val for val,va in taken.items()]
    # vals.sort()
    # #check if beakon is in range
    # for a in values:
    #     if (a[1][0],a[1][1]) in vals:
    #         taken[tuple(a[1])] = 0
    #         # taken.pop(tuple(a[1]))
    # print(len(taken))
    # sub = 0
    # for val in taken:
    #     if taken[val] == 0:
    #        sub += 1
    # print(len(taken)-sub)
def get_arr(vals,max_size):
    final = [0 for i in range(max_size)]
    for val in vals:
        if val[0] < max_size and val[1] < max_size and val[0] >= 0 and val[1] >= 0:
            final[val[0]] = 1
    return final
def find_beacon(max_size,values):
    taken = {}
    max_size+=1
    # total = [[0 for i in range(max_size)] for j in range(max_size)]
    total = []
    threads = []
    with Pool(4) as pool:
        # for i in range(max_size):
            # threads.append(executor.apply_async(find_taken_in_y,(i,values)))
        total = [(i,values,max_size) for i in range(max_size)]
        total = pool.starmap(find_taken_in_y,total)

            # threads.append(multiprocessing.Process(target=find_taken_in_y,args=(i,values)).start())
        
        # for thread in threads:
        #     for a in thread.get():
        #         if a[0] < max_size and a[1] < max_size and a[0] >= 0 and a[1] >= 0:
        #             total[a[0]][a[1]] = 1
    # with ThreadPoolExecutor(max_workers=6) as executor:
    #     for i in range(max_size):
    #         threads.append(executor.submit(find_taken_in_y,i,values))
    #     for thread in as_completed(threads):
    #         for a in thread.result():
    #             if a[0] < max_size and a[1] < max_size and a[0] >= 0 and a[1] >= 0:
    #                 total[a[0]][a[1]] = 1
    # while active_children():
    #     time.sleep(1)
    #     print(active_children())
    # i = 0
    # while i < max_size:
    #     j = 0
    #     while j < max_size:
    #         if total[i][j] == 0:
    #             print(i,j)
    #         j+=1
    #     i+=1


if __name__ == "__main__":            

    with open(filename,"r") as f:
        lines = f.readlines()
        x = [[[int(line.split(":")[0].split(",")[0].split("=")[1]),int(line.split(":")[0].split(",")[1].split("=")[1])],[int(line.split(":")[1].split(",")[0].split("=")[1]),int(line.split(":")[1].split(",")[1].split("=")[1])]] for line in lines]
        # find_taken_in_y(2000000,x)
        find_beacon(4000000,x)
        
        # find_beacon(20,x)