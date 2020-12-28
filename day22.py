# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Part 1

# +
f = open('data/day22_data.csv')
player1 = []
player2 = []
switch = False
for line in f:
    try:
        if not switch:
            player1.append(int(line.rstrip('\n')))
        else:
            player2.append(int(line.rstrip('\n')))
    except:
        pass
    if line.startswith('Player 2:'):
        switch = True

playing = True
while playing:
    pl1 = player1[0]
    pl2 = player2[0]
    player1.remove(pl1)
    player2.remove(pl2)
    if pl1 > pl2:
        player1.append(pl1)
        player1.append(pl2)
    else:
        player2.append(pl2)
        player2.append(pl1)
    if (len(player1)==0) or (len(player2)==0):
        playing = False
        winner = 'player 1' if len(player1)!=0 else 'player 2'
        winners_list = player1 if len(player1)!=0 else player2

score = 0
for idx, i in enumerate(winners_list):
    score += i*(len(winners_list) - idx)
score


# -

def play_game(player1, player2):
    config = []
    playing = True
    while playing:
        won = 0
        current = player1 + [0] + player2
        if current in config:
            return 1, player1
        else:
            config.append(current)
        pl1 = player1[0]
        pl2 = player2[0]
        player1.remove(pl1)
        player2.remove(pl2)
        if (pl1<=len(player1)) & (pl2<=len(player2)):
            subpl1 = player1[:pl1].copy()
            subpl2 = player2[:pl2].copy()
            won, _ = play_game(subpl1, subpl2)
        elif pl1 > pl2:
            won = 1
        else:
            won = 2
        if won==1:
            player1.append(pl1)
            player1.append(pl2)
        elif won==2:
            player2.append(pl2)
            player2.append(pl1)
        if (len(player1)==0) or (len(player2)==0):
            playing = False
            winner = 1 if len(player1)!=0 else 2
            winners_list = player1 if len(player1)!=0 else player2
            return winner, winners_list


# +
f = open('data/day22_data.csv')
player1 = []
player2 = []
switch = False
for line in f:
    try:
        if not switch:
            player1.append(int(line.rstrip('\n')))
        else:
            player2.append(int(line.rstrip('\n')))
    except:
        pass
    if line.startswith('Player 2:'):
        switch = True

winner, winners_list = play_game(player1, player2)
print(winner, winners_list)
score = 0
for idx, i in enumerate(winners_list):
    score += i*(len(winners_list) - idx)
score
