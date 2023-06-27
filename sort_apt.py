from arrays import players
def APT_sort():
    print("ID First Name Last Name APT SET Nationality Position")
    x=sorted( players, key=lambda player: player.APT, reverse=True)
    for i in x:
        print(i)