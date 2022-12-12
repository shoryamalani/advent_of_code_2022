alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
with open("input-3.txt","r+") as f:
    data = f.read()
    data = data.split("\n")
    total = 0
    for i in data:
        first_half = i[len(i)//2:]
        second_half = i[:len(i)//2]
        first_half = set(first_half)
        second_half = set(second_half)
        for a in first_half:
            if a in second_half:
                total += alpha.index(a) +1
                break
    print(total)

with open("input-3.txt","r+") as f:
    data = f.read()
    data = data.split("\n")
    i = 0
    total = 0
    while i < (len(data))/3 - 1:
        full_set = []
        j = 0
        while j < 3:
            full_set.append(set(list(data[j+i*3])))
            print(data[j+i*3])
            j += 1
        for a in full_set[0]:
            if a in full_set[1] and a in full_set[2]:
                total += alpha.index(a) +1
                break
    
            
        i += 1
    print(total)