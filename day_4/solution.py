with open("input-4.txt","r+") as f:
    data = f.read()
    data = data.split("\n")
    total = 0
    for a in data:
        a = a.split(",")
        b = [ x.split("-") for x in a]
        if int(b[0][0]) <= int(b[1][0]) and int(b[0][1]) >= int(b[1][1]):
            total += 1
        elif int(b[0][0]) >= int(b[1][0]) and int(b[0][1]) <= int(b[1][1]):
            total += 1
    print(total)

with open("input-4.txt","r+") as f:
    data = f.read()
    data = data.split("\n")
    total = 0
    for a in data:
        a = a.split(",")
        b = [ x.split("-") for x in a]
        print(b)
        total_ad = False
        if int(b[0][0]) <= int(b[1][0]) and int(b[0][1]) >= int(b[1][0]):
            total_ad += True
        elif int(b[0][0]) <= int(b[1][1]) and int(b[0][1]) >= int(b[1][1]):
            total_ad += True
        if int(b[1][0]) <= int(b[0][0]) and int(b[1][1]) >= int(b[0][0]):
            total_ad += True
        elif int(b[1][0]) <= int(b[0][1]) and int(b[1][1]) >= int(b[0][1]):
            total_ad += True
        if total_ad:
            total += 1
    print(total)
