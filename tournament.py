#Opponent
opp_strategy_path = "/home/sh/Desktop/gthw/titfortat.txt"
opp_txt = open(opp_strategy_path, 'r')

opp_strategy = []
for line in opp_txt:
    zeile = line.strip()
    opp_strategy.append(zeile)

print(opp_strategy)
opp_group_names = opp_strategy[0]
opp_strategy_name = opp_strategy[1]

opp_number_nodes = opp_strategy[2]

#Me and my team
strategy_path = "/home/sh/Desktop/gthw/defect.txt"
my_txt = open(strategy_path, 'r')

my_strategy = []
for line in my_txt:
    zeile = line.strip()
    my_strategy.append(zeile)

print(my_strategy)
my_group_names = my_strategy[0]
my_strategy_name = my_strategy[1]

my_number_nodes = my_strategy[2]

#Game
my_strategy.remove(my_strategy_name) #Delete the first three elements of the list
my_strategy.remove(my_group_names)
my_strategy.remove(my_number_nodes)
opp_strategy.remove(opp_strategy_name) #Delete the first three elements of the list
opp_strategy.remove(opp_group_names)
opp_strategy.remove(opp_number_nodes)

my_points_total = 0 #Init points
opp_points_total = 0
my_node = 0 #Initialize at node 0
opp_node = 0

rounds = 100 #Parameter: How many games played
points_win = 0 #Parameter: How many points per outcome
points_loss = 20
points_coop = 10
points_defec = 15

my_node = 0
opp_node = 0

for i in range(1, rounds):
    if my_strategy[my_node].split(",")[0]=="D" and opp_strategy[opp_node].split(",")[0]=="D": #Defect draw
        my_points_total += points_defec
        opp_points_total += points_defec

        present_node = my_strategy[my_node] #Transitioning to new node
        present_node.split(",")
        my_node = int(present_node[4])

        present_node = opp_strategy[opp_node] #Transitioning to new node
        present_node.split(",")
        opp_node = int(present_node[4])

    elif my_strategy[my_node].split(",")[0]=="C" and opp_strategy[opp_node].split(",")[0]=="D": #We lose
        my_points_total += points_loss
        opp_points_total += points_win

        present_node = my_strategy[my_node]  # Transitioning to new node
        present_node.split(",")
        my_node = int(present_node[4])

        present_node = opp_strategy[opp_node]  # Transitioning to new node
        present_node.split(",")
        opp_node = int(present_node[2])

    elif my_strategy[my_node].split(",")[0]=="D" and opp_strategy[opp_node].split(",")[0]=="C": #We win
        my_points_total += points_win
        opp_points_total += points_loss

        present_node = my_strategy[0]  # Transitioning to new node
        present_node.split(",")
        my_node = int(present_node[2])

        present_node = opp_strategy[opp_node]  # Transitioning to new node
        present_node.split(",")
        opp_node = int(present_node[4])

    elif my_strategy[my_node].split(",")[0]=="C" and opp_strategy[opp_node].split(",")[0]=="C": #Coop draw
        my_points_total += points_coop
        opp_points_total += points_coop

        present_node = my_strategy[my_node]  # Transitioning to new node
        present_node.split(",")
        my_node = int(present_node[2])

        present_node = opp_strategy[opp_node]  # Transitioning to new node
        present_node.split(",")
        opp_node = int(present_node[2])

print(my_node,opp_node)
print(my_points_total, opp_points_total)

if my_points_total > opp_points_total:
    winner = my_strategy_name
elif my_points_total == opp_points_total:
    winner = "none"
else:
    winner = opp_strategy_name

