ip =  open('dec2_input.txt')
strategy = []
for line in ip:
    new_line = line.replace("\n", "")
    split = new_line.split(" ")
    strategy.append([split[0],split[1]])
ip.close()

winning_combos = {'A':'C','C':'B','B':'A'} #where A=rock, B=paper, C=scissors
scores = {'A':1,'B':2,'C':3}
outcome = {'loss':0,'draw':3,'win':6}
#counter_mapping = {'X':'A','Y':'B','Z':'C'} #for part 1
counter_mapping = {'X':'loss','Y':'draw','Z':'win'} #for part 2

print(len(strategy))
score = []
for first_move,counter in strategy[:]:
    #counter_move = counter_mapping[counter] #for part 1
    strategy_outcome = counter_mapping[counter] #for part 2
    if strategy_outcome == 'win':
        counter_move = list(winning_combos.keys())[list(winning_combos.values()).index(first_move)]
    elif strategy_outcome == 'draw':
        counter_move = first_move
    else:
        counter_move = winning_combos[first_move]
    current_score = scores[counter_move]
    if winning_combos[counter_move] == first_move:
        current_score += outcome['win']
    elif first_move == counter_move: #draw
        current_score += outcome['draw']
    else:
        current_score += outcome['loss']
    score.append(current_score)
    #print("first move:",first_move,"counter:",counter_move,"score:",score)
print(sum(score))