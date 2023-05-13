with open("cdp.txt", "r") as cdp:
    info = [x.strip() for x in cdp.readlines() if x[0] != "-" and x[0].isdigit() == False]
    print(info)

with open("cdp.txt", "w+") as cdp:
    for i in range(len(info)):
        cdp.write(f'{info[i]}\n')

with open("espn_order.txt", "r") as espn_order:
    info = [x.strip() for x in espn_order.readlines() if x[0] != "-" and x[0].isdigit() == False]
    print(info)

with open("espn_order.txt", "w+") as espn_order:
    for i in range(len(info)):
        espn_order.write(f'{info[i]}\n')