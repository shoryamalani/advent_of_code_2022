# get max between splits
with open("input-2.txt","r+") as f:
    data = f.read()
    data = data.split("\n\n")
    print(data)
    data = [i.split() for i in data]
    sums = []
    for i in data:
        sum_val = 0
        for a in i:
            sum_val += int(a)
        # if sum_val > cur_max:
        #     cur_max = sum_val
        sums.append(sum_val)
    sums.sort()
    print(sums[::-1])
# with open("input-2.txt","r+") as f:
#     data = f.readlines()
#     data = [int(i.strip()) for i in data]
#     data = [int(data[i])+int(data[i+1])+int(data[i+2]) for i in range(0,len(data)-2)]
#     last_val = 0
#     increasing = 0
#     for i in range(len(data)):
#         if i == 0:
#             last_val = data[i]
#         else:
#             if data[i] > last_val:
            
#                 increasing += 1
#             last_val = data[i]
#     print(increasing)