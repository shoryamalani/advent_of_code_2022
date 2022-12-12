with open("input-5.txt", "r") as f:
    data = f.read()
    i = 13
    while i < len(data):
        if len(set(data[i-13:i+1])) == 14:
            print(data[i-13:i+1])
            print(i)
            break
        i += 1
    