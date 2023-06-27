from arrays import players
def highest_APT():
    print("ID First Name Last Name APT SET Nationality Position")
    l=sorted(players, key=lambda player: player.APT, reverse=True)
    print(l[0])