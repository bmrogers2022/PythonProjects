with open("cdp.txt", "r") as cdp:
    info = [x.strip() for x in cdp.readlines()]
    cdp_rankings = {}
    count = 1
    for x in info[0:92]: # steep dropoff in QB ratings after QB10
        player = ""
        i = 0
        while x[i] != "(":
            player += x[i]
            i += 1
        cdp_rankings[player] = count
        count += 1
    # print(cdp_rankings)

# print(info)

with open("espn_order.txt", "r") as espn_order:
    info = [x.strip() for x in espn_order.readlines()]
    espn_rankings = {}
    count = 1
    for x in info:
        player = ""
        i = 0
        while x[i] != "(":
            player += x[i]
            i += 1
        espn_rankings[player] = count
        count += 1
    # print(espn_rankings)

print(cdp_rankings["Christian McCaffrey"])
print(espn_rankings["Christian McCaffrey"])
players_relative_value = {i: espn_rankings[i]-cdp_rankings[i] for i in cdp_rankings.keys()}

sorted_by_rel_val = {k: v for k, v in sorted(players_relative_value.items(), key=lambda player: player[1], reverse=True)}

print(sorted_by_rel_val)
