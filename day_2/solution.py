# get max between splits
with open("input-3.txt","r+") as f:
    # X is rock
    # Y is paper
    # Z is scissors
    rock_paper_scissors = {"A":["X","Z"],"B":["Y","X"],"C":["Z","Y"] }
    data = f.read().splitlines()
    total = 0
    for i in range(0,len(data)):
        if data[i][0] == "A":
            if data[i][-1] == "X":
                total += 1
                total += 3
                # Draw
            elif data[i][-1] == "Y":
                total += 2
                total += 6
                # Win
            else:
                total += 3
                # Lose
        elif data[i][0] == "B":
            if data[i][-1] == "Y":
                total += 2
                total += 3
                # Draw
            elif data[i][-1] == "Z":
                total += 3
                total += 6
                # Win
            else:
                total += 1
                # Lose
        elif data[i][0] == "C":
            if data[i][-1] == "Z":
                total += 3
                total += 3
                # Draw
            elif data[i][-1] == "X":
                total += 1
                total += 6
                # Win
            else:
                total += 2
                # Lose
    print(total)

# get max between splits
with open("input-3.txt","r+") as f:
    # X is rock
    # Y is paper
    # Z is scissors
    rock_paper_scissors = {"A":["X","Z"],"B":["Y","X"],"C":["Z","Y"] }
    data = f.read().splitlines()
    total = 0
    for i in range(0,len(data)):
        if data[i][-1] == "X":
            #Lose
            total +=0
            if data[i][0] == "A":
                total += 3
            elif data[i][0] == "B":
                total += 1
            elif data[i][0] == "C":
                total += 2
        elif data[i][-1] == "Y":
            #Draw
            total += 3
            if data[i][0] == "A":
                total += 1
            elif data[i][0] == "B":
                total += 2
            elif data[i][0] == "C":
                total += 3
        elif data[i][-1] == "Z":
            #Win
            total += 6
            if data[i][0] == "A":
                total += 2
            elif data[i][0] == "B":
                total += 3
            elif data[i][0] == "C":
                total += 1
    print(total)