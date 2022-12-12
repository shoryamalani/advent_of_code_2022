import math
def run_operation(worry,operation):
    operator = operation[1]
    if operator == "+":
        if operation[2] == "old":
            return worry + worry
        else:
            return worry + int(operation[2])
    elif operator == "*":
        if operation[2] == "old":
            return worry * worry
        else:
            return worry * int(operation[2])

        

with open("input-10.txt", "r") as f:
    data = f.read()
    monkeys_dat = data.split("\n\n")
    monkeys = []
    for monkey in monkeys_dat:
        monkeys.append({"monkey_num": monkey.split("\n")[0],"items": [int(x) for x in monkey.split("\n")[1].split(":")[1].split(",")], "operation" : monkey.split("\n")[2].split("=")[1].split(" "), "test": int(monkey.split("\n")[3].split(" ")[-1]), "true_throw":int(monkey.split("\n")[4].split(" ")[-1]),"false_throw":int(monkey.split("\n")[5].split(" ")[-1]),"inspected":0})
    print(monkeys)
    rounds = 10000
    for monkey in monkeys:
        monkey['operation'].remove('')
    with open("primes.txt", "r") as f:
        data = f.read()
        data = data.replace("\n","")

        prime_factors = [int(x) for x in data.split(",")]
        tenths = [i['test'] for i in monkeys]
        mult = 1
        for i in tenths:
            mult = mult * i
    for a in range(rounds):
        for monkey in monkeys:
            for item in monkey["items"]:
                    
                new_worry_level = run_operation(item, monkey["operation"])
                new_worry_level = new_worry_level % mult
                # if new_worry_level > 100000000000:
                #     for i in prime_factors:
                #         while new_worry_level % i == 0 and new_worry_level > i*10:
                #             new_worry_level = new_worry_level // i
                #         if new_worry_level < i:
                #             break
                #     for i in tenths:
                #         if item < i[1]:
                #             print("tenth")
                #             break
                #         if item % i[1] == 0:
                #             item = item // i[0]
                if new_worry_level % monkey["test"] == 0:
                    monkeys[monkey["true_throw"]]["items"].append(new_worry_level)
                else:
                    monkeys[monkey["false_throw"]]["items"].append(new_worry_level)
                monkey["inspected"] += 1
            monkey["items"] = []
        print(a)
        # for monkey in monkeys:
        #     print(monkey["monkey_num"], monkey["items"],a)
    print(monkeys)
    for monkey in monkeys:
        print(monkey["monkey_num"], monkey["inspected"],a)




