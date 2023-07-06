from arrays import players
def APT_sort():
    x=sorted( players, key=lambda player: player.APT, reverse=True)
    for i in x:
        print(i)