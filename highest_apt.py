from arrays import players
def highest_APT():
    l=sorted(players, key=lambda player: player.APT, reverse=True)
    print(l[0])